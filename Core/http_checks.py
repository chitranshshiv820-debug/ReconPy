import requests

def scan_headers(url: str) -> dict:
    """
    Go through a website’s response and check if
    some well-known security headers are there.
    Returns a dictionary with each header marked
    as either 'present' or 'missing'.
    """

    output = {}

    try:
        response = requests.get(url, timeout=5)
        headers = response.headers

        # Check each header one by one
        if "Strict-Transport-Security" in headers:
            output["Strict-Transport-Security"] = "present"
        else:
            output["Strict-Transport-Security"] = "missing"

        if "Content-Security-Policy" in headers:
            output["Content-Security-Policy"] = "present"
        else:
            output["Content-Security-Policy"] = "missing"

        if "X-Frame-Options" in headers:
            output["X-Frame-Options"] = "present"
        else:
            output["X-Frame-Options"] = "missing"

        if "X-Content-Type-Options" in headers:
            output["X-Content-Type-Options"] = "present"
        else:
            output["X-Content-Type-Options"] = "missing"

        if "Referrer-Policy" in headers:
            output["Referrer-Policy"] = "present"
        else:
            output["Referrer-Policy"] = "missing"

        if "Permissions-Policy" in headers:
            output["Permissions-Policy"] = "present"
        else:
            output["Permissions-Policy"] = "missing"

    except Exception as error:
        output["error"] = str(error)

    return output
