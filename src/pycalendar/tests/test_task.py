from datetime import datetime, timedelta
from pycalendar.core.task import Task, Priority


def test_task_creation():
    """Тест создания задачи"""
    due = datetime.now() + timedelta(days=1)
    task = Task("Complete project", due, Priority.HIGH)

    assert task.title == "Complete project"
    assert task.due_date == due
    assert task.priority == Priority.HIGH
    assert not task.is_overdue()


def test_overdue_task():
    """Тест просроченной задачи"""
    past = datetime.now() - timedelta(days=1)
    task = Task("Overdue task", past)

    assert task.is_overdue()

    # Проверка завершенной задачи
    task.complete()
    assert not task.is_overdue()

def test_task_str():
    due = datetime.now() + timedelta(days=1)
    task = Task("Test task", due)
    assert "Test task" in str(task)
    assert str(due) in str(task)