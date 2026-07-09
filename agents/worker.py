from tools.registration import registration_tool
from tools.budget import budget_tool
from tools.eligibility import eligibility_tool
from graph.state import GrantState
from models.tool_models import ToolResult


TOOLS = {
    "registration": registration_tool,
    "budget": budget_tool,
    "eligibility": eligibility_tool,
}


def worker_agent(state: GrantState):
    print("\n===== Worker Agent =====")
    application = state["application"]

    results = {}

    for step in state["plan"].steps:

        tool_name = step.tool

        if tool_name not in TOOLS:
            results[tool_name] = ToolResult(
                tool=tool_name,
                status="NOT_IMPLEMENTED",
                success=False,
                reason=f"{tool_name} tool has not been implemented yet.",
                data={}
            )
            continue

        tool = TOOLS[tool_name]

        results[tool_name] = tool(application)

    state["tool_results"] = results

    return state