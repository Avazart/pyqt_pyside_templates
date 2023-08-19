import sys
from PyQt5.QtWidgets import QApplication

from main_window import MainWindow


def main() -> int:
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    return app.exec()


if __name__ == '__main__':
    sys.exit(main())
