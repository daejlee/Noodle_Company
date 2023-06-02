import sys
from PyQt5.QtWidgets import QApplication
from service import main_service_Screen
from invest_bias_test import *
from bias_test_result import *
from invest_principle import *
from assess_market import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_service_sr = main_service_Screen()
    invest_bias_test_sr = invest_bias_test_Screen()
    invest_bias_test_sr.pushButton.clicked.connect(main_service_sr.show)
    bias_test_result_sr = test_result_Screen()
    invest_bias_test_sr.pushButton_2.clicked.connect(bias_test_result_sr.show)
    assessMarket_sr = assessMarket()
    invest_principle_sr = investPrinciple()
    detail_1_sr = detail_1()
    detail_2_sr = detail_2()
    detail_3_sr = detail_3()
    detail_4_sr = detail_4()
    detail_5_sr = detail_5()
    invest_principle_sr.pushButton.clicked.connect(detail_1_sr.show)
    invest_principle_sr.pushButton_2.clicked.connect(detail_2_sr.show)
    invest_principle_sr.pushButton_3.clicked.connect(detail_3_sr.show)
    invest_principle_sr.pushButton_4.clicked.connect(detail_4_sr.show)
    invest_principle_sr.pushButton_5.clicked.connect(detail_5_sr.show)
    main_service_sr.pushButton.clicked.connect(invest_bias_test_sr.show)
    main_service_sr.pushButton_4.clicked.connect(invest_principle_sr.show)
    main_service_sr.pushButton_3.clicked.connect(assessMarket_sr.show)
    main_service_sr.show()

    sys.exit(app.exec_())