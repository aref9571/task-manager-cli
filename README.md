# Task Manager CLI

A command-line task manager written in Python. Tasks are saved to a JSON file, so they are still there the next time the program starts.

## Features

- Add tasks with a title and an optional description
- List tasks with their status (pending or complete)
- Mark tasks as complete and delete them
- Select a task by the first characters of its ID instead of typing the full UUID
- Input validation: empty titles and empty IDs are rejected
- Unit tests for the business logic with pytest

## Tech stack

- Python 3.13
- pytest
- JSON file storage

## Project structure

```text
task-manager-cli/
├── src/
│   ├── main.py        Command-line menu and input handling
│   ├── models.py      Task data class and JSON conversion
│   ├── services.py    TaskManager with the business logic
│   └── storage.py     Reading and writing data/tasks.json
├── tests/
│   └── test_manager.py
├── conftest.py        Adds src/ to the import path for the tests
└── requirements.txt
```

The code is split into layers: `main.py` only talks to the user, `TaskManager` holds the rules, and `StorageHandler` is the only part that touches the file system.

## Getting started

```bash
git clone https://github.com/aref9571/task-manager-cli.git
cd task-manager-cli
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Run the application from the repository root:

```bash
python src/main.py
```

Tasks are saved to `data/tasks.json`, which is created on first use and is not tracked by Git.

## Running tests

```bash
pytest
```

The tests cover adding a task, marking it complete and deleting it. GitHub Actions runs them on every push to `main`.

## Limitations

- Tasks cannot be edited or set back to pending from the menu.
- If the JSON file is damaged, the application starts with an empty list instead of reporting the problem.
