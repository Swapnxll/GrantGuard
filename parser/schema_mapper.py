# JSON → GrantApplication dictionary

def map_to_application_schema(extracted: dict) -> dict:
    """
    Convert Gemini extraction into the canonical
    GrantGuard application schema.
    """

    return {

        "organization":
            extracted.get("organization"),

        "registration_number":
            extracted.get("registration_number"),

        "year_established":
            extracted.get("year_established"),

        "years_operating":
            extracted.get("years_operating"),

        "contact_person":
            extracted.get("contact_person"),

        "designation":
            extracted.get("designation"),

        "email":
            extracted.get("email"),

        "phone":
            extracted.get("phone"),

        "project_title":
            extracted.get("project_title"),

        "grant_category":
            extracted.get("grant_category"),

        "requested_amount":
            extracted.get("requested_amount", 0),

        "project_description":
            extracted.get("project_description", ""),

        "beneficiaries":
            extracted.get("beneficiaries", 0),

        "timeline":
            extracted.get("timeline", ""),

        "budget":
            extracted.get("budget", {}),

        "documents":
            extracted.get("documents", []),

        "declaration_signed":
            extracted.get("declaration_signed", False),
    }