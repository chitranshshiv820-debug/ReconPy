import requests

def enumerate_subdomains(domain: str, wordlist: list) -> list:
    """
    Try each word in the list as a possible subdomain.
    If the subdomain responds, add it to the results.
    """

    found_subdomains = []

    for word in wordlist:
        subdomain = f"{word}.{domain}"
        try:
            requests.get(f"http://{subdomain}", timeout=2)
            found_subdomains.append(subdomain)
        except Exception:
            # If it fails, just skip to the next one
            continue

    return found_subdomains

