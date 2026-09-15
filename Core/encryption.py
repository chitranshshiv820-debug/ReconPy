import ssl
import socket
from datetime import datetime

def check_ssl(url: str) -> dict:
    """
    Look at the SSL/TLS certificate for a given site.
    Returns basic details like issuer, validity dates,
    and whether the certificate is valid right now.
    """

    details = {}

    try:
        # Pull out the hostname from the URL
        hostname = url.replace("https://", "").replace("http://", "").split("/")[0]

        # Set up a secure connection
        context = ssl.create_default_context()

        # Connect to the server on port 443
        with socket.create_connection((hostname, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as secure_sock:
                cert = secure_sock.getpeercert()

                # Issuer information
                issuer_info = dict(x[0] for x in cert.get("issuer", []))
                details["issuer"] = issuer_info.get("organizationName", "Unknown")

                # Validity period
                start_date = cert.get("notBefore")
                end_date = cert.get("notAfter")
                details["valid_from"] = start_date
                details["valid_to"] = end_date

                # Check if certificate is valid at this moment
                fmt = "%b %d %H:%M:%S %Y %Z"
                start = datetime.strptime(start_date, fmt)
                end = datetime.strptime(end_date, fmt)
                now = datetime.utcnow()
                details["is_valid_now"] = start <= now <= end

    except Exception as error:
        details["error"] = str(error)

    return details
