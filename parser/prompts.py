EXTRACTION_PROMPT = """
You are an information extraction system.

Extract the application.

Return JSON in this format:

{{
    "organization": "",
    "registration_number": "",
    "year_established": 0,
    "years_operating": 0,

    "contact_person": "",
    "designation": "",

    "email": "",
    "phone": "",

    "project_title": "",
    "grant_category": "",

    "requested_amount": 0,

    "project_description": "",

    "beneficiaries": 0,

    "timeline": "",

    "budget": {{}},

    "documents": [],

    "declaration_signed": false
}}

Document:

{document}
"""