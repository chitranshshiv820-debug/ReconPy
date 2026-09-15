# ReconPy Architecture

## Overview
ReconPy is a modular security scanner inspired by OSINT techniques, built in Python.  
It checks websites for common security issues, gathers domain intelligence, and produces structured reports.  
The design is intentionally modular: each feature lives in its own file under `core/`, making it easy to extend or maintain.

---

## Flowchart
*(to be added later – shows how modules connect and data flows through the system)*

---

## Utilities
- **utils/logger.py** → Handles all logging in one place  
- **utils/validators.py** → Provides input validation helpers  
- **utils/config.py** → Loads configuration from YAML or JSON files  

---

## Tests
Every module has a matching test file in `tests/` to ensure reliability:
- `test_http.py`  
- `test_password.py`  
- `test_encryption.py`  
- `test_whois.py`  
- `test_dns.py`  
- `test_subdomain.py`  
- `test_breach.py`  

---

## Data Flow
1. User runs `scanner.py` with CLI arguments.  
2. The scanner decides which modules to run based on those arguments.  
3. Each module performs its own analysis and returns results.  
4. Results are collected and passed into `reporting.py`.  
5. Reports are generated in JSON, CSV, or HTML format.  

---

## Design Principles
- **Modularity**