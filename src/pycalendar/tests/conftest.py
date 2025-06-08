from unittest.mock import patch

import pytest
from datetime import datetime, timedelta
from pycalendar.core import Calendar, Event, Notification

@pytest.fixture
def sample_event():
    now = datetime.now()
    return Event("Test Event", now, now + timedelta(hours=1))

@pytest.fixture
def sample_notification():
    return Notification("Test", datetime.now() + timedelta(minutes=15))

@pytest.fixture
def calendar_with_event():
    cal = Calendar()
    start = datetime.now() + timedelta(minutes=5)
    end = start + timedelta(hours=1)
    cal.add_event(Event("Test Event", start, end))
    return cal
@pytest.fixture
def calendar_with_event():
    """Фикстура для календаря с событием"""
    cal = Calendar()
    start = datetime.now() - timedelta(minutes=5)  # Событие уже началось
    end = datetime.now() + timedelta(hours=1)
    cal.add_event(Event("Test Event", start, end))
    return cal
@pytest.fixture(autouse=True)
def mock_qt_timer():
    """Фикстура для мокинга Qt таймеров"""
    with patch('PyQt5.QtCore.QTimer.start'):
        yield