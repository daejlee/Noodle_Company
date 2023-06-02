import sys
from PyQt5.QtWidgets import QApplication
from service import main_service_Screen
from invest_bias_test import *
from bias_test_result import *
from shared_data import *

if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_service_sr = main_service_Screen()
    invest_bias_test_sr = invest_bias_test_Screen()
    bias_test_result_sr = test_result_Screen()
    main_service_sr.pushButton.clicked.connect(invest_bias_test_sr.show)
    invest_bias_test_sr.pushButton.clicked.connect(main_service_sr.show)
    invest_bias_test_sr.pushButton_2.clicked.connect(bias_test_result_sr.show)
    main_service_sr.show()

    sys.exit(app.exec_())