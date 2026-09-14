import pytest
from core import http_checks

def test_scan_headers_valid_site():
    result = http_checks.scan_headers("https://example.com")
    assert isinstance(result, dict)
    assert "Strict-Transport-Security" in result

def test_scan_headers_invalid_site():
    result = http_checks.scan_headers("http://nonexistent.local")
    assert "error" in result
