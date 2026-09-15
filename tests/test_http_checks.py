import pytest
from core import http_checks

def test_scan_headers_valid_site():
    """Scanning a valid site should return header info"""
    result = http_checks.scan_headers("https://example.com")
    assert isinstance(result, dict)
    assert "Strict-Transport-Security" in result

def test_scan_headers_invalid_site():
    """Scanning an invalid site should return an error"""
    result = http_checks.scan_headers("http://nonexistent.local")
    assert isinstance(result, dict)
    assert "error" in result

