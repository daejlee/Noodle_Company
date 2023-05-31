import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from Buffett import *

form_class_AM = uic.loadUiType("C:/Users/savif/workspace/Noodle_Company/gui/assess_market.ui")[0]

class assessMarket(QMainWindow, form_class_AM):
	def __init__(self):
		super().__init__()
		self.Mk_stat = Mk_stat
		self.stk = stk
		self.setupUi(self)
		self.label.setText("현재 주식 시장의 과열도 : " + str(self.Mk_stat))
		self.label_2.setText("권장되는 주식 / 채권 비율: " + str(round(self.stk)) + " : " + str(round(100 - self.stk)))

if __name__ == '__main__':
	app = QApplication(sys.argv)
	myWindow = assessMarket()
	myWindow.show()
	app.exec_()