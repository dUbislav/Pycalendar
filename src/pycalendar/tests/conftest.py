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