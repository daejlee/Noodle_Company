import sys
from PyQt5.QtWidgets import QApplication
from second_screen import FirstScreen

if __name__ == "__main__":
    app = QApplication(sys.argv)
    first_screen = FirstScreen()
    first_screen.show()
    sys.exit(app.exec_())
    from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton


    class FirstScreen(QWidget):
        def __init__(self, parent=None):
            super().__init__(parent)
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


    class SecondScreen(QWidget):
        def __init__(self, parent=None):
            super().__init__(parent)
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


    class ThirdScreen(QWidget):
        def __init__(self, parent=None):
            super().__init__(parent)
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


    class FourthScreen(QWidget):
        def __init__(self, label_text, parent=None):
            super().__init__(parent)
            layout = QVBoxLayout()
            label = QLabel(label_text)
            layout.addWidget(label)
            self.setLayout(layout)


    class FifthScreen(QWidget):
        def __init__(self, label_text, parent=None):
            super().__init__(parent)
            layout = QVBoxLayout()
            label = QLabel(label_text)
            layout.addWidget(label)
            self.setLayout(layout)
