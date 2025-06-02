import pytest
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