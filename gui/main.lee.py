import sys
from PyQt5.QtWidgets import QApplication
from main_service import Screen1
from invest_bias_test import Screen2
from test_result import Screen3

if __name__ == '__main__':
    app = QApplication(sys.argv)

    screen1 = Screen1()
    screen2 = Screen2()
    screen3 = Screen3()

    screen1.pushButton.clicked.connect(screen2.show)  # Show Screen2 when button on Screen1 is clicked
    screen2.pushButton.clicked.connect(screen1.show)  # Show Screen1 when button on Screen2 is clicked
    screen2.pushButton_2.clicked.connect(screen3.show)  # Show Screen3 when button on Screen2 is clicked

    screen1.show()

    sys.exit(app.exec_())