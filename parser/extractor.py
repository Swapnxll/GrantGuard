import re


def _search(pattern: str, text: str, default: str = "") -> str:
    match = re.search(pattern, text, re.IGNORECASE)
    return match.group(1).strip() if match else default


def _search_int(pattern: str, text: str, default: int = 0) -> int:
    value = _search(pattern, text)

    if not value:
        return default

    value = value.replace(",", "").replace("₹", "").strip()

    try:
        return int(value)
    except ValueError:
        return default


def extract_application(text: str) -> dict:
    """
    Extract structured information directly from PDF text.
    """

    return {
        "organization": _search(r"Organization Name:\s*(.*)", text),
        "registration_number": _search(r"Registration Number:\s*(.*)", text),
        "year_established": _search_int(r"Year Established:\s*(\d{4})", text),
        "years_operating": _search_int(r"Years Operating:\s*(\d+)", text),
        "contact_person": _search(r"Contact Person:\s*(.*)", text),
        "designation": _search(r"Designation:\s*(.*)", text),
        "email": _search(r"Email:\s*(.*)", text),
        "phone": _search(r"Phone:\s*(.*)", text),
        "project_title": _search(r"Project Title:\s*(.*)", text),
        "grant_category": _search(r"Grant Category:\s*(.*)", text),
        "requested_amount": _search_int(r"Requested Amount:\s*₹?\s*([\d,]+)", text),
        "project_description": _search(
            r"Project Description:\s*(.*?)(?:\n[A-Z][A-Za-z ]+:|\Z)",
            text,
        ),
        "beneficiaries": _search_int(r"Beneficiaries:\s*(\d+)", text),
        "timeline": _search(r"Timeline:\s*(.*)", text),
        "budget": {},
        "documents": [],
        "declaration_signed": "I declare" in text,
    }