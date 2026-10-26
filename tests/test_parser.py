import unittest

from query_processor import process_query
from sql_parser import SQLSemanticError, SQLSyntaxError, parse_sql


class ParserTests(unittest.TestCase):
    def test_simple_select_and_where(self):
        query = parse_sql(
            "SELECT Nome, Preco FROM Produto WHERE Preco > 100"
        )

        self.assertEqual(query["from"]["name"], "Produto")
        self.assertEqual(query["select"][0]["resolved_name"], "Nome")
        self.assertEqual(query["where"]["operator"], ">")

    def test_case_spaces_parentheses_and_aliases_are_supported(self):
        query = parse_sql(
            "  select   p.nome, c.descricao  from produto p "
            " join categoria c on (p.categoria_idcategoria = c.idcategoria) "
            " where (p.preco >= 100); "
        )

        self.assertEqual(query["from"]["name"], "Produto")
        self.assertEqual(query["from"]["alias"], "p")
        self.assertEqual(query["joins"][0]["table"]["name"], "Categoria")

    def test_multiple_joins(self):
        query = parse_sql(
            "SELECT Pedido.idPedido, Produto.Nome "
            "FROM Pedido "
            "JOIN Pedido_has_Produto ON "
            "Pedido.idPedido = Pedido_has_Produto.Pedido_idPedido "
            "JOIN Produto ON "
            "Pedido_has_Produto.Produto_idProduto = Produto.idProduto"
        )

        self.assertEqual(len(query["joins"]), 2)

    def test_missing_keyword_is_syntactic_error(self):
        with self.assertRaises(SQLSyntaxError):
            parse_sql("SELECT Nome Produto")

    def test_unclosed_parenthesis_is_syntactic_error(self):
        with self.assertRaises(SQLSyntaxError):
            parse_sql("SELECT Nome FROM Produto WHERE (Preco > 100")

    def test_unknown_table_is_semantic_error(self):
        with self.assertRaises(SQLSemanticError):
            parse_sql("SELECT Nome FROM TabelaInexistente")

    def test_unknown_column_is_semantic_error(self):
        with self.assertRaises(SQLSemanticError):
            parse_sql("SELECT ColunaInexistente FROM Produto")

    def test_ambiguous_column_is_semantic_error(self):
        with self.assertRaises(SQLSemanticError):
            parse_sql(
                "SELECT Descricao FROM Produto "
                "JOIN Categoria ON "
                "Produto.Categoria_idCategoria = Categoria.idCategoria"
            )

    def test_join_must_connect_new_table(self):
        with self.assertRaises(SQLSemanticError):
            parse_sql(
                "SELECT Produto.Nome FROM Produto "
                "JOIN Categoria ON Produto.idProduto = Produto.idProduto"
            )

    def test_join_cannot_reference_a_table_added_later(self):
        with self.assertRaises(SQLSemanticError):
            parse_sql(
                "SELECT Produto.Nome FROM Produto "
                "JOIN Categoria ON "
                "Produto.Categoria_idCategoria = Categoria.idCategoria "
                "AND Pedido.Cliente_idCliente = Produto.idProduto "
                "JOIN Pedido ON Pedido.idPedido = Produto.idProduto"
            )

    def test_star_and_table_star_are_supported(self):
        all_columns = parse_sql("SELECT * FROM Produto")
        table_columns = parse_sql("SELECT Produto.* FROM Produto")

        self.assertEqual(all_columns["select"][0]["type"], "star")
        self.assertEqual(
            table_columns["select"][0]["resolved_table"], "Produto"
        )

    def test_empty_query_is_syntactic_error(self):
        with self.assertRaises(SQLSyntaxError):
            parse_sql("   ")

    def test_unsupported_or_is_syntactic_error(self):
        with self.assertRaises(SQLSyntaxError):
            parse_sql(
                "SELECT Nome FROM Produto "
                "WHERE Preco > 100 OR QuantEstoque > 0"
            )


class ProcessorTests(unittest.TestCase):
    def test_processor_generates_required_outputs(self):
        result = process_query(
            "SELECT Produto.Nome, Categoria.Descricao "
            "FROM Produto "
            "JOIN Categoria ON "
            "Produto.Categoria_idCategoria = Categoria.idCategoria "
            "WHERE Produto.Preco > 100"
        )

        self.assertIn("π", result["original_algebra"])
        self.assertIn("σ", result["optimized_algebra"])
        self.assertIn("⋈", result["optimized_algebra"])
        self.assertTrue(result["heuristics"])
        self.assertGreater(len(result["execution_plan"]), 0)

    def test_selection_is_moved_near_its_table(self):
        result = process_query(
            "SELECT Produto.Nome, Categoria.Descricao "
            "FROM Produto "
            "JOIN Categoria ON "
            "Produto.Categoria_idCategoria = Categoria.idCategoria "
            "WHERE Produto.Preco > 100"
        )
        optimized = result["optimized_tree"]

        self.assertEqual(optimized["operator"], "projection")
        self.assertTrue(
            any("Redução de tuplas" in item for item in result["heuristics"])
        )

    def test_more_restrictive_selection_is_executed_first(self):
        result = process_query(
            "SELECT Nome FROM Produto "
            "WHERE Preco <> 100 AND QuantEstoque = 1"
        )
        selection_steps = [
            item["operation"]
            for item in result["execution_plan"]
            if item["operation"].startswith("Aplicar seleção")
        ]

        self.assertIn("QuantEstoque = 1", selection_steps[0])

    def test_multiple_joins_are_reordered_from_restrictive_table(self):
        result = process_query(
            "SELECT Pedido.idPedido, Produto.Nome "
            "FROM Pedido "
            "JOIN Pedido_has_Produto ON "
            "Pedido.idPedido = Pedido_has_Produto.Pedido_idPedido "
            "JOIN Produto ON "
            "Pedido_has_Produto.Produto_idProduto = Produto.idProduto "
            "WHERE Produto.Preco = 100"
        )

        self.assertTrue(
            any(
                "Produto → Pedido_has_Produto → Pedido" in item
                for item in result["heuristics"]
            )
        )
        self.assertTrue(
            any("Redução de atributos" in item for item in result["heuristics"])
        )
        self.assertTrue(
            result["execution_plan"][-1]["operation"].startswith("Projetar")
        )


if __name__ == "__main__":
    unittest.main()
