import re
from dataclasses import dataclass

from metadata import TABLES, find_column, find_table, tables_with_column


KEYWORDS = {
    "SELECT",
    "FROM",
    "WHERE",
    "JOIN",
    "ON",
    "AND",
    "AS",
}

RESERVED_WORDS = KEYWORDS | {
    "ALL",
    "ALTER",
    "BETWEEN",
    "BY",
    "CREATE",
    "CROSS",
    "DELETE",
    "DISTINCT",
    "DROP",
    "FULL",
    "GROUP",
    "HAVING",
    "IN",
    "INNER",
    "INSERT",
    "INTO",
    "IS",
    "LEFT",
    "LIKE",
    "LIMIT",
    "NOT",
    "NULL",
    "OR",
    "ORDER",
    "OUTER",
    "RIGHT",
    "SET",
    "TABLE",
    "UNION",
    "UPDATE",
    "VALUES",
}

TOKEN_PATTERN = re.compile(
    r"(?P<SPACE>\s+)"
    r"|(?P<STRING>'(?:''|[^'])*'|\"(?:\"\"|[^\"])*\")"
    r"|(?P<NUMBER>\d+(?:\.\d+)?)"
    r"|(?P<OPERATOR><=|>=|<>|=|<|>)"
    r"|(?P<LPAREN>\()"
    r"|(?P<RPAREN>\))"
    r"|(?P<COMMA>,)"
    r"|(?P<DOT>\.)"
    r"|(?P<STAR>\*)"
    r"|(?P<SEMICOLON>;)"
    r"|(?P<IDENTIFIER>[A-Za-z_À-ÖØ-öø-ÿ][A-Za-z0-9_À-ÖØ-öø-ÿ]*)"
    r"|(?P<INVALID>.)",
    re.UNICODE,
)


class SQLSyntaxError(ValueError):
    pass


class SQLSemanticError(ValueError):
    pass


@dataclass(frozen=True)
class Token:
    kind: str
    value: str
    position: int


def tokenize(sql):
    """Transforma a consulta em tokens simples e verificaveis."""
    if not isinstance(sql, str) or not sql.strip():
        raise SQLSyntaxError("A consulta SQL esta vazia.")

    tokens = []

    for match in TOKEN_PATTERN.finditer(sql):
        kind = match.lastgroup
        value = match.group()

        if kind == "SPACE":
            continue
        if kind == "INVALID":
            raise SQLSyntaxError(
                f"Caractere invalido '{value}' na posicao {match.start()}."
            )

        tokens.append(Token(kind, value, match.start()))

    tokens.append(Token("EOF", "", len(sql)))
    return tokens


class SQLParser:
    """Parser descendente para o subconjunto SQL exigido no trabalho."""

    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0

    def parse(self):
        self._expect_keyword("SELECT")
        selected_columns = self._parse_select_list()
        self._expect_keyword("FROM")
        from_table = self._parse_table_reference()
        joins = []

        while self._match_keyword("JOIN"):
            table = self._parse_table_reference()
            self._expect_keyword("ON")
            condition = self._parse_condition()
            joins.append({"table": table, "condition": condition})

        where = None
        if self._match_keyword("WHERE"):
            where = self._parse_condition()

        self._match("SEMICOLON")
        if not self._check("EOF"):
            token = self._peek()
            raise SQLSyntaxError(
                f"Token inesperado '{token.value}' na posicao {token.position}."
            )

        return {
            "select": selected_columns,
            "from": from_table,
            "joins": joins,
            "where": where,
        }

    def _parse_select_list(self):
        if self._match("STAR"):
            return [{"type": "star", "table": None}]

        columns = [self._parse_column_reference(allow_table_star=True)]

        while self._match("COMMA"):
            columns.append(self._parse_column_reference(allow_table_star=True))

        return columns

    def _parse_table_reference(self):
        table_token = self._expect("IDENTIFIER", "Esperado o nome de uma tabela.")
        alias = None

        if self._match_keyword("AS"):
            alias = self._expect(
                "IDENTIFIER", "Esperado um alias depois de AS."
            ).value
        elif self._check("IDENTIFIER") and not self._is_keyword(self._peek()):
            alias = self._advance().value

        return {"name": table_token.value, "alias": alias}

    def _parse_condition(self):
        conditions = [self._parse_condition_factor()]

        while self._match_keyword("AND"):
            conditions.append(self._parse_condition_factor())

        if len(conditions) == 1:
            return conditions[0]

        return {"type": "and", "conditions": conditions}

    def _parse_condition_factor(self):
        if self._match("LPAREN"):
            condition = self._parse_condition()
            self._expect("RPAREN", "Parenteses de fechamento ausente.")
            return condition

        left = self._parse_operand()
        operator = self._expect(
            "OPERATOR",
            "Esperado um operador de comparacao (=, >, <, <=, >= ou <>).",
        )
        right = self._parse_operand()
        return {
            "type": "comparison",
            "operator": operator.value,
            "left": left,
            "right": right,
        }

    def _parse_operand(self):
        if self._match("STRING"):
            token = self._previous()
            return {"type": "literal", "value": token.value, "data_type": "text"}

        if self._match("NUMBER"):
            token = self._previous()
            return {"type": "literal", "value": token.value, "data_type": "number"}

        return self._parse_column_reference()

    def _parse_column_reference(self, allow_table_star=False):
        first = self._expect("IDENTIFIER", "Esperado o nome de uma coluna.")

        if self._match("DOT"):
            if allow_table_star and self._match("STAR"):
                return {"type": "star", "table": first.value}

            second = self._expect(
                "IDENTIFIER", "Esperado o nome da coluna depois do ponto."
            )
            return {
                "type": "column",
                "table": first.value,
                "name": second.value,
            }

        return {"type": "column", "table": None, "name": first.value}

    def _expect_keyword(self, keyword):
        if self._match_keyword(keyword):
            return self._previous()

        token = self._peek()
        raise SQLSyntaxError(
            f"Esperado {keyword} na posicao {token.position}; "
            f"encontrado '{token.value or 'fim da consulta'}'."
        )

    def _match_keyword(self, keyword):
        if self._check("IDENTIFIER") and self._peek().value.upper() == keyword:
            self._advance()
            return True

        return False

    def _is_keyword(self, token):
        return token.kind == "IDENTIFIER" and token.value.upper() in RESERVED_WORDS

    def _expect(self, kind, message):
        if self._check(kind):
            if kind == "IDENTIFIER" and self._is_keyword(self._peek()):
                token = self._peek()
                raise SQLSyntaxError(
                    f"{message} '{token.value}' e uma palavra reservada. "
                    f"Posicao {token.position}."
                )
            return self._advance()

        token = self._peek()
        raise SQLSyntaxError(f"{message} Posicao {token.position}.")

    def _match(self, kind):
        if self._check(kind):
            self._advance()
            return True

        return False

    def _check(self, kind):
        return self._peek().kind == kind

    def _advance(self):
        token = self._peek()
        if token.kind != "EOF":
            self.current += 1
        return token

    def _peek(self):
        return self.tokens[self.current]

    def _previous(self):
        return self.tokens[self.current - 1]


def parse_sql(sql):
    """Executa analise lexica, sintatica e semantica."""
    tokens = tokenize(sql)
    query = SQLParser(tokens).parse()
    validate_semantics(query)
    query["tokens"] = [token.value for token in tokens if token.kind != "EOF"]
    query["normalized_sql"] = normalize_tokens(tokens)
    return query


def validate_semantics(query):
    sources = [query["from"]] + [join["table"] for join in query["joins"]]
    aliases = {}
    alias_names = {}
    table_names = []

    for source in sources:
        official_table = find_table(source["name"])
        if official_table is None:
            raise SQLSemanticError(f"A tabela '{source['name']}' nao existe.")

        source["name"] = official_table
        source["alias"] = source["alias"] or official_table
        alias_key = source["alias"].casefold()

        if alias_key in aliases:
            raise SQLSemanticError(f"O alias '{source['alias']}' esta repetido.")

        aliases[alias_key] = official_table
        alias_names[alias_key] = source["alias"]
        table_names.append(official_table)

    for column in query["select"]:
        _resolve_reference(column, aliases, alias_names, table_names)

    available_aliases = {query["from"]["alias"].casefold()}

    for join in query["joins"]:
        joined_alias = join["table"]["alias"].casefold()
        _validate_condition(join["condition"], aliases, alias_names, table_names)
        referenced_aliases = condition_aliases(join["condition"])
        allowed_aliases = available_aliases | {joined_alias}

        if joined_alias not in referenced_aliases:
            raise SQLSemanticError(
                f"A condicao ON deve referenciar a tabela '{join['table']['alias']}'."
            )
        if not referenced_aliases.intersection(available_aliases):
            raise SQLSemanticError(
                "A condicao ON deve conectar a nova tabela a uma tabela anterior."
            )
        if not referenced_aliases.issubset(allowed_aliases):
            raise SQLSemanticError(
                "A condicao ON nao pode usar uma tabela que ainda nao foi adicionada."
            )

        available_aliases.add(joined_alias)

    if query["where"] is not None:
        _validate_condition(query["where"], aliases, alias_names, table_names)

    query["aliases"] = aliases
    query["alias_names"] = alias_names


def _validate_condition(condition, aliases, alias_names, table_names):
    if condition["type"] == "and":
        for child in condition["conditions"]:
            _validate_condition(child, aliases, alias_names, table_names)
        return

    _resolve_reference(condition["left"], aliases, alias_names, table_names)
    _resolve_reference(condition["right"], aliases, alias_names, table_names)


def _resolve_reference(reference, aliases, alias_names, table_names):
    if reference["type"] == "literal":
        return

    if reference["type"] == "star":
        if reference["table"] is None:
            return

        alias_key = reference["table"].casefold()
        if alias_key not in aliases:
            raise SQLSemanticError(
                f"A tabela ou alias '{reference['table']}' nao participa da consulta."
            )

        reference["resolved_table"] = aliases[alias_key]
        reference["resolved_alias"] = alias_names[alias_key]
        return

    if reference["table"] is not None:
        alias_key = reference["table"].casefold()
        if alias_key not in aliases:
            raise SQLSemanticError(
                f"A tabela ou alias '{reference['table']}' nao participa da consulta."
            )

        table_name = aliases[alias_key]
        column_name = find_column(table_name, reference["name"])
        if column_name is None:
            raise SQLSemanticError(
                f"A coluna '{reference['name']}' nao existe na tabela '{table_name}'."
            )

        reference["resolved_table"] = table_name
        reference["resolved_alias"] = alias_names[alias_key]
        reference["resolved_name"] = column_name
        return

    matching_tables = tables_with_column(table_names, reference["name"])
    unique_tables = list(dict.fromkeys(matching_tables))

    if len(unique_tables) == 0:
        raise SQLSemanticError(f"A coluna '{reference['name']}' nao existe.")
    if len(unique_tables) > 1:
        raise SQLSemanticError(
            f"A coluna '{reference['name']}' e ambigua. Informe a tabela."
        )

    table_name = unique_tables[0]
    aliases_for_table = [
        alias for alias, alias_table in aliases.items() if alias_table == table_name
    ]
    if len(aliases_for_table) > 1:
        raise SQLSemanticError(
            f"A coluna '{reference['name']}' e ambigua. Informe o alias."
        )

    reference["resolved_table"] = table_name
    reference["resolved_alias"] = alias_names[aliases_for_table[0]]
    reference["resolved_name"] = find_column(table_name, reference["name"])


def flatten_conditions(condition):
    if condition is None:
        return []
    if condition["type"] == "comparison":
        return [condition]

    flattened = []
    for child in condition["conditions"]:
        flattened.extend(flatten_conditions(child))
    return flattened


def condition_aliases(condition):
    aliases = set()

    for comparison in flatten_conditions(condition):
        for operand in (comparison["left"], comparison["right"]):
            if operand["type"] == "column" and "resolved_alias" in operand:
                aliases.add(operand["resolved_alias"].casefold())

    return aliases


def normalize_tokens(tokens):
    parts = []

    for token in tokens:
        if token.kind == "EOF":
            continue

        value = token.value.upper() if token.value.upper() in KEYWORDS else token.value

        if token.kind in {"COMMA", "RPAREN", "SEMICOLON"}:
            if parts:
                parts[-1] = parts[-1].rstrip()
            parts.append(value + " ")
        elif token.kind == "DOT":
            if parts:
                parts[-1] = parts[-1].rstrip()
            parts.append(".")
        elif token.kind == "LPAREN":
            parts.append("( ")
        else:
            parts.append(value + " ")

    normalized = "".join(parts).strip()
    return normalized.replace(". ", ".")
