from optimizer import generate_execution_plan, optimize_query
from relational_algebra import build_original_tree, tree_to_algebra
from sql_parser import parse_sql


def process_query(sql):
    """Executa todas as fases solicitadas para uma consulta SQL."""
    parsed_query = parse_sql(sql)
    original_tree = build_original_tree(parsed_query)
    optimized_tree, heuristics = optimize_query(parsed_query)

    return {
        "query": parsed_query,
        "original_tree": original_tree,
        "optimized_tree": optimized_tree,
        "original_algebra": tree_to_algebra(original_tree),
        "optimized_algebra": tree_to_algebra(optimized_tree),
        "heuristics": heuristics,
        "execution_plan": generate_execution_plan(optimized_tree),
    }
