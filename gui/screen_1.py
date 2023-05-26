import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("C:/Users/user/Desktop/Noodle_Company/gui/main.ui")[0]
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    
    
    #line editor: 사용자가 직접입력
    #label: 글자 입력 가능(... 클릭하면 글자의 색이나 여러가지 바꾸기 가능)

