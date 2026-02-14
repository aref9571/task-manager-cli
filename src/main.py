from services import TaskManager
import sys

def print_menu():
    print("\n--- 📝 PROFESSIONAL TASK MANAGER ---")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")
    print("-------------------------------------")

def main():
    manager = TaskManager()
    while True:
        print_menu()
        choice = input("Choose an action (1-5): ").strip().lower()

        if choice == "1":
            title = input("Enter the task title: ").strip()
            if title:
                descr = input("Enter the task description: ").strip()
                new_task = manager.add_task(title , descr)
                print(f"Task created: {new_task.title} (ID: {new_task.id[:8]})")
            else:
                print("Title cannot be empty!")

        elif choice == "2":
            all_tasks = manager.list_all_tasks()
            if not all_tasks:
                print("No task found.")
            else:
                print(f"You have {len(all_tasks)} tasks.")
                for t in all_tasks:
                    status = "Complete" if t.completed else "Pending"
                    print(f"[{t.id[:8]}] {t.title} - {status} ")

        elif choice == "3":
            task_id_snippet = input("Enter Task ID (first 8 chars is enough): ").strip()
            found = False
            for t in manager.list_all_tasks():
                if t.id.startswith(task_id_snippet):
                    manager.mark_task_complete(t.id)
                    print(f"Task '{t.title}' marked as complete!")
                    found =True
                    break
                if not found:
                    print("Task not found.")

        elif choice == "4":
            task_id_snippet = input("Enter Task ID (first 8 chars is enough): ").strip()
            found = False
            for t in manager.list_all_tasks():
                if t.id.startswith(task_id_snippet):
                    manager.delete_task(t.id)
                    print(f"Task '{t.title}' deleted successfully.")
                    found = True
                    break
                if not found:
                    print("Task not found.")

        elif choice == "5":
            print("Goodbye!")
            sys.exit(0)

        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()