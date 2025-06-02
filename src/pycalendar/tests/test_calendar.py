import pytest
from datetime import datetime, timedelta
from pycalendar.core.calendar import Calendar
from pycalendar.core.event import Event

@pytest.fixture
def sample_calendar():
    """Фикстура с тестовым календарём и одним событием"""
    cal = Calendar()
    now = datetime.now()
    cal.add_event(Event("Meeting", now + timedelta(hours=1), now + timedelta(hours=2)))
    return cal

def test_add_event():
    cal = Calendar()
    event = Event("Meeting", "2023-01-01 10:00", "2023-01-01 11:00")
    cal.add_event(event)
    assert len(cal._events) == 1

def test_event_conflict(sample_calendar):
    """Тест обнаружения конфликта событий"""
    with pytest.raises(ValueError, match="Event time conflict"):
        sample_calendar.add_event(Event("Conflict",
                                     datetime.now() + timedelta(minutes=30),
                                     datetime.now() + timedelta(hours=1, minutes=30)))

def test_get_events(sample_calendar):
    """Тест получения событий по диапазону дат"""
    now = datetime.now()
    events = sample_calendar.get_events(now, now + timedelta(days=1))
    assert len(events) == 1
    assert events[0].title == "Meeting"

def test_empty_calendar():
    cal = Calendar()
    assert len(cal.get_events(datetime.now(), datetime.now() + timedelta(days=1))) == 0

def test_calendar_str_representation():
    """Тест строкового представления календаря"""
    cal = Calendar()
    assert "Calendar" in str(cal)
    assert "events" in str(cal).lower()

def test_calendar_repr():
    cal = Calendar()
    assert repr(cal).startswith("<Calendar at")

def test_calendar_repr():
    cal = Calendar()
    assert repr(cal).startswith("<Calendar at 0x")