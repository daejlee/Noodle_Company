from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from invest_bias_test import MyWindow

form_class_screen3 = uic.loadUiType("C:/Users/user/Desktop/Noodle_Company/gui/test_result.ui")[0]


class Screen3(QMainWindow, form_class_screen3):
    def __init__(self):
        super().__init__()
        self.setupUi(self)