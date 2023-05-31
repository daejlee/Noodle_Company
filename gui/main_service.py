from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from invest_bias_test import Screen2
form_class_screen1 = uic.loadUiType("C:/Users/user/Desktop/Noodle_Company/gui/main_service.ui")[0]


class Screen1(QMainWindow, form_class_screen1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.switch_to_screen2)

    def switch_to_screen2(self):
        self.hide()
        Screen2.show
    
    
    #line editor: 사용자가 직접입력
    #label: 글자 입력 가능(... 클릭하면 글자의 색이나 여러가지 바꾸기 가능)

