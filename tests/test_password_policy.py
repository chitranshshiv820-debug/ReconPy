import pytest
from core import password_policy

def test_check_policy_returns_dict():
    result = password_policy.check_policy("https://example.com")
    assert isinstance(result, dict)
    assert "min_length" in result

def test_validate_password_strong():
    result = password_policy.validate_password("StrongPass123!")
    assert result["length_ok"]
    assert result["has_special_char"]
    assert result["has_number"]
    assert result["has_uppercase"]

def test_validate_password_weak():
    result = password_policy.validate_password("weak")
    assert not result["length_ok"]
