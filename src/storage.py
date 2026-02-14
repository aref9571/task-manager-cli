import json
import os
from typing import List
from models import Task

class StorageHandler:

    def __init__(self , file_path: str = "data/tasks.json"):

        self.file_path = file_path
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

    def save_tasks(self , tasks : List[Task]) -> None:

        data_to_save = [task.to_dict() for task in tasks]
        with open(self.file_path , 'w' , encoding='utf-8') as f:
            json.dump(data_to_save , f , indent=4)

    def load_tasks(self) -> List[Task]:

        if not os.path.exists(self.file_path):
            return []

        try:
            with open(self.file_path , 'r' , encoding= 'utf-8') as f:
                data = json.load(f)
                return [Task.from_dict(item) for item in data]
        except(json.JSONDecodeError , KeyError) as e:
            return []

