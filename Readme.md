# 🔎 ReconPy

ReconPy is an **OSINT-inspired website security scanner** written in Python.  
It helps security researchers and developers quickly assess a website’s basic security posture by checking:

- ✅ HTTP security headers  
- ✅ Password policy strength (baseline checks)  
- ✅ SSL/TLS certificate validity  
- ✅ JSON, CSV, or HTML report generation with a security score  

---

## 🚀 Features
- ASCII banner header for hacker‑tool vibe in Termux/Linux
- CLI arguments for flexible usage (`--report`, `--debug`)
- Logging with INFO/DEBUG levels
- Clean JSON/CSV/HTML reports with a simple security rating
- Modular design (`core/`, `utils/`, `tests/`) for easy extension

---

## 📦 Installation
Clone the repository and install dependencies:
```bash
git clone https://github.com/ChitranshShiv/ReconPy.git
cd ReconPy
pip install -r requirements.txt

