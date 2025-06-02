from datetime import datetime


class Notification:
    def __init__(self, message, notify_time):  # Используем notify_time как в тесте
        self.message = message
        self.notify_time = notify_time  # Именно такое имя ожидает тест

    def __str__(self):
        return f"Notification: '{self.message}' at {self.notify_time}"

    def __repr__(self):
        return f"<Notification at {hex(id(self))}>"
class NotificationManager:
    def __init__(self):
        self.notifications = []
