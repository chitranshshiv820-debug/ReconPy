import ssl
import socket
from datetime import datetime

def check_ssl(url: str) -> dict:
    """
    Check SSL/TLS certificate details for a given website.

    Args:
        url (str): The target website URL.

    Returns:
        dict: Certificate details including issuer and validity period.
    """
    findings = {}
    try:
        # Extract hostname from URL
        hostname = url.replace("https://", "").replace("http://", "").split("/")[0]

        # Create SSL context
        context = ssl.create_default_context()

        # Connect to server on port 443
        with socket.create_connection((hostname, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()

                # Extract issuer
                issuer = dict(x[0] for x in cert.get("issuer", []))
                findings["issuer"] = issuer.get("organizationName", "Unknown")

                # Extract validity dates
                valid_from = cert.get("notBefore")
                valid_to = cert.get("notAfter")

                findings["valid_from"] = valid_from
                findings["valid_to"] = valid_to

                # Check if certificate is currently valid
                fmt = "%b %d %H:%M:%S %Y %Z"
                start = datetime.strptime(valid_from, fmt)
                end = datetime.strptime(valid_to, fmt)
                now = datetime.utcnow()

                findings["is_valid_now"] = start <= now <= end

    except Exception as e:
        findings["error"] = str(e)

    return findings
