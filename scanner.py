#!/usr/bin/env python3
"""
ReconPy - Website Security Scanner
----------------------------------
A simple OSINT-inspired tool to scan websites for:
- Security headers
- Password policy checks
- SSL/TLS certificate details
"""

import argparse
import random
import logging
import pyfiglet

from core.http_checks import check_http_headers
from core.password_policy import check_password_policy
from core.encryption import check_ssl_certificate
from core.reporting import generate_report
from utils import logger, validator


def print_banner():
    """Print ASCII banner with a random font."""
    fonts = ["slant", "block", "banner3-D", "cyberlarge", "doom"]
    banner = pyfiglet.figlet_format("ReconPy", font=random.choice(fonts))
    tagline = "Website Security Scanner - OSINT Inspired"
    print(banner)
    print(tagline)
    print("-" * len(tagline))


def main():
    print_banner()

    # CLI arguments
    parser = argparse.ArgumentParser(description="ReconPy - Website Security Scanner")
    parser.add_argument("url", help="Target website URL")
    parser.add_argument("--report", choices=["json", "csv", "html"], default="json", help="Report format")
    parser.add_argument("--output", default="report", help="Output filename (without extension)")
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")
    args = parser.parse_args()

    # Validate URL
    try:
        target_url = validator.validate_url(args.url)
    except ValueError as err:
        print(f"[!] Invalid URL: {err}")
        return

    # Logger setup
    log = logger.get_logger(level=logging.DEBUG if args.debug else logging.INFO)
    log.info(f"Scanning {target_url}...")

    # Run checks
    results = {
        "http": check_http_headers(target_url),
        "password_policy": check_password_policy("ExamplePassword123!"),
        "encryption": check_ssl_certificate(target_url),
    }

    # Report
    report_file = generate_report(results, format=args.report, filename=args.output)
    log.info(f"Scan complete. Report saved as {report_file}")


if __name__ == "__main__":
    main()
