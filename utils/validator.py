import re

def validate_url(url: str) -> str:
    """
    Validate that the provided string is a proper HTTP/HTTPS URL.

    Args:
        url (str): The target website URL.

    Returns:
        str: The validated URL.

    Raises:
        ValueError: If the URL is invalid.
    """
    pattern = re.compile(r"^(http|https)://[a-zA-Z0-9.-]+(:[0-9]+)?(/.*)?$")
    if not pattern.match(url):
        raise ValueError("URL must start with http:// or https:// and be properly formatted.")
    return url


def validate_email(email: str) -> str:
    """
    Validate that the provided string is a proper email address.

    Args:
        email (str): The email address to validate.

    Returns:
        str: The validated email.

    Raises:
        ValueError: If the email is invalid.
    """
    pattern = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")
    if not pattern.match(email):
        raise ValueError("Invalid email format.")
    return email


def sanitize_input(text: str) -> str:
    """
    Sanitize generic input to prevent injection or unsafe characters.

    Args:
        text (str): Input string.

    Returns:
        str: Sanitized string.
    """
    unsafe_chars = [';', '|', '&', '$', '>', '<', '"', "'", '`']
    for char in unsafe_chars:
        text = text.replace(char, "")
    return text.strip()
