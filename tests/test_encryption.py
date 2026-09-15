import pytest
from core import encryption

def test_check_ssl_valid_site():
    """SSL check on a valid site should return issuer or error info"""
    result = encryption.check_ssl("https://example.com")
    assert isinstance(result, dict)
    assert "issuer" in result or "error" in result

def test_check_ssl_invalid_site():
    """SSL check on an invalid site should return an error"""
    result = encryption.check_ssl("http://nonexistent.local")
    assert isinstance(result, dict)
    assert "error" in result

