# ReconPy Usage Examples

## Basic Scan
Run a quick security scan on a target domain:
```bash
reconpy https://example.com --report json
#whois lookup
reconpy https://example.com --whois
#subdomains details 
reconpy https://example.com --subdomains wordlist.txt
#breach details 
reconpy test@example.com --breach

# report formats
reconpy https://example.com --report csv
reconpy https://example.com --report html

# help menu
reconpy --help
