# 🔎 ReconPy

ReconPy is a small Python tool inspired by OSINT techniques.  
It helps check a website’s basic security posture by looking at things like:

- HTTP security headers  
- Password policy strength (basic checks)  
- SSL/TLS certificate validity  
- Report generation (JSON, CSV, HTML) with a simple score  

---

## 🚀 Features
- ASCII banner for that hacker‑tool vibe (works in Termux/Linux)
- CLI arguments for flexible usage (`--report`, `--debug`)
- Logging with INFO/DEBUG levels
- Clean reports in JSON/CSV/HTML
- Modular design (`core/`, `utils/`, `tests/`) so it’s easy to extend

---

## 📦 Installation
Clone the repo and install dependencies:

```bash
git clone https://github.com/chitranshshiv820-debug/ReconPy.git
cd ReconPy
pip install -r requirements.txt


