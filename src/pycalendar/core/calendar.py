from datetime import datetime
from typing import List

import timedelta

from .event import Event

class Calendar:
    def __init__(self):
        self._events: List[Event] = []

    def add_event(self, event: Event) -> None:
        if self._check_event_conflict(event):
            raise ValueError("Event time conflict")
        self._events.append(event)
        self._events.sort(key=lambda x: x.start_time)

    def get_events(self, start: datetime, end: datetime) -> List[Event]:
        return [e for e in self._events if start <= e.start_time <= end]

    def _check_event_conflict(self, new_event: Event) -> bool:
        return any(
            existing.start_time < new_event.end_time and
            new_event.start_time < existing.end_time
            for existing in self._events
        )
    def __str__(self):
        return f"Calendar with {len(self._events)} events"

    def __repr__(self):
        return f"<Calendar at {hex(id(self))}>"

    def get_upcoming_events(self, minutes=15):
        """Возвращает события, которые начнутся в ближайшие N минут"""
        now = datetime.now()
        time_threshold = now + timedelta(minutes=minutes)
        return [
            event for event in self._events  # Исправлено на self._events
            if now <= event.start_time <= time_threshold
        ]
