import traceback

from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout,
                             QCalendarWidget, QListWidget, QPushButton,
                             QLineEdit, QTimeEdit, QMessageBox, QHBoxLayout, QLabel)
from PyQt5.QtCore import QDate, QTime, QTimer
from datetime import datetime, timedelta
from pycalendar.core.calendar import Calendar
from pycalendar.core.event import Event


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.calendar = Calendar()
        self.init_ui()
        self.init_notifications()

    def init_ui(self):
        """Инициализация пользовательского интерфейса"""
        self.setWindowTitle('PyCalendar')
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Виджет календаря
        self.calendar_widget = QCalendarWidget()
        layout.addWidget(self.calendar_widget)

        # Список событий
        self.event_list = QListWidget()
        layout.addWidget(self.event_list)

        # Форма создания события
        self.title_input = QLineEdit(placeholderText="Event Title")
        layout.addWidget(self.title_input)

        # Время начала и окончания
        time_layout = QHBoxLayout()
        self.start_time = QTimeEdit(time=QTime(9, 0))
        self.end_time = QTimeEdit(time=QTime(10, 0))
        time_layout.addWidget(QLabel("Start:"))
        time_layout.addWidget(self.start_time)
        time_layout.addWidget(QLabel("End:"))
        time_layout.addWidget(self.end_time)
        layout.addLayout(time_layout)

        # Кнопка добавления
        self.add_button = QPushButton("Add Event")
        self.add_button.clicked.connect(self.add_event)
        layout.addWidget(self.add_button)

        # Обновление списка событий при изменении даты
        self.calendar_widget.selectionChanged.connect(self.update_events)
        self.update_events()  # Первоначальное обновление

    def add_event(self):
        try:
            # Получаем и проверяем название
            title = self.title_input.text().strip()
            if not title:
                raise ValueError("Please enter event title")

            # Получаем дату и время
            date = self.calendar_widget.selectedDate()
            start_time = self.start_time.time()
            end_time = self.end_time.time()

            # Проверяем время
            if start_time >= end_time:
                raise ValueError("End time must be after start time")

            # Создаем datetime объекты
            start = datetime.combine(date.toPyDate(), start_time.toPyTime())
            end = datetime.combine(date.toPyDate(), end_time.toPyTime())

            # Создаем и добавляем событие
            event = Event(title, start, end)
            self.calendar.add_event(event)

            # Обновляем интерфейс
            self.update_events()
            self.title_input.clear()

            QMessageBox.information(self, "Success", "Event added successfully")

        except ValueError as e:
            QMessageBox.warning(self, "Input Error", str(e))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to add event: {str(e)}")
            print(f"Error adding event: {traceback.format_exc()}")

    def update_events(self):
        """Обновление списка событий для выбранной даты"""
        self.event_list.clear()
        date = self.calendar_widget.selectedDate()
        start = datetime.combine(date.toPyDate(), datetime.min.time())
        end = datetime.combine(date.toPyDate(), datetime.max.time())

        for event in self.calendar.get_events(start, end):
            self.event_list.addItem(
                f"{event.title} ({event.start_time.strftime('%H:%M')}-{event.end_time.strftime('%H:%M')})"
            )

    def init_notifications(self):
        """Инициализация системы уведомлений"""
        self.notification_timer = QTimer()
        self.notification_timer.timeout.connect(self.check_upcoming_events)
        self.notification_timer.start(60000)  # Проверка каждую минуту

    def check_upcoming_events(self):
        """Проверка предстоящих событий"""
        now = datetime.now()
        upcoming_threshold = now + timedelta(minutes=15)

        # Получаем все события из календаря
        all_events = self.calendar.get_events(
            start=datetime.min,
            end=datetime.max
        )

        for event in all_events:
            # Уведомление о скором начале
            if now <= event.start_time <= upcoming_threshold:
                self.show_notification(
                    "Скоро событие",
                    f"{event.title}\nНачнется в {event.start_time.strftime('%H:%M')}"
                )
            # Уведомление о текущем событии
            elif event.start_time <= now <= event.end_time:
                self.show_notification(
                    "Текущее событие",
                    f"{event.title}\nИдет до {event.end_time.strftime('%H:%M')}"
                )

    def show_notification(self, title, message):
        """Показ уведомления"""
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()