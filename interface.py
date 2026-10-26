import streamlit as st

from query_processor import process_query
from sql_parser import SQLSemanticError, SQLSyntaxError
from visualization import (
    load_styles,
    render_algebra,
    render_execution_plan,
    render_header,
    render_metadata,
    render_pipeline,
    render_query_summary,
    render_tree,
)


EXAMPLES = {
    "Seleção simples": (
        "SELECT Nome, Preco\n"
        "FROM Produto\n"
        "WHERE Preco > 100"
    ),
    "Uma junção": (
        "SELECT Produto.Nome, Categoria.Descricao\n"
        "FROM Produto\n"
        "JOIN Categoria ON Produto.Categoria_idCategoria = Categoria.idCategoria\n"
        "WHERE Produto.Preco >= 100"
    ),
    "Múltiplas junções": (
        "SELECT Pedido.idPedido, Produto.Nome, Categoria.Descricao\n"
        "FROM Pedido\n"
        "JOIN Pedido_has_Produto ON "
        "Pedido.idPedido = Pedido_has_Produto.Pedido_idPedido\n"
        "JOIN Produto ON "
        "Pedido_has_Produto.Produto_idProduto = Produto.idProduto\n"
        "JOIN Categoria ON "
        "Produto.Categoria_idCategoria = Categoria.idCategoria\n"
        "WHERE Pedido.ValorTotalPedido > 500 AND Produto.Preco > 100"
    ),
}


def initialize_state():
    if "sql_input" not in st.session_state:
        st.session_state.sql_input = EXAMPLES["Uma junção"]
    if "result" not in st.session_state:
        st.session_state.result = None
    if "error" not in st.session_state:
        st.session_state.error = None


def load_example():
    st.session_state.sql_input = EXAMPLES[st.session_state.example_selector]
    st.session_state.result = None
    st.session_state.error = None


def analyze_query(sql):
    try:
        st.session_state.result = process_query(sql)
        st.session_state.error = None
    except SQLSyntaxError as error:
        st.session_state.result = None
        st.session_state.error = ("Erro sintático", str(error))
    except SQLSemanticError as error:
        st.session_state.result = None
        st.session_state.error = ("Erro semântico", str(error))


def render_sidebar():
    with st.sidebar:
        st.header("Consulta de exemplo")
        st.caption("Use um exemplo ou escreva sua própria consulta SQL.")
        st.selectbox(
            "Exemplo",
            list(EXAMPLES),
            index=1,
            key="example_selector",
            on_change=load_example,
        )

        st.divider()
        st.markdown("##### Subconjunto aceito")
        st.code(
            "SELECT  FROM  WHERE\n"
            "JOIN  ON  AND\n"
            "=  >  <  <=  >=  <>\n"
            "( )",
            language=None,
        )
        st.caption(
            "Palavras-chave, tabelas e colunas não diferenciam maiúsculas "
            "de minúsculas. Espaços repetidos são ignorados."
        )

        st.divider()
        st.markdown("##### Legenda dos grafos")
        st.markdown(":blue[**Azul:** projeção]")
        st.markdown(":green[**Verde:** seleção]")
        st.markdown(":orange[**Laranja:** junção]")
        st.markdown(":gray[**Cinza:** tabela]")


def render_analysis_area():
    st.subheader("Consulta SQL")
    render_pipeline()

    with st.form("query_form"):
        sql = st.text_area(
            "Digite a consulta",
            key="sql_input",
            height=210,
            help="O processador não executa a consulta; ele valida e monta o plano.",
        )
        submitted = st.form_submit_button(
            "Analisar", type="primary", width="stretch"
        )

    if submitted:
        analyze_query(sql)

    if st.session_state.error is not None:
        error_type, message = st.session_state.error
        st.error(f"**{error_type}:** {message}")
        return

    result = st.session_state.result
    if result is None:
        st.info("Digite uma consulta e clique em Analisar consulta.")
        return

    st.success("Consulta sintática e semanticamente válida.")
    st.markdown("#### Consulta normalizada")
    st.code(result["query"]["normalized_sql"], language="sql", wrap_lines=True)
    render_query_summary(result["query"])


def create_app():
    st.set_page_config(
        page_title="Processador de Consultas",
        page_icon="🌳",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    load_styles()
    initialize_state()
    render_sidebar()
    render_header(st.session_state.result is not None)

    tabs = st.tabs(
        [
            "1 · Análise",
            "2 · Álgebra relacional",
            "3 · Grafo original",
            "4 · Grafo otimizado",
            "5 · Plano de execução",
            "6 · Metadados",
        ]
    )

    with tabs[0]:
        render_analysis_area()

    result = st.session_state.result

    with tabs[1]:
        st.subheader("Conversão e otimização")
        if result is None:
            st.info("Analise uma consulta válida para gerar a álgebra relacional.")
        else:
            render_algebra(result)

    with tabs[2]:
        st.subheader("Grafo de operadores original")
        st.caption("Folhas são tabelas; nós internos são operadores; a raiz é a projeção final.")
        if result is None:
            st.info("Analise uma consulta válida para construir o grafo original.")
        else:
            render_tree(result["original_tree"])

    with tabs[3]:
        st.subheader("Grafo de operadores otimizado")
        st.caption("Árvore equivalente após redução de tuplas, atributos e reordenação segura.")
        if result is None:
            st.info("Analise uma consulta válida para construir o grafo otimizado.")
        else:
            render_tree(result["optimized_tree"])

    with tabs[4]:
        st.subheader("Plano de execução")
        st.caption("A ordem é apresentada de baixo para cima na árvore otimizada.")
        if result is None:
            st.info("Analise uma consulta válida para gerar o plano de execução.")
        else:
            render_execution_plan(result["execution_plan"])

    with tabs[5]:
        render_metadata()
