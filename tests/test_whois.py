# tests/test_whois.py

import unittest
from core import whois_lookup

class TestWhoisLookup(unittest.TestCase):
    def test_valid_domain(self):
        """Test WHOIS lookup for a valid domain"""
        result = whois_lookup.lookup_domain("example.com")
        self.assertIsInstance(result, dict)
        self.assertIn("domain_name", result)
        self.assertEqual(result["domain_name"].lower(), "example.com")

    def test_invalid_domain(self):
        """Test WHOIS lookup for an invalid domain"""
        result = whois_lookup.lookup_domain("notarealdomain.abcxyz")
        self.assertIsInstance(result, dict)
        self.assertIn("error", result)

    def test_empty_input(self):
        """Test WHOIS lookup with empty input"""
        result = whois_lookup.lookup_domain("")
        self.assertIsInstance(result, dict)
        self.assertIn("error", result)

if __name__ == "__main__":
    unittest.main()
