import pytest
import os
# We import from src.services
from src.services import TaskManager

@pytest.fixture
def manager():
    test_db = "data/test_task.json"
    if os.path.exists(test_db):
        os.remove(test_db)

    # We ensure we are using the test database path
    m = TaskManager()
    from src.storage import StorageHandler
    m.storage = StorageHandler(test_db)
    m.tasks = []
    return m

def test_add_task(manager):
    # Fixed the title mismatch here
    task = manager.add_task(title="Test Task", description="Test Description")
    assert len(manager.list_all_tasks()) == 1
    assert task.title == "Test Task"

def test_mark_complete(manager):
    task = manager.add_task("Finish Testing")
    manager.mark_task_complete(task.id)
    assert task.completed is True

def test_delete_task(manager):
    task = manager.add_task("Delete Task")
    manager.delete_task(task.id)
    assert len(manager.list_all_tasks()) == 0