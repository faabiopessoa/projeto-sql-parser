import unittest
from pathlib import Path

from streamlit.testing.v1 import AppTest


class InterfaceTests(unittest.TestCase):
    def create_app(self):
        main_file = Path(__file__).resolve().parents[1] / "main.py"
        return AppTest.from_file(main_file, default_timeout=30).run()

    def test_initial_screen_has_no_exception(self):
        app = self.create_app()

        self.assertEqual(len(app.exception), 0)
        self.assertEqual(len(app.text_area), 1)

    def test_valid_query_builds_the_complete_pipeline(self):
        app = self.create_app()
        next(
            button
            for button in app.button
            if button.label == "Analisar"
        ).click().run()

        self.assertEqual(len(app.exception), 0)
        self.assertIsNotNone(app.session_state.result)
        self.assertIn("⋈", app.session_state.result["optimized_algebra"])

    def test_syntactic_and_semantic_errors_are_distinguished(self):
        for sql, expected_type in (
            ("SELECT Nome Produto", "Erro sintático"),
            ("SELECT ColunaInexistente FROM Produto", "Erro semântico"),
        ):
            with self.subTest(sql=sql):
                app = self.create_app()
                app.text_area[0].set_value(sql)
                next(
                    button
                    for button in app.button
                    if button.label == "Analisar"
                ).click().run()

                self.assertEqual(len(app.exception), 0)
                self.assertEqual(app.session_state.error[0], expected_type)


if __name__ == "__main__":
    unittest.main()
