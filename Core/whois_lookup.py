import socket

def lookup_domain(domain: str) -> dict:
    try:
        # Simple WHOIS query (works with some registries)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("whois.verisign-grs.com", 43))
        s.send((domain + "\r\n").encode())
        response = b""
        while True:
            data = s.recv(4096)
            if not data:
                break
            response += data
        s.close()
        return {"domain_name": domain, "raw": response.decode(errors="ignore")}
    except Exception as e:
        return {"error": str(e)}
