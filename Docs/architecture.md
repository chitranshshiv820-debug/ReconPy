# ReconPy Architecture

## Overview
ReconPy is a modular OSINT-inspired security scanner written in Python.  
It analyzes websites for security issues, gathers domain intelligence, and generates structured reports.  
The design emphasizes modularity, so each feature lives in its own file under `core/`.

---

## Flowchart


---

## Utilities
- **utils/logger.py** → Centralized logging system  
- **utils/validators.py** → Input validation helpers  
- **utils/config.py** → Loads YAML/JSON config files  

---

## Tests
Each module has a corresponding test file in `tests/`:
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
2. Scanner orchestrates modules based on selected checks.  
3. Each module performs its analysis and returns results.  
4. Results are aggregated and passed to `reporting.py`.  
5. Reports are generated in JSON, CSV, or HTML format.  

---

## Design Principles
- **Modularity**: Each feature is isolated in its own file.  
- **Extensibility**: Easy to add new modules (e.g., Shodan API, Censys).  
- **Testability**: Every module has a unit test for reliability.  
- **Professional polish**: Config files, logging, and documentation make it production‑ready.  
