# tests/test_subdomain.py

import unittest
from core import subdomain_enum

class TestSubdomainEnum(unittest.TestCase):
    """
    Unit tests for the subdomain enumeration module.
    Covers valid domains, invalid domains, and empty wordlists.
    """

    def test_valid_domain(self):
        """Valid domain should return a list with expected subdomains"""
        wordlist = ["www", "mail", "ftp"]
        result = subdomain_enum.enumerate_subdomains("example.com", wordlist)
        self.assertIsInstance(result, list)
        # Common subdomain 'www.example.com' should be detected
        self.assertIn("www.example.com", result)

    def test_invalid_domain(self):
        """Invalid domain should return an empty list gracefully"""
        wordlist = ["test", "demo"]
        result = subdomain_enum.enumerate_subdomains("notarealdomain.abcxyz", wordlist)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0)

    def test_empty_wordlist(self):
        """Empty wordlist should return an empty list"""
        result = subdomain_enum.enumerate_subdomains("example.com", [])
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0)


if __name__ == "__main__":
    unittest.main()

