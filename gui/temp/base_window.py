from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget
class BaseWindow(QWidget):
    def __init__(self, title, icon_path, x, y, width, height):
        super().__init__()
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon(icon_path))
        self.setGeometry(x, y, width, height)