from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

form_test_result_screen = uic.loadUiType("C:/Users/savif/workspace/Noodle_Company/gui/ui/test_result.ui")[0]

class test_result_Screen(QMainWindow, form_test_result_screen):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.hide)
        self.pushButton.clicked.connect(self.calculate_investment_bias_type)

    def calculate_investment_bias_type(self):
        f = open("C:/Users/savif/workspace/Noodle_Company/gui/ui/total_score.txt", 'r')
        total_score = float(f.readline())
        f.close()
        print("result total_score: ", total_score)
        if total_score <= 20:
            bias_type = "안정형"
        elif total_score <= 40:
            bias_type = "안정추구형"
        elif total_score <= 60:
            bias_type = "위험중립형"
        elif total_score <= 80:
            bias_type = "적극투자형"
        else:
            bias_type = "공격투자형"
        self.label_investment_type.setText(f"투자 유형: {bias_type}, {round(total_score)}")
