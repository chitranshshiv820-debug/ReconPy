import pytest
from core import password_policy

def test_check_policy_returns_dict():
    """Policy check should return a dictionary with expected keys"""
    result = password_policy.check_policy("https://example.com")
    assert isinstance(result, dict)
    assert "min_length" in result
    assert "requires_special_chars" in result
    assert "requires_numbers" in result
    assert "requires_uppercase" in result

def test_validate_password_strong():
    """Strong password should pass all checks"""
    result = password_policy.validate_password("StrongPass123!")
    assert result["length_ok"]
    assert result["has_special_char"]
    assert result["has_number"]
    assert result["has_uppercase"]

def test_validate_password_weak():
    """Weak password should fail length check"""
    result = password_policy.validate_password("weak")
    assert isinstance(result, dict)
    assert not result["length_ok"]
