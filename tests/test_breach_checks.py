# tests/test_breach.py

import unittest
from core import breach_check

class TestBreachCheck(unittest.TestCase):
    """
    Unit tests for the breach_check module.
    These tests cover safe identifiers, invalid inputs,
    and domain lookups.
    """

    def test_known_safe_email(self):
        """Safe email should return a dict with breaches or safe flag"""
        result = breach_check.check_breach("test@example.com")
        self.assertIsInstance(result, dict)
        self.assertTrue("breaches" in result or "safe" in result)

    def test_invalid_email(self):
        """Invalid email format should return an error"""
        result = breach_check.check_breach("notanemail")
        self.assertIsInstance(result, dict)
        self.assertIn("error", result)

    def test_domain_lookup(self):
        """Domain input should return breaches or safe flag"""
        result = breach_check.check_breach("example.com")
        self.assertIsInstance(result, dict)
        self.assertTrue("breaches" in result or "safe" in result)


if __name__ == "__main__":
    unittest.main()
