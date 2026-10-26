def build_original_tree(query):
    """Monta a arvore que representa diretamente a consulta recebida."""
    current = table_node(query["from"])

    for join in query["joins"]:
        current = {
            "operator": "join",
            "condition": join["condition"],
            "children": [current, table_node(join["table"])],
            "optimized": False,
        }

    if query["where"] is not None:
        current = {
            "operator": "selection",
            "condition": query["where"],
            "children": [current],
            "optimized": False,
        }

    return {
        "operator": "projection",
        "columns": query["select"],
        "children": [current],
        "final": True,
        "optimized": False,
    }


def table_node(source):
    return {
        "operator": "table",
        "table": source["name"],
        "alias": source["alias"],
        "children": [],
    }


def tree_to_algebra(node):
    operator = node["operator"]

    if operator == "table":
        if node["alias"].casefold() == node["table"].casefold():
            return node["table"]
        return f"ρ_{{{node['alias']}}}({node['table']})"

    if operator == "selection":
        child = tree_to_algebra(node["children"][0])
        return f"σ_{{{format_condition(node['condition'])}}}({child})"

    if operator == "projection":
        child = tree_to_algebra(node["children"][0])
        columns = format_columns(node["columns"])
        return f"π_{{{columns}}}({child})"

    left = tree_to_algebra(node["children"][0])
    right = tree_to_algebra(node["children"][1])
    condition = format_condition(node["condition"])
    return f"({left} ⋈_{{{condition}}} {right})"


def format_columns(columns):
    return ", ".join(format_reference(column) for column in columns)


def format_condition(condition):
    if condition["type"] == "comparison":
        left = format_reference(condition["left"])
        right = format_reference(condition["right"])
        return f"{left} {condition['operator']} {right}"

    return " ∧ ".join(format_condition(child) for child in condition["conditions"])


def format_reference(reference):
    if isinstance(reference, str):
        return reference

    if reference["type"] == "literal":
        return reference["value"]

    if reference["type"] == "star":
        if reference["table"] is None:
            return "*"
        return f"{reference.get('resolved_alias', reference['table'])}.*"

    alias = reference.get("resolved_alias")
    column = reference.get("resolved_name", reference["name"])
    return f"{alias}.{column}" if alias else column


def combine_conditions(conditions):
    if len(conditions) == 1:
        return conditions[0]
    return {"type": "and", "conditions": conditions}
