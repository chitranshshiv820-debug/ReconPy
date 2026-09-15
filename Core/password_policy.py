import re

def check_policy(url: str) -> dict:
    """
    Placeholder function to describe a site's password policy.
    In reality, this would require checking signup forms or documentation,
    but here we just assume a strong default policy.
    """

    policy = {
        "min_length": 8,
        "requires_special_chars": True,
        "requires_numbers": True,
        "requires_uppercase": True
    }

    return policy


def validate_password(password: str) -> dict:
    """
    Test a password against a simple strong policy.
    Returns a dictionary showing which rules are met.
    """

    checks = {
        "length_ok": len(password) >= 8,
        "has_special_char": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)),
        "has_number": bool(re.search(r"\d", password)),
        "has_uppercase": bool(re.search(r"[A-Z]", password))
    }

    return checks
