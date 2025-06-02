from datetime import datetime, timedelta

import pytest

from src.pycalendar.core.event import Event


def test_event_creation():
    """Тест создания события"""
    start = datetime.now()
    end = start + timedelta(hours=1)
    event = Event("Test Event", start, end, "Description", "Location")

    assert event.title == "Test Event"
    assert event.start_time == start
    assert event.end_time == end
    assert event.description == "Description"
    assert event.location == "Location"


def test_invalid_event_times():
    """Тест на неправильные временные рамки"""
    start = datetime.now()
    end = start - timedelta(hours=1)  # Конец раньше начала

    with pytest.raises(ValueError, match="End time must be after start time"):
        Event("Invalid", start, end)


def test_event_str_representation():
    """Тест строкового представления"""
    start = datetime(2023, 1, 1, 10, 0)
    end = datetime(2023, 1, 1, 11, 0)
    event = Event("Test", start, end)

    assert str(event) == "Test (2023-01-01 10:00 - 11:00)"

@pytest.mark.parametrize("hours,expected", [(23, True), (25, False)])
def test_event_within_day(hours, expected):
    """Проверяет, укладывается ли событие в 24 часа"""
    start = datetime.now()
    end = start + timedelta(hours=hours)
    duration = (end - start).total_seconds()
    assert (duration < 86400) == expected  # 86400 секунд = 24 часа

def test_event_repr():
    start = datetime.now()
    end = start + timedelta(hours=1)
    event = Event("Test", start, end)
    assert repr(event).startswith("<Event at 0x")