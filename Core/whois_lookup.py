import socket

def lookup_domain(domain: str) -> dict:
    """
    Perform a basic WHOIS lookup for a domain.
    Connects to the Verisign WHOIS server and returns raw data.
    """

    try:
        # Open a socket connection to the WHOIS server
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(("whois.verisign-grs.com", 43))

        # Send the domain name query
        sock.send((domain + "\r\n").encode())

        response = b""
        while True:
            data = sock.recv(4096)
            if not data:
                break
            response += data

        sock.close()

        return {
            "domain_name": domain,
            "raw": response.decode(errors="ignore")
        }

    except Exception as error:
        return {
            "error": str(error)
        }

