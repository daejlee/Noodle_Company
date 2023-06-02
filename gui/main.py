import sys
from PyQt5.QtWidgets import QApplication
from service import main_service_Screen
from invest_bias_test import *
from shared_data import *
# from test_result import Screen3

if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_service_sr = main_service_Screen()
    invest_bias_test_sr = invest_bias_test_Screen()

    main_service_sr.pushButton.clicked.connect(invest_bias_test_sr.show)  # Show Screen2 when button on Screen1 is clicked

    main_service_sr.show()

    sys.exit(app.exec_())