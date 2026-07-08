from models.tool_models import ToolResult


def eligibility_tool(application: dict):

    eligible = (
        application["beneficiaries"] >= 100
        and application["timeline"] == "12 months"
    )

    return ToolResult(
        tool="eligibility",
        status="SUCCESS",
        success=True,
        reason="Eligibility evaluation completed.",
        data={
            "eligible": eligible,
            "beneficiaries": application["beneficiaries"],
            "timeline": application["timeline"],
        },
    )