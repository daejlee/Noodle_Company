from PyQt5.QtWidgets import QVBoxLayout, QLabel, QPushButton
from fourth_screen import FourthScreen
from fifth_screen import FifthScreen
from base_window import BaseWindow

class ThirdScreen(BaseWindow):
    def __init__(self):
        super().__init__("잔치국수 증권사", "web.png", 100, 100, 400, 300)
        layout = QVBoxLayout()
        label = QLabel("세번째 화면입니다.")
        layout.addWidget(label)
        button1 = QPushButton("공격형 투자자")
        button1.clicked.connect(self.show_fourth_screen_attacker)
        layout.addWidget(button1)
        button2 = QPushButton("방어형 투자자")
        button2.clicked.connect(self.show_fifth_screen_defender)
        layout.addWidget(button2)
        self.setLayout(layout)

    def show_fourth_screen_attacker(self):
        self.fourth_screen = FourthScreen("공격형 투자자입니다.")
        self.fourth_screen.show()

    def show_fifth_screen_defender(self):
        self.fifth_screen = FifthScreen("방어형 투자자입니다.")
        self.fifth_screen.show()