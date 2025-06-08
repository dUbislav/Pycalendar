from datetime import datetime, timedelta
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMessageBox

class Notification:
    def __init__(self, message, notify_time):
        self.message = message
        self.notify_time = notify_time

    def __str__(self):
        return f"Notification: '{self.message}' at {self.notify_time}"

    def __repr__(self):
        return f"<Notification at {hex(id(self))}>"


from datetime import datetime
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMessageBox

class NotificationManager:
    def __init__(self, calendar=None):
        self.calendar = calendar
        self.notifications = []  # Явная инициализация списка уведомлений
        self._timer = QTimer()
        self._timer.timeout.connect(self._check_events)
        self._timer.start(60000)  # 1 минута в реальном режиме

    def _check_events(self):
        """Проверяет текущие события и создает уведомления"""
        if not self.calendar:
            return

        now = datetime.now()
        # Используем get_events() с широким диапазоном
        for event in self.calendar.get_events(datetime.min, datetime.max):
            if event.start_time <= now <= event.end_time:
                self._add_notification(event)
    def _add_notification(self, event):
        """Добавляет новое уведомление"""
        notification = {
            'title': f"Событие: {event.title}",  # Изменено с event.name на event.title
            'message': f"Время: {event.start_time.strftime('%H:%M')}",
            'timestamp': datetime.now()
        }
        self.notifications.append(notification)
        self._show_notification(notification)

    def _show_notification(self, notification):
        """Отображает уведомление пользователю"""
        msg = QMessageBox()
        msg.setWindowTitle(notification['title'])
        msg.setText(notification['message'])
        msg.exec_()

    def stop(self):
        """Останавливает менеджер уведомлений"""
        self._timer.stop()