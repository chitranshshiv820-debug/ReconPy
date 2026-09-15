import re

def validate_url(url: str) -> str:
    """Check if the string looks like a valid HTTP/HTTPS URL."""
    pattern = r"^(http|https)://[a-zA-Z0-9.-]+(:[0-9]+)?(/.*)?$"
    if not re.match(pattern, url):
        raise ValueError("Invalid URL. Must start with http:// or https://")
    return url


def validate_email(email: str) -> str:
    """Check if the string looks like a valid email address."""
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(pattern, email):
        raise ValueError("Invalid email format")
    return email


def sanitize_input(text: str) -> str:
    """Remove unsafe characters from input."""
    unsafe_chars = [';', '|', '&', '$', '>', '<', '"', "'", '`']
    for ch in unsafe_chars:
        text = text.replace(ch, "")
    return text.strip()
