import uuid
from dataclasses import dataclass , field
from datetime import datetime
from typing import Optional

@dataclass
class Task:
    title : str
    description : str
    id : str = field(default_factory=lambda : str(uuid.uuid4()))
    completed : bool = False
    created_at : str = field(default_factory=lambda : datetime.now().isoformat())

    def mark_complete(self) -> None:
        self.completed = True

    def mark_pending(self) -> None:
        self.completed = False

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "description" : self.description,
            "completed" : self.completed,
            "created_at" : self.created_at
        }
    @classmethod
    def from_dict(cls , data:dict) -> 'Task':
        return cls(
            id = data["id"],
            title = data["title"],
            description=data["description"],
            completed=data["completed"],
            created_at=data["created_at"]
        )