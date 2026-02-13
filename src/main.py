from services import TaskManager

def test_service():
    print("Testing TaskManager Service...")
    manager = TaskManager()

    task_1 = manager.add_task(title = "finish day 2" , description= "Implement the service layer")
    print(f"Added: {task_1.title} | ID: {task_1.id}")

    all_tasks = manager.list_all_tasks()
    print(f"Total tasks: {len(all_tasks)}")

    success = manager.mark_task_complete(task_1.id)
    if success:
        print(f"Task status: {'Complete' if task_1.completed else 'Pending'}")

    manager.delete_task(task_1.id)
    print(f"Tasks after deletion: {len(manager.list_all_tasks())}")

if __name__ == "__main__":
    test_service()


