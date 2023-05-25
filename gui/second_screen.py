from PyQt5.QtWidgets import QVBoxLayout, QLabel, QPushButton
from third_screen import ThirdScreen
from base_window import BaseWindow

class SecondScreen(BaseWindow):
    def __init__(self):
        super().__init__("잔치국수 증권사", "web.png", 100, 100, 400, 300)
        layout = QVBoxLayout()
        label = QLabel("두번째 화면입니다.")
        layout.addWidget(label)
        button = QPushButton("다음")
        button.clicked.connect(self.start_third_screen)
        layout.addWidget(button)
        self.setLayout(layout)

    def start_third_screen(self):
        self.third_screen = ThirdScreen()
        self.third_screen.show()
        self.close()