#!/usr/bin/env python3
"""
ReconPy - Website Security Scanner
----------------------------------
An OSINT-inspired tool for scanning websites for
security headers, password policies, and SSL/TLS details.
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
    """Print a stylish ASCII banner for ReconPy."""
    fonts = ["slant", "block", "banner3-D", "cyberlarge", "doom"]
    font = random.choice(fonts)
    banner = pyfiglet.figlet_format("ReconPy", font=font)
    tagline = "Website Security Scanner - OSINT Inspired"
    print(banner)
    print(tagline)
    print("-" * len(tagline))


def main():
    # Print banner
    print_banner()

    # Setup CLI arguments
    parser = argparse.ArgumentParser(description="ReconPy - Website Security Scanner")
    parser.add_argument("url", help="Target website URL")
    parser.add_argument("--report", choices=["json", "csv", "html"], default="json", help="Report format")
    parser.add_argument("--output", default="report", help="Output filename (without extension)")
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")
    args = parser.parse_args()

    # Validate URL
    try:
        target_url = validator.validate_url(args.url)
    except ValueError as e:
        print(f"[!] Invalid URL: {e}")
        return

    # Setup logger
    log = logger.get_logger()
    if args.debug:
        log.setLevel(logging.DEBUG)

    log.info(f"Starting security scan for {target_url}")

    # Run checks
    results = {}
    log.debug("Scanning HTTP headers...")
    results["http"] = check_http_headers(target_url)

    log.debug("Checking password policy...")
    results["password_policy"] = check_password_policy("ExamplePassword123!")

    log.debug("Checking SSL/TLS certificate...")
    results["encryption"] = check_ssl_certificate(target_url)

    # Generate report
    report_file = generate_report(results, format=args.report, filename=args.output)
    log.info(f"Scan complete. Report saved as {report_file}")


if __name__ == "__main__":
    main()
