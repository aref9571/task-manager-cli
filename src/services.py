from typing import List , Optional
from models import Task
from storage import StorageHandler


class TaskManager:


    def __init__(self):
        self.storage = StorageHandler()
        self.tasks: List[Task] = self.storage.load_tasks()

    def _save(self):
        self.storage.save_tasks(self.tasks)

    def add_task(self , title: str , description: str = ""):
        new_task = Task(title = title , description=description)
        self.tasks.append(new_task)
        self._save()
        return new_task

    def list_all_tasks(self) -> List[Task]:
        return self.tasks

    def find_task_by_id(self , task_id : str) -> Optional[Task]:
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def delete_task(self , task_id: str) -> bool:
        initial_length = len(self.tasks)
        self.tasks = [t for t in self.tasks if t.id != task_id ]
        self._save()
        return len(self.tasks) < initial_length

    def mark_task_complete(self , task_id: str ) -> bool:
        task = self.find_task_by_id(task_id)
        if task:
            task.mark_complete()
            self._save()
            return True
        return False



