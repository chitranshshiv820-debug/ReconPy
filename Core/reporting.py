import json
import csv

def generate_report(results: dict, format: str = "json") -> None:
    """
    Create a security report from scan results.
    Adds a simple score and saves the report
    either as JSON or CSV.
    """

    # Add a quick score based on header findings
    results["security_score"] = calculate_score(results)

    if format == "json":
        with open("report.json", "w") as file:
            json.dump(results, file, indent=4)

    elif format == "csv":
        with open("report.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Section", "Findings"])
            for section, data in results.items():
                writer.writerow([section, data])


def calculate_score(results: dict) -> str:
    """
    Work out a simple rating based on HTTP headers.
    Returns 'High', 'Medium', 'Low', or 'Unknown'.
    """

    headers = results.get("http", {})

    if "error" in headers:
        return "Unknown"

    # Count how many headers are missing
    missing_count = sum(1 for value in headers.values() if value == "missing")

    if missing_count == 0:
        return "High"
    elif missing_count <= 2:
        return "Medium"
    else:
        return "Low"
