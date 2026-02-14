from services import StorageHandler, TaskManager
import os

def test_persistence():
    print("Testing persistence...")
    manager = TaskManager()

    current_tasks = manager.list_all_tasks()
    print("Current Tasks in DB: {}".format(len(current_tasks)))
    for task in current_tasks:
        print(f"{task.title} {'Done' if task.completed else 'Pending'} ")

    new_task = manager.add_task("Persistence Task" , "I survive restarts")
    print(f"ADDED: {new_task.title}")

    manager.mark_task_complete(new_task.id)
    if os.path.exists("data/tasks.json"):
        print("Success: data/tasks.json exists!")
    else:
        print("FAILURE: file not found")



if __name__ == "__main__":
    test_persistence()

