from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5 import uic
from invest_bias_test import Screen2
form_class_screen3 = uic.loadUiType("C:/Users/user/Desktop/Noodle_Company/gui/ui/test_result.ui")[0]


class Screen3(QMainWindow, form_class_screen3):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
         # 버튼을 투자 유형 계산 메서드에 연결합니다.
        self.pushButton.clicked.connect(self.calculate_investment_bias_type)
        
        
    def calculate_investment_bias_type(self):
        screen2_instance = Screen2()  # Screen2 클래스의 인스턴스 생성
        total_score = screen2_instance.calculate_total_score()  # Screen2 인스턴스에서 총 점수를 가져옵니다.
        
        
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
        
        # 레이블에 투자 유형을 표시합니다.
        self.label_investment_type.setText(f"투자 유형: {bias_type}, {total_score}")