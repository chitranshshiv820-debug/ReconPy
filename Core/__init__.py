# core/__init__.py
"""
Expose key scanning modules for easy import.
This allows you to do: from core import check_http_headers, check_password_policy, etc.
"""

from .http_checks import check_http_headers
from .password_policy import check_password_policy
from .encryption import check_ssl_certificate
from .reporting import generate_report
from .whois_lookup import lookup_domain
from .dns_checks import get_dns_records
from .subdomain_enum import enumerate_subdomains
from .breach_check import check_breach

__all__ = [
    "check_http_headers",
    "check_password_policy",
    "check_ssl_certificate",
    "generate_report",
    "lookup_domain",
    "get_dns_records",
    "enumerate_subdomains",
    "check_breach",
]
