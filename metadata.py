TABLES = {
    "Categoria": [
        "idCategoria",
        "Descricao",
    ],
    "Produto": [
        "idProduto",
        "Nome",
        "Descricao",
        "Preco",
        "QuantEstoque",
        "Categoria_idCategoria",
    ],
    "TipoCliente": [
        "idTipoCliente",
        "Descricao",
    ],
    "Cliente": [
        "idCliente",
        "Nome",
        "Email",
        "Nascimento",
        "Senha",
        "TipoCliente_idTipoCliente",
        "DataRegistro",
    ],
    "TipoEndereco": [
        "idTipoEndereco",
        "Descricao",
    ],
    "Endereco": [
        "idEndereco",
        "EnderecoPadrao",
        "Logradouro",
        "Numero",
        "Complemento",
        "Bairro",
        "Cidade",
        "UF",
        "CEP",
        "TipoEndereco_idTipoEndereco",
        "Cliente_idCliente",
    ],
    "Telefone": [
        "Numero",
        "Cliente_idCliente",
    ],
    "Status": [
        "idStatus",
        "Descricao",
    ],
    "Pedido": [
        "idPedido",
        "Status_idStatus",
        "DataPedido",
        "ValorTotalPedido",
        "Cliente_idCliente",
    ],
    "Pedido_has_Produto": [
        "idPedidoProduto",
        "Pedido_idPedido",
        "Produto_idProduto",
        "Quantidade",
        "PrecoUnitario",
    ],
}


RELATIONSHIPS = [
    ("Produto", "Categoria_idCategoria", "Categoria", "idCategoria"),
    ("Cliente", "TipoCliente_idTipoCliente", "TipoCliente", "idTipoCliente"),
    ("Endereco", "TipoEndereco_idTipoEndereco", "TipoEndereco", "idTipoEndereco"),
    ("Endereco", "Cliente_idCliente", "Cliente", "idCliente"),
    ("Telefone", "Cliente_idCliente", "Cliente", "idCliente"),
    ("Pedido", "Status_idStatus", "Status", "idStatus"),
    ("Pedido", "Cliente_idCliente", "Cliente", "idCliente"),
    ("Pedido_has_Produto", "Pedido_idPedido", "Pedido", "idPedido"),
    ("Pedido_has_Produto", "Produto_idProduto", "Produto", "idProduto"),
]


def find_table(table_name):
    """Retorna o nome oficial de uma tabela, ignorando maiusculas e minusculas."""
    searched_name = table_name.casefold()

    for official_name in TABLES:
        if official_name.casefold() == searched_name:
            return official_name

    return None


def find_column(table_name, column_name):
    """Retorna o nome oficial de uma coluna pertencente a uma tabela."""
    searched_name = column_name.casefold()

    for official_name in TABLES[table_name]:
        if official_name.casefold() == searched_name:
            return official_name

    return None


def tables_with_column(table_names, column_name):
    """Encontra as tabelas da consulta que possuem uma coluna sem qualificacao."""
    matches = []

    for table_name in table_names:
        if find_column(table_name, column_name) is not None:
            matches.append(table_name)

    return matches
