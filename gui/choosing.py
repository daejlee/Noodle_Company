from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

form_main_choose = uic.loadUiType("C:/Users/savif/workspace/Noodle_Company/gui/ui/choose_invest.ui")[0]


class choose(QMainWindow, form_main_choose):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.hide)
        self.pushButton_2.clicked.connect(self.hide)
        self.pushButton_3.clicked.connect(self.hide)
        self.pushButton_4.clicked.connect(self.hide)
        self.pushButton_5.clicked.connect(self.hide)


