import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class_IP = uic.loadUiType("C:/Users/savif/workspace/Noodle_Company/gui/invest_principle.ui")[0]
form_class_detail = uic.loadUiType("C:/Users/savif/workspace/Noodle_Company/gui/invest_principles_detail.ui")[0]
class investPrinciple(QMainWindow, form_class_IP):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.pushButton.clicked.connect(self.pop_detail)
		self.detail_1 = detail_1()
	def pop_detail(self):
		# self.hide()
		self.detail_1.show()

class detail_1(QMainWindow, form_class_detail):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.pushButton.clicked.connect(self.hide)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	myWindow = investPrinciple()
	myWindow.show()
	app.exec_()