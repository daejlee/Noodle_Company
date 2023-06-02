from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class_IP = uic.loadUiType("C:/Users/savif/workspace/Noodle_Company/gui/ui/invest_principle.ui")[0]
form_class_detail_1 = uic.loadUiType("C:/Users/savif/workspace/Noodle_Company/gui/ui/invest_principles_detail_1.ui")[0]
form_class_detail_2 = uic.loadUiType("C:/Users/savif/workspace/Noodle_Company/gui/ui/invest_principles_detail_2.ui")[0]
form_class_detail_3 = uic.loadUiType("C:/Users/savif/workspace/Noodle_Company/gui/ui/invest_principles_detail_3.ui")[0]
form_class_detail_4 = uic.loadUiType("C:/Users/savif/workspace/Noodle_Company/gui/ui/invest_principles_detail_4.ui")[0]
form_class_detail_5 = uic.loadUiType("C:/Users/savif/workspace/Noodle_Company/gui/ui/invest_principles_detail_5.ui")[0]
class investPrinciple(QMainWindow, form_class_IP):
	def __init__(self):
		super().__init__()
		self.setupUi(self)

class detail_1(QMainWindow, form_class_detail_1):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.move(1200, 150)
		self.pushButton.clicked.connect(self.hide)

class detail_2(QMainWindow, form_class_detail_2):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.move(1200, 150)
		self.pushButton.clicked.connect(self.hide)

class detail_3(QMainWindow, form_class_detail_3):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.move(1200, 150)
		self.pushButton.clicked.connect(self.hide)

class detail_4(QMainWindow, form_class_detail_4):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.move(1200, 150)
		self.pushButton.clicked.connect(self.hide)

class detail_5(QMainWindow, form_class_detail_5):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.move(1200, 150)
		self.pushButton.clicked.connect(self.hide)
