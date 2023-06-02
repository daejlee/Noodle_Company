from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5 import uic
from shared_data import *

form_invest_bias_test_screen = uic.loadUiType("C:/Users/savif/workspace/Noodle_Company/gui/ui/invest_bias_test.ui")[0]
form_test_result_screen = uic.loadUiType("C:/Users/savif/workspace/Noodle_Company/gui/ui/test_result.ui")[0]

class test_result_Screen(QMainWindow, form_test_result_screen):
    def __init__(self, total_score):
        super().__init__()
        self.setupUi(self)
         # 버튼을 투자 유형 계산 메서드에 연결합니다.
        self.pushButton.clicked.connect(self.calculate_investment_bias_type)
        self.total_score = total_score

        
    def calculate_investment_bias_type(self):
        total_score = self.total_score
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

class invest_bias_test_Screen(QMainWindow, form_invest_bias_test_screen):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.switch_main_service_screen)
        self.pushButton_2.clicked.connect(self.switch_test_result_screen)
        
        self.button_scores = {
            self.radioButton_1: 12.5,   # QRadioButton 객체와 점수를 매핑하는 딕셔너리를 생성합니다.
            self.radioButton_2: 12.5,
            self.radioButton_3: 9.3,
            self.radioButton_4: 6.2,
            self.radioButton_5: 3.1,
            self.radioButton_6: 3.1,
            self.radioButton_7: 6.2,
            self.radioButton_8: 9.3,
            self.radioButton_9: 12.5,
            self.radioButton_10: 15.6,
            self.radioButton_11: 3.1,
            self.radioButton_12: 6.2,
            self.radioButton_13: 9.3,
            self.radioButton_14: 12.5,
            self.radioButton_15: 15.6,
            self.radioButton_16: 3.1,
            self.radioButton_17: 6.2,
            self.radioButton_18: 9.3,
            self.radioButton_19: 12.5,
            self.radioButton_20: 15.6,
            self.radioButton_21: 12.5,
            self.radioButton_22: 9.3,
            self.radioButton_23: 6.2,
            self.radioButton_24: 3.1,
            self.radioButton_25: 9.3,
            self.radioButton_26: 6.2,
            self.radioButton_27: 3.1,
            self.radioButton_28: -6.2,
            self.radioButton_29: 6.2,
            self.radioButton_30: 12.5,
            self.radioButton_31: 18.7,
           
            
        }

        self.radioButton_1.clicked.connect(self.calculate_total_score)
        self.radioButton_1.clicked.connect(self.calculate_total_score)
        self.radioButton_2.clicked.connect(self.calculate_total_score)
        self.radioButton_3.clicked.connect(self.calculate_total_score)
        self.radioButton_4.clicked.connect(self.calculate_total_score)
        self.radioButton_5.clicked.connect(self.calculate_total_score)
        self.radioButton_6.clicked.connect(self.calculate_total_score)
        self.radioButton_7.clicked.connect(self.calculate_total_score)
        self.radioButton_8.clicked.connect(self.calculate_total_score)
        self.radioButton_9.clicked.connect(self.calculate_total_score)
        self.radioButton_10.clicked.connect(self.calculate_total_score)
        self.radioButton_11.clicked.connect(self.calculate_total_score)
        self.radioButton_12.clicked.connect(self.calculate_total_score)
        self.radioButton_13.clicked.connect(self.calculate_total_score)
        self.radioButton_14.clicked.connect(self.calculate_total_score)
        self.radioButton_15.clicked.connect(self.calculate_total_score)
        self.radioButton_16.clicked.connect(self.calculate_total_score)
        self.radioButton_17.clicked.connect(self.calculate_total_score)
        self.radioButton_18.clicked.connect(self.calculate_total_score)
        self.radioButton_19.clicked.connect(self.calculate_total_score)
        self.radioButton_20.clicked.connect(self.calculate_total_score)
        self.radioButton_21.clicked.connect(self.calculate_total_score)
        self.radioButton_22.clicked.connect(self.calculate_total_score)
        self.radioButton_23.clicked.connect(self.calculate_total_score)
        self.radioButton_24.clicked.connect(self.calculate_total_score)
        self.radioButton_25.clicked.connect(self.calculate_total_score)
        self.radioButton_26.clicked.connect(self.calculate_total_score)
        self.radioButton_27.clicked.connect(self.calculate_total_score)
        self.radioButton_28.clicked.connect(self.calculate_total_score)
        self.radioButton_29.clicked.connect(self.calculate_total_score)
        self.radioButton_30.clicked.connect(self.calculate_total_score)
        self.radioButton_31.clicked.connect(self.calculate_total_score)

        self.total_score_label = QLabel("Total Score: 0")
        self.verticalLayout.addWidget(self.total_score_label)

    def calculate_total_score(self):
        global TOTALSCORE
        total_score = 0
        for button, score in self.button_scores.items():
            if button.isChecked():
                total_score += score
                TOTALSCORE = total_score
        self.total_score_label.setText(f"Total Score: {total_score}")

    def switch_main_service_screen(self):
        self.hide()
        from service import main_service_Screen
        main_service_Screen.show

    def switch_test_result_screen(self):
        self.hide()
        print(TOTALSCORE)
        res = test_result_Screen(TOTALSCORE)
        res.show()
