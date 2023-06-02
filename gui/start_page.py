from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

form_main_start = uic.loadUiType("C:/Users/savif/workspace/Noodle_Company/gui/ui/start_main.ui")[0]


class start(QMainWindow, form_main_start):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.hide)


