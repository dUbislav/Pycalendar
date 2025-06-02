import sys
import os
import pytest
import traceback
from PyQt5.QtWidgets import QApplication


def run_tests():
    """Запуск тестов с покрытием"""
    print("🔄 Running tests with coverage...")

    tests_path = os.path.join("src", "pycalendar", "tests")
    if not os.path.exists(tests_path):
        print(f"❌ Error: Tests directory not found at {tests_path}", file=sys.stderr)
        return False

    try:
        test_result = pytest.main([
            tests_path,
            "--cov=src/pycalendar",
            "--cov-report=term-missing",
            "-v",
            "--no-header"
        ])
        return test_result == 0
    except Exception as e:
        print(f"❌ Test execution failed: {e}", file=sys.stderr)
        traceback.print_exc()
        return False


def run_application():
    """Запуск основного приложения"""
    print("🚀 Starting application...")
    try:
        from pycalendar.gui.main_window import MainWindow

        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        print("✅ Application started successfully")
        return app.exec_()
    except Exception as e:
        print(f"❌ Application failed to start: {e}", file=sys.stderr)
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    # Шаг 1: Запуск тестов
    if not run_tests():
        print("❌ Tests failed, aborting application launch")
        sys.exit(1)

    # Шаг 2: Запуск приложения
    exit_code = run_application()
    sys.exit(exit_code)