from models import Task

try:
    my_task = Task(title= "finish roadmap" , description="Complete day 1")
    print(f"Created Task: {my_task.title} (ID: {my_task.id})")

    print(f"Status: {'Done' if my_task.completed else 'pending'}")

    my_task.mark_complete()
    print(f"Status: {'Done' if my_task.completed else 'pending'}")

    data = my_task.to_dict()
    print(f"Serialized to dict: {data}")

    new_task = Task.from_dict(data)
    print(f"Recreated from dict: {new_task.title}")
except Exception as e:
    print(f"Error :{e}")
