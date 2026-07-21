# Core Python Engineering: Data Pipelines, Parsing & Caching

A collection of foundational data engineering and infrastructure production tools built to practice core Python fundamentals, structured file handling, syntax manipulation, and data pipeline optimization techniques required in MLOps and LLM infrastructure.

## 📁 Repository Directory Structure

```text
core-python-fundamentals/
├── .gitignore
├── LICENSE
├── README.md
├── CLI expense tracker/
│   ├── CLI expense tracker.py
│   └── expenses.json
├── Log file parser/
│   ├── Log file parser.py
│   ├── generator.py
│   └── app.log
└── TTL system/
    └── TTL.py
```

---

## 🚀 Projects Overview

### 1. CLI Expense Tracker
*   **Directory**: `./CLI expense tracker`
*   **Purpose**: Manages and tracks data entries using structural JSON flat-file storage schemas.
*   **Core Concepts**: `argparse` CLI sub-commands, JSON serialization/deserialization, input token validation, and error recovery utilizing `.get()` dictionary operations.
*   **Execution**: `python "CLI expense tracker/CLI expense tracker.py" list`

### 2. Log File Parser & Analytics Utility
*   **Directory**: `./Log file parser`
*   **Purpose**: Processes unstructured server log text streams into structural tabular datasets to isolate operational metrics and event trends.
*   **Core Concepts**: Regular expressions (`re`), token regex pattern group matching, data aggregation, and anomaly frequency distribution tracking.
*   **Execution**: `python "Log file parser/Log file parser.py"`

### 3. TTL In-Memory Cache System
*   **Directory**: `./TTL system`
*   **Purpose**: Implements a high-performance key-value in-memory caching system with lazy Time-To-Live expiration policies mimicking basic Redis session architectures.
*   **Core Concepts**: Object-Oriented Programming (OOP), UNIX epoch data thresholds, lazy eviction memory pipelines, and state tracking.
*   **Execution**: `python "TTL system/TTL.py"`

---

## ⚙️ Engineering Principles Covered
*   **Defensive Code Architecture**: Preventing execution crashes by handling missing metadata gracefully and overriding empty files using error traps (`try-except`).
*   **Optimized Resource Processing**: Using clean object mappings, string normalization tokens, and fast lookup dictionary tracking profiles.
*   **Clean Repository Automation**: Maintaining clean directory files via strict tracking configurations (`.gitignore`) to block local editor settings (`.idea/`) from production deployment.

## 📦 Getting Started

### Installation
Clone this entire engineering ecosystem to your local system:
```bash
git clone https://github.com
cd core-python-fundamentals

```
Run any script directly using your local Python execution layout environment.
