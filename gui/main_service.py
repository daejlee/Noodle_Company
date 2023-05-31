import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class_screen1 = uic.loadUiType("C:/Users/user/Desktop/Noodle_Company/gui/main_service.ui")[0]
form_class_screen2 = uic.loadUiType("C:/Users/user/Desktop/Noodle_Company/gui/invest_bias_test.ui")[0]
form_class_screen3 = uic.loadUiType("C:/Users/user/Desktop/Noodle_Company/gui/test_result.ui")[0]


class Screen1(QMainWindow, form_class_screen1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.switch_to_screen2)

    def switch_to_screen2(self):
        self.hide()
        screen2.show()


class Screen2(QMainWindow, form_class_screen2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.switch_to_screen1)
        self.pushButton_2.clicked.connect(self.switch_to_screen3)
    def switch_to_screen1(self):
        self.hide()
        screen1.show()
    def switch_to_screen3(self):
        self.hide()
        screen3.show()
        

class Screen3(QMainWindow, form_class_screen3):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
               


if __name__ == '__main__':
    app = QApplication(sys.argv)

    screen1 = Screen1()
    screen2 = Screen2()
    screen3 = Screen3()

    screen1.show()

    sys.exit(app.exec_())
    
    
    #line editor: 사용자가 직접입력
    #label: 글자 입력 가능(... 클릭하면 글자의 색이나 여러가지 바꾸기 가능)

