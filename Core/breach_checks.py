def check_breach(identifier: str) -> dict:
    # Placeholder: no API key required
    if "@" not in identifier and "." not in identifier:
        return {"error": "Invalid identifier"}
    return {"safe": True, "breaches": []}
