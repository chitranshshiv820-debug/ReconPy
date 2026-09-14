# tests/test_subdomain.py

import unittest
from core import subdomain_enum

class TestSubdomainEnum(unittest.TestCase):
    def test_valid_domain(self):
        """Test subdomain enumeration for a valid domain"""
        wordlist = ["www", "mail", "ftp"]
        result = subdomain_enum.enumerate_subdomains("example.com", wordlist)
        self.assertIsInstance(result, list)
        # At least 'www.example.com' should be in the results
        self.assertIn("www.example.com", result)

    def test_invalid_domain(self):
        """Test subdomain enumeration for an invalid domain"""
        wordlist = ["test", "demo"]
        result = subdomain_enum.enumerate_subdomains("notarealdomain.abcxyz", wordlist)
        self.assertIsInstance(result, list)
        # Should return an empty list or handle gracefully
        self.assertEqual(len(result), 0)

    def test_empty_wordlist(self):
        """Test subdomain enumeration with empty wordlist"""
        result = subdomain_enum.enumerate_subdomains("example.com", [])
        self.assertIsInstance(result, list)
        # No subdomains should be found
        self.assertEqual(len(result), 0)

if __name__ == "__main__":
    unittest.main()
