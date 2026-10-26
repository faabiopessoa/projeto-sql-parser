from html import escape
from pathlib import Path

import streamlit as st

from metadata import RELATIONSHIPS, TABLES
from relational_algebra import format_columns, format_condition


def load_styles():
    styles = Path(__file__).with_name("styles.css").read_text(encoding="utf-8")
    st.markdown(f"<style>{styles}</style>", unsafe_allow_html=True)


def render_header(has_result):
    status = "Consulta analisada" if has_result else "Aguardando consulta"
    st.markdown(
        f"""
        <div class="app-header">
            <div>
                <h1>Processador de Consultas</h1>
                <p>Parsing, álgebra relacional, otimização e plano de execução</p>
            </div>
            <div class="status-pill">{status}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_pipeline():
    steps = [
        "SQL",
        "Validação",
        "Álgebra",
        "Grafo original",
        "Otimização",
        "Plano",
    ]
    parts = []

    for position, step in enumerate(steps):
        parts.append(f'<div class="pipeline-step">{escape(step)}</div>')
        if position < len(steps) - 1:
            parts.append('<div class="pipeline-arrow">→</div>')

    st.markdown(
        f'<div class="pipeline">{"".join(parts)}</div>',
        unsafe_allow_html=True,
    )


def render_query_summary(query):
    sources = [query["from"]] + [join["table"] for join in query["joins"]]

    st.markdown("#### Estrutura reconhecida")
    columns = st.columns(4)
    columns[0].metric("Campos projetados", len(query["select"]))
    columns[1].metric("Tabelas", len(sources))
    columns[2].metric("Junções", len(query["joins"]))
    columns[3].metric(
        "Cláusula WHERE", "Sim" if query["where"] is not None else "Não"
    )

    st.write("**Projeção:**", format_columns(query["select"]))
    st.write(
        "**Relações:**",
        ", ".join(
            _source_label(source) for source in sources
        ),
    )

    if query["where"] is not None:
        st.write("**Condição:**", format_condition(query["where"]))

    with st.expander("Ver tokens produzidos pela análise léxica"):
        st.code(" | ".join(query["tokens"]), language=None)


def render_algebra(result):
    original_column, optimized_column = st.columns(2)

    with original_column:
        st.markdown("#### Expressão original")
        st.code(result["original_algebra"], language=None, wrap_lines=True)
        st.caption("Representação direta da estrutura informada na consulta SQL.")

    with optimized_column:
        st.markdown("#### Expressão otimizada")
        st.code(result["optimized_algebra"], language=None, wrap_lines=True)
        st.caption("Expressão equivalente após a aplicação das heurísticas.")

    st.markdown("#### Heurísticas aplicadas")
    if not result["heuristics"]:
        st.info("A consulta não exigiu uma transformação heurística adicional.")
    else:
        for position, heuristic in enumerate(result["heuristics"], 1):
            st.markdown(f"**{position}.** {heuristic}")


def render_tree(tree):
    st.graphviz_chart(tree_to_dot(tree), width="stretch")


def render_execution_plan(plan):
    for item in plan:
        st.markdown(
            f"""
            <div class="plan-step">
                <span>{item['step']}</span>
                <div>
                    <strong>{escape(item['operation'])}</strong>
                    <small>{escape(item['heuristic'])}</small>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_metadata():
    st.markdown("### Modelo relacional aceito")
    st.caption(
        "A validação semântica permite somente as tabelas e colunas abaixo."
    )

    for table_name, columns in TABLES.items():
        with st.expander(f"{table_name} · {len(columns)} campos"):
            st.code(", ".join(columns), language=None, wrap_lines=True)

    st.markdown("### Relacionamentos de referência")
    for left_table, left_column, right_table, right_column in RELATIONSHIPS:
        st.code(
            f"{left_table}.{left_column} = {right_table}.{right_column}",
            language=None,
        )


def tree_to_dot(tree):
    lines = [
        "digraph QueryTree {",
        'graph [bgcolor="transparent", ranksep="0.75", nodesep="0.35"];',
        'node [shape="box", style="rounded,filled", fontname="Arial", '
        'fontcolor="#E8EEF8", color="#3B82F6", fillcolor="#142A46", '
        'margin="0.15,0.10"];',
        'edge [color="#8294AE", penwidth="1.5", arrowsize="0.7"];',
    ]
    counter = [0]

    def add_node(node):
        node_id = f"node_{counter[0]}"
        counter[0] += 1
        label, color, fill = _node_appearance(node)
        safe_label = label.replace("\\", "\\\\").replace('"', '\\"')
        lines.append(
            f'{node_id} [label="{safe_label}", color="{color}", '
            f'fillcolor="{fill}"];'
        )

        for child in node["children"]:
            child_id = add_node(child)
            lines.append(f"{node_id} -> {child_id} [dir=back];")

        return node_id

    add_node(tree)
    lines.append("}")
    return "\n".join(lines)


def _node_appearance(node):
    operator = node["operator"]

    if operator == "table":
        alias = ""
        if node["alias"].casefold() != node["table"].casefold():
            alias = f"\\nAlias: {node['alias']}"
        return f"TABELA\\n{node['table']}{alias}", "#64748B", "#1E293B"

    if operator == "selection":
        return (
            f"SELEÇÃO  σ\\n{format_condition(node['condition'])}",
            "#22C55E",
            "#123524",
        )

    if operator == "projection":
        title = "PROJEÇÃO FINAL  π" if node.get("final") else "PROJEÇÃO  π"
        return (
            f"{title}\\n{format_columns(node['columns'])}",
            "#60A5FA",
            "#112D55",
        )

    return (
        f"JUNÇÃO  ⋈\\n{format_condition(node['condition'])}",
        "#F59E0B",
        "#3A2714",
    )


def _source_label(source):
    if source["alias"].casefold() == source["name"].casefold():
        return source["name"]
    return f"{source['name']} AS {source['alias']}"
