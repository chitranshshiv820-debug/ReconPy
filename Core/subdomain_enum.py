import requests

def enumerate_subdomains(domain: str, wordlist: list) -> list:
    found = []
    for sub in wordlist:
        subdomain = f"{sub}.{domain}"
        try:
            requests.get(f"http://{subdomain}", timeout=2)
            found.append(subdomain)
        except Exception:
            continue
    return found
