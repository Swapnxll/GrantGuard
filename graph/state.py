from typing_extensions import TypedDict


class GrantState(TypedDict):
    # Original application
    application: dict

    # Planner output
    plan: str

    # Worker output
    worker_result: str

    # Final decision
    final_decision: str

# Why not use a Python class?

# Because LangGraph expects a serializable state.

# A TypedDict gives us:

# lightweight state
# type hints
# compatibility with LangGraph
# easy debugging

# Later, we may switch to a Pydantic state if we want stricter validation, but TypedDict is the standard starting point.