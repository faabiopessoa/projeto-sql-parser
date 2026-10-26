from metadata import TABLES
from relational_algebra import (
    combine_conditions,
    format_columns,
    format_condition,
    table_node,
)
from sql_parser import condition_aliases, flatten_conditions


def optimize_query(query):
    """Aplica as heuristicas solicitadas e retorna a arvore equivalente."""
    sources = [query["from"]] + [join["table"] for join in query["joins"]]
    source_by_alias = {
        source["alias"].casefold(): source for source in sources
    }
    original_order = [source["alias"].casefold() for source in sources]
    predicates = flatten_conditions(query["where"])
    local_predicates = {alias: [] for alias in source_by_alias}
    remaining_predicates = []
    heuristics = []

    for predicate in predicates:
        aliases = condition_aliases(predicate)
        if len(aliases) == 1:
            local_predicates[next(iter(aliases))].append(predicate)
        else:
            remaining_predicates.append(predicate)

    required_columns, unrestricted_aliases = _required_columns(query, sources)
    leaves = {}

    for alias, source in source_by_alias.items():
        node = table_node(source)

        ordered_predicates = sorted(
            local_predicates[alias], key=_predicate_score, reverse=True
        )
        for position, predicate in enumerate(ordered_predicates):
            node = {
                "operator": "selection",
                "condition": predicate,
                "children": [node],
                "optimized": True,
            }
            priority = ""
            if len(ordered_predicates) > 1 and position == 0:
                priority = " estimada como mais restritiva e"
            heuristics.append(
                f"Redução de tuplas: a seleção{priority} "
                f"{format_condition(predicate)} foi aproximada da tabela "
                f"{source['alias']}."
            )

        official_columns = TABLES[source["name"]]
        needed = required_columns[alias]

        if (
            len(sources) > 1
            and alias not in unrestricted_aliases
            and 0 < len(needed) < len(official_columns)
        ):
            ordered_columns = [
                f"{source['alias']}.{column}"
                for column in official_columns
                if column.casefold() in needed
            ]
            node = {
                "operator": "projection",
                "columns": ordered_columns,
                "children": [node],
                "final": False,
                "optimized": True,
            }
            heuristics.append(
                "Redução de atributos: a tabela "
                f"{source['alias']} mantém somente "
                f"{', '.join(ordered_columns)}."
            )

        leaves[alias] = node

    join_edges = []
    for position, join in enumerate(query["joins"]):
        aliases = condition_aliases(join["condition"])
        join_edges.append(
            {
                "condition": join["condition"],
                "aliases": aliases,
                "position": position,
            }
        )

    join_order = _choose_join_order(
        original_order, local_predicates, join_edges
    )
    current = leaves[join_order[0]]
    joined = {join_order[0]}
    used_edges = set()

    for alias in join_order[1:]:
        edge_index = _find_connecting_edge(
            alias, joined, join_edges, used_edges
        )
        edge = join_edges[edge_index]
        used_edges.add(edge_index)
        current = {
            "operator": "join",
            "condition": edge["condition"],
            "children": [current, leaves[alias]],
            "optimized": True,
        }
        joined.add(alias)

    if join_edges:
        displayed_order = " → ".join(
            source_by_alias[alias]["alias"] for alias in join_order
        )
        if join_order != original_order:
            heuristics.append(
                "Junções mais restritivas primeiro: ordem escolhida "
                f"{displayed_order}."
            )
        heuristics.append(
            "Produto cartesiano evitado: todas as tabelas são combinadas "
            "por condições explícitas de junção."
        )

    if remaining_predicates:
        current = {
            "operator": "selection",
            "condition": combine_conditions(remaining_predicates),
            "children": [current],
            "optimized": True,
        }

    tree = {
        "operator": "projection",
        "columns": query["select"],
        "children": [current],
        "final": True,
        "optimized": True,
    }

    return tree, heuristics


def generate_execution_plan(tree):
    steps = []

    def visit(node):
        for child in node["children"]:
            visit(child)

        operator = node["operator"]
        if operator == "table":
            description = f"Ler a tabela {node['table']}"
            if node["alias"].casefold() != node["table"].casefold():
                description += f" com alias {node['alias']}"
            heuristic = "Folha da árvore: relação de entrada."
        elif operator == "selection":
            description = f"Aplicar seleção: {format_condition(node['condition'])}"
            heuristic = "Redução de tuplas antes das operações superiores."
        elif operator == "projection":
            description = f"Projetar: {format_columns(node['columns'])}"
            heuristic = (
                "Produzir somente os atributos solicitados."
                if node.get("final")
                else "Redução antecipada de atributos."
            )
        else:
            description = f"Executar junção: {format_condition(node['condition'])}"
            heuristic = "Junção com condição explícita, evitando produto cartesiano."

        steps.append(
            {
                "step": len(steps) + 1,
                "operation": description,
                "heuristic": heuristic,
            }
        )

    visit(tree)
    return steps


def _required_columns(query, sources):
    required = {source["alias"].casefold(): set() for source in sources}
    unrestricted = set()

    references = list(query["select"])
    for join in query["joins"]:
        references.extend(_condition_references(join["condition"]))

    for predicate in flatten_conditions(query["where"]):
        if len(condition_aliases(predicate)) != 1:
            references.extend(_condition_references(predicate))

    for reference in references:
        if reference["type"] == "literal":
            continue
        if reference["type"] == "star":
            if reference["table"] is None:
                unrestricted.update(required)
            else:
                unrestricted.add(reference["resolved_alias"].casefold())
            continue

        alias = reference["resolved_alias"].casefold()
        required[alias].add(reference["resolved_name"].casefold())

    return required, unrestricted


def _condition_references(condition):
    references = []

    for comparison in flatten_conditions(condition):
        references.extend([comparison["left"], comparison["right"]])

    return references


def _choose_join_order(original_order, local_predicates, join_edges):
    if len(original_order) == 1:
        return original_order

    scores = {
        alias: sum(_predicate_score(item) for item in predicates)
        for alias, predicates in local_predicates.items()
    }
    first = max(
        original_order,
        key=lambda alias: (scores[alias], -original_order.index(alias)),
    )
    order = [first]
    joined = {first}
    used_edges = set()

    while len(order) < len(original_order):
        candidates = []

        for alias in original_order:
            if alias in joined:
                continue

            edge_index = _find_connecting_edge(
                alias, joined, join_edges, used_edges, required=False
            )
            if edge_index is not None:
                edge = join_edges[edge_index]
                candidates.append(
                    (
                        scores[alias] + _condition_score(edge["condition"]),
                        -original_order.index(alias),
                        alias,
                        edge_index,
                    )
                )

        if not candidates:
            return original_order

        _, _, alias, edge_index = max(candidates)
        order.append(alias)
        joined.add(alias)
        used_edges.add(edge_index)

    return order


def _find_connecting_edge(
    alias, joined, join_edges, used_edges, required=True
):
    for index, edge in enumerate(join_edges):
        if index in used_edges or alias not in edge["aliases"]:
            continue
        if edge["aliases"].issubset(joined | {alias}) and edge["aliases"].intersection(joined):
            return index

    if required:
        raise ValueError("Não foi possível montar as junções sem produto cartesiano.")
    return None


def _predicate_score(predicate):
    return {"=": 4, ">": 2, "<": 2, ">=": 2, "<=": 2, "<>": 1}[
        predicate["operator"]
    ]


def _condition_score(condition):
    return sum(_predicate_score(item) for item in flatten_conditions(condition))
