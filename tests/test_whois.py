# tests/test_whois.py

import unittest
from core import whois_lookup

class TestWhoisLookup(unittest.TestCase):
    """
    Tests for the WHOIS lookup function.
    Covers normal domains, bad domains, and empty input.
    """

    def test_valid_domain(self):
        """A real domain should return its name in the result"""
        result = whois_lookup.lookup_domain("example.com")
        self.assertIsInstance(result, dict)
        self.assertIn("domain_name", result)
        self.assertEqual(result["domain_name"].lower(), "example.com")

    def test_invalid_domain(self):
        """A fake domain should give back an error"""
        result = whois_lookup.lookup_domain("notarealdomain.abcxyz")
        self.assertIsInstance(result, dict)
        self.assertIn("error", result)

    def test_empty_input(self):
        """Empty input should also give back an error"""
        result = whois_lookup.lookup_domain("")
        self.assertIsInstance(result, dict)
        self.assertIn("error", result)


if __name__ == "__main__":
    unittest.main()
