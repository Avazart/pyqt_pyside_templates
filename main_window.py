from PyQt5 import uic
# from PyQt5.QtWidgets import QMainWindow

(Ui_MainWindow, QMainWindow) = uic.loadUiType('main_window.ui')


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def __del__(self):
        self.ui = None
