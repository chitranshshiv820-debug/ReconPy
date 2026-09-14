import pytest
from core import encryption

def test_check_ssl_valid_site():
    result = encryption.check_ssl("https://example.com")
    assert isinstance(result, dict)
    assert "issuer" in result or "error" in result

def test_check_ssl_invalid_site():
    result = encryption.check_ssl("http://nonexistent.local")
    assert "error" in result
