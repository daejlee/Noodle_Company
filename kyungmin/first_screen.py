from PyQt5.QtWidgets import QVBoxLayout, QLabel, QPushButton
from second_screen import SecondScreen
from base_window import BaseWindow

class FirstScreen(BaseWindow):
    def __init__(self):
        super().__init__("잔치국수 증권사", "web.png", 100, 100, 400, 300)
        layout = QVBoxLayout()
        label = QLabel("첫번째 화면입니다.")
        layout.addWidget(label)
        button = QPushButton("시작하기")
        button.clicked.connect(self.start_second_screen)
        layout.addWidget(button)
        self.setLayout(layout)

    def start_second_screen(self):
        self.second_screen = SecondScreen()
        self.second_screen.show()
        self.close()