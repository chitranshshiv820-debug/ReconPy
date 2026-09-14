import requests

def scan_headers(url: str) -> dict:
    """
    Scan a website for important security-related HTTP headers.
    
    Args:
        url (str): The target website URL.
    
    Returns:
        dict: Findings about security headers.
    """
    findings = {}
    try:
        response = requests.get(url, timeout=5)
        headers = response.headers

        # Check for common security headers
        findings["Strict-Transport-Security"] = (
            "present" if "Strict-Transport-Security" in headers else "missing"
        )
        findings["Content-Security-Policy"] = (
            "present" if "Content-Security-Policy" in headers else "missing"
        )
        findings["X-Frame-Options"] = (
            "present" if "X-Frame-Options" in headers else "missing"
        )
        findings["X-Content-Type-Options"] = (
            "present" if "X-Content-Type-Options" in headers else "missing"
        )
        findings["Referrer-Policy"] = (
            "present" if "Referrer-Policy" in headers else "missing"
        )
        findings["Permissions-Policy"] = (
            "present" if "Permissions-Policy" in headers else "missing"
        )

    except Exception as e:
        findings["error"] = str(e)

    return findings
