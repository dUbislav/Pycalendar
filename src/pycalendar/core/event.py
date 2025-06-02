from datetime import datetime
from typing import List

from .notification import Notification


class Event:
    def __init__(self,
                 title: str,
                 start_time: datetime,
                 end_time: datetime,
                 description: str = "",
                 location: str = "",
                 notifications: List[Notification] = None):
        if end_time <= start_time:
            raise ValueError("End time must be after start time")
        self.title = title
        self.start_time = start_time
        self.end_time = end_time
        self.description = description
        self.location = location
        self.notifications = notifications or []

    def __str__(self):
        return f"{self.title} ({self.start_time.strftime('%Y-%m-%d %H:%M')} - {self.end_time.strftime('%H:%M')})"

    def __repr__(self):
        return f"<Event at {hex(id(self))}>"