import pytest
from datetime import datetime, timedelta
from pycalendar.core.notification import Notification, NotificationManager


def test_notification_creation():
    """Тест создания уведомления"""
    time = datetime.now() + timedelta(minutes=30)
    notif = Notification("Test message", time)
    assert notif.message == "Test message"
    assert notif.notify_time == time


def test_notification_manager():
    """Тест менеджера уведомлений"""
    manager = NotificationManager()
    time = datetime.now() + timedelta(minutes=15)

    # Проверка пустого менеджера
    assert len(manager.notifications) == 0

    # Добавление уведомления
    notif = Notification("Test", time)
    manager.notifications.append(notif)
    assert len(manager.notifications) == 1
    assert manager.notifications[0].message == "Test"


def test_notification_str_representation():
    time = datetime.now() + timedelta(minutes=30)
    notif = Notification("Test message", time)
    assert str(notif) == f"Notification: 'Test message' at {time}"

def test_notification_repr():
    time = datetime.now()
    notif = Notification("Test", time)
    assert repr(notif).startswith("<Notification at 0x")