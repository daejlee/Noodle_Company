from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from invest_bias_test import invest_bias_test_Screen
form_main_service_screen = uic.loadUiType("C:/Users/savif/workspace/Noodle_Company/gui/ui/main_service.ui")[0]


class main_service_Screen(QMainWindow, form_main_service_screen):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.switch_invest_bias_test_screen)

    def switch_invest_bias_test_screen(self):
        self.hide()
        invest_bias_test_Screen.show
    
    
    #line editor: 사용자가 직접입력
    #label: 글자 입력 가능(... 클릭하면 글자의 색이나 여러가지 바꾸기 가능)

