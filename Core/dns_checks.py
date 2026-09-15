import dns.resolver

def get_dns_records(domain: str) -> dict:
    """
    Try to fetch some basic DNS records (MX, TXT, NS) for a given domain.
    Returns a dictionary with record types as keys.
    If something goes wrong, an error message is returned instead.
    """

    results = {}

    try:
        for record_type in ["MX", "TXT", "NS"]:
            try:
                answers = dns.resolver.resolve(domain, record_type)
                results[record_type] = [str(item) for item in answers]
            except Exception:
                # If this record type fails, just store an empty list
                results[record_type] = []
        return results
    except Exception as error:
        return {
            "error": str(error)
        }

