import pytest
from PyQt5.QtCore import QTime
from PyQt5.QtWidgets import QApplication
from pycalendar.gui.main_window import MainWindow

@pytest.fixture(scope="module")
def qapp():
    """Фикстура для QApplication"""
    app = QApplication.instance() or QApplication([])
    yield app
    app.quit()

def test_main_window_init(qapp):
    """Тест инициализации главного окна"""
    window = MainWindow()
    assert window.windowTitle() == "PyCalendar"
    assert window.calendar is not None

@pytest.fixture
def main_window(qtbot):
    window = MainWindow()
    qtbot.addWidget(window)
    yield window
    window.close()


def test_main_window_ui(qtbot):
    """Простейший тест интерфейса главного окна"""
    from pycalendar.gui.main_window import MainWindow

    window = MainWindow()
    qtbot.addWidget(window)

    # Простые проверки элементов интерфейса
    assert window.windowTitle() == "PyCalendar"
    assert window.title_input.placeholderText() == "Event Title"
    assert window.add_button.text() == "Add Event"

    # Проверяем начальное время
    assert window.start_time.time().hour() == 9
    assert window.start_time.time().minute() == 0
    assert window.end_time.time().hour() == 10
    assert window.end_time.time().minute() == 0