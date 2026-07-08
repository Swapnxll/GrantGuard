from models.tool_models import ToolResult

def registration_tool(application: dict):

    valid = application["registration_valid"]

    return ToolResult(
        tool="registration",
        status="SUCCESS",
        success=True,
        reason="Registration verification completed.",
        data={
            "valid": valid,
            "message": "Registration is valid." if valid else "Registration is invalid.",
        },
    )