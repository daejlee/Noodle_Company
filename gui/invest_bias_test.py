from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5 import uic
from shared_data import *

form_invest_bias_test_screen = uic.loadUiType("C:/Users/savif/workspace/Noodle_Company/gui/ui/invest_bias_test.ui")[0]

class invest_bias_test_Screen(QMainWindow, form_invest_bias_test_screen):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
        total_score = 0
        for button, score in self.button_scores.items():
            if button.isChecked():
                total_score += score
                f = open('C:/Users/savif/workspace/Noodle_Company/gui/ui/total_score.txt', 'w')
                f.write(str(total_score))
                f.close()
        self.total_score_label.setText(f"Total Score: {total_score}")
