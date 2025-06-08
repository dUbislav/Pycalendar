import pytest
from datetime import datetime, timedelta
from unittest.mock import patch

from PyQt5.QtWidgets import QMessageBox

from pycalendar.core.notification import NotificationManager
from pycalendar.core.calendar import Calendar
from pycalendar.core.event import Event


@pytest.fixture
def manager():
    """Фикстура для менеджера уведомлений"""
    return NotificationManager()


@pytest.fixture
def calendar_with_event():
    """Фикстура для календаря с событием"""
    cal = Calendar()
    start = datetime.now() - timedelta(minutes=5)  # Событие уже началось
    end = datetime.now() + timedelta(hours=1)
    cal.add_event(Event("Test Event", start, end))
    return cal


def test_notification_manager_initialization(manager):
    """Тест инициализации менеджера"""
    assert hasattr(manager, 'notifications')
    assert isinstance(manager.notifications, list)
    assert len(manager.notifications) == 0


def test_notification_creation_simple():
    """Простейший тест создания уведомления"""
    from pycalendar.core.notification import Notification

    # 1. Создаем тестовые данные
    test_message = "Test message"
    test_time = datetime.now()

    # 2. Создаем уведомление
    notification = Notification(test_message, test_time)

    # 3. Проверяем основные свойства
    assert notification.message == test_message
    assert notification.notify_time == test_time

    # 4. Проверяем строковое представление
    assert test_message in str(notification)
    assert "Notification" in repr(notification)



def test_empty_calendar_handling(manager):
    """Тест обработки пустого календаря"""
    manager._check_events()
    assert len(manager.notifications) == 0