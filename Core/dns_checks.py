import dns.resolver

def get_dns_records(domain: str) -> dict:
    records = {}
    try:
        for record_type in ["MX", "TXT", "NS"]:
            try:
                answers = dns.resolver.resolve(domain, record_type)
                records[record_type] = [str(r) for r in answers]
            except Exception:
                records[record_type] = []
        return records
    except Exception as e:
        return {"error": str(e)}
