from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout,
                             QCalendarWidget, QListWidget, QPushButton,
                             QLineEdit, QTimeEdit, QLabel, QMessageBox, QHBoxLayout)
from PyQt5.QtCore import QDate, QTime
from datetime import datetime
from pycalendar.core.calendar import Calendar
from pycalendar.core.event import Event
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.calendar = Calendar()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('PyCalendar')
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Calendar Widget
        self.calendar_widget = QCalendarWidget()
        layout.addWidget(self.calendar_widget)

        # Event List
        self.event_list = QListWidget()
        layout.addWidget(self.event_list)

        # Event Creation
        self.title_input = QLineEdit(placeholderText="Event Title")
        layout.addWidget(self.title_input)

        time_layout = QHBoxLayout()
        self.start_time = QTimeEdit(time=QTime(9, 0))
        self.end_time = QTimeEdit(time=QTime(10, 0))
        time_layout.addWidget(self.start_time)
        time_layout.addWidget(self.end_time)
        layout.addLayout(time_layout)

        self.add_button = QPushButton("Add Event")
        self.add_button.clicked.connect(self.add_event)
        layout.addWidget(self.add_button)

        # Connect signals
        self.calendar_widget.selectionChanged.connect(self.update_events)

    def add_event(self):
        try:
            title = self.title_input.text()
            if not title:
                raise ValueError("Event title cannot be empty")

            date = self.calendar_widget.selectedDate()
            start = datetime.combine(
                date.toPyDate(),
                self.start_time.time().toPyTime()
            )
            end = datetime.combine(
                date.toPyDate(),
                self.end_time.time().toPyTime()
            )

            event = Event(title, start, end)
            self.calendar.add_event(event)
            self.update_events()
            self.title_input.clear()

        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

    def update_events(self):
        self.event_list.clear()
        date = self.calendar_widget.selectedDate()
        start = datetime.combine(date.toPyDate(), datetime.min.time())
        end = datetime.combine(date.toPyDate(), datetime.max.time())

        for event in self.calendar.get_events(start, end):
            self.event_list.addItem(str(event))