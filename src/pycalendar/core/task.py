from datetime import datetime
from enum import Enum

class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

class Task:
    def __init__(self, title, due_date, priority=Priority.MEDIUM):  # Изменяем name на title
        self.title = title  # Соответствуем тесту
        self.due_date = due_date
        self.priority = priority
        self._completed = False

    def is_overdue(self):
        return datetime.now() > self.due_date and not self._completed

    def __str__(self):
        return f"Task: {self.title} (Due: {self.due_date})"

    def __repr__(self):
        return f"<Task '{self.title}' at {hex(id(self))}>"

    def complete(self):
        """Пометить задачу как выполненную"""
        self._completed = True



