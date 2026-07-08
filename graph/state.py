from typing_extensions import TypedDict

class GrantState(TypedDict):
    application: dict

    plan: str

    worker_result: str

    final_decision: str