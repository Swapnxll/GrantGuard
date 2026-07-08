from models.tool_models import ToolResult

MAX_GRANT = 2_000_000


def budget_tool(application: dict):

    amount = application["requested_amount"]

    return ToolResult(
        tool="budget",
        status="SUCCESS",
        success=True,
        reason="Budget evaluation completed.",
        data={
            "requested_amount": amount,
            "within_limit": amount <= MAX_GRANT,
            "max_limit": MAX_GRANT,
        },
    )