import json
import csv

def generate_report(results: dict, format: str = "json") -> None:
    """
    Generate a security report from scan results.

    Args:
        results (dict): The findings from all modules.
        format (str): Report format ("json" or "csv").
    """
    # Add a simple security score based on missing headers
    score = calculate_score(results)
    results["security_score"] = score

    if format == "json":
        with open("report.json", "w") as f:
            json.dump(results, f, indent=4)
    elif format == "csv":
        with open("report.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Section", "Findings"])
            for section, data in results.items():
                writer.writerow([section, data])


def calculate_score(results: dict) -> str:
    """
    Calculate a simple security score based on HTTP header findings.

    Args:
        results (dict): The findings from all modules.

    Returns:
        str: Security rating ("High", "Medium", "Low").
    """
    headers = results.get("http", {})
    if "error" in headers:
        return "Unknown"

    # Count missing headers
    missing = sum(1 for v in headers.values() if v == "missing")

    if missing == 0:
        return "High"
    elif missing <= 2:
        return "Medium"
    else:
        return "Low"
