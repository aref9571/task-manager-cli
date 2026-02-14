# 📝 Professional Task Manager CLI

A robust, persistent command-line interface (CLI) application built with Python. This project demonstrates clean architecture, Object-Oriented Programming (OOP), and automated testing. It was developed as the final capstone for Month 1 of a Backend Engineering intensive.

## 🚀 Key Features
- **N-Tier Architecture:** Separated into Model (Data), Service (Logic), Storage (File I/O), and Presentation (CLI) layers.
- **Persistence:** All data is saved to and loaded from a `data/tasks.json` file automatically, ensuring your tasks survive app restarts.
- **Input Sanitization:** Handles empty inputs and provides a case-insensitive menu system.
- **Automated Testing:** Logic is fully verified with a Pytest suite to ensure stability during updates.
- **Developer Friendly:** Supports **UUID Snippets**. You only need to type the first few characters (e.g., `8fa1`) of a Task ID to mark it complete or delete it.

## 🛠️ Tech Stack
- **Language:** Python 3.13+
- **Testing:** Pytest
- **Data Format:** JSON
- **Version Control:** Git

## 📂 Project Structure
```text
task-manager-cli/
├── src/
│   ├── models.py      # Data blueprints (Task class)
│   ├── services.py    # Business logic (TaskManager)
│   ├── storage.py     # Data persistence (StorageHandler)
│   └── main.py        # CLI interactive loop
├── tests/
│   ├── __init__.py
│   └── test_manager.py # Automated unit tests
├── data/              # Folder for JSON storage (auto-generated)
├── conftest.py        # Pytest path configuration
├── requirements.txt   # Project dependencies
└── README.md          # Documentation