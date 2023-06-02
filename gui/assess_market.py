from PyQt5.QtWidgets import *
from PyQt5 import uic
from get_sync_data import get_KOSPI

form_class_AM = uic.loadUiType("C:/Users/savif/workspace/Noodle_Company/gui/ui/assess_market.ui")[0]

class assessMarket(QMainWindow, form_class_AM):
	def __init__(self):
		super().__init__()
		Kospi = float(get_KOSPI().replace(',', ''))
		BI = 0.79 * Kospi / 2150 * 100
		stk = 0
		if BI < 91:
			stk = -10 / 34 * (BI-91) + 70
			if stk > 80:
				stk = 80
		else:
			stk = -0.1865 * (BI-91) * (BI-93.6) + 70
			if stk < 30:
				stk = 30
		Mk_stat = 0
		if BI <= 60:
			Mk_stat = 1
		elif BI <= 77:
			Mk_stat = 2
		elif BI <= 95:
			Mk_stat = 3
		elif BI <= 112:
			Mk_stat = 4
		else: Mk_stat = 5
		if Mk_stat == 1:
			Mk_stat = str(Mk_stat) + ", 매우 양호"
		elif Mk_stat == 2:
			Mk_stat = str(Mk_stat) + ", 양호"
		elif Mk_stat == 3:
			Mk_stat = str(Mk_stat) + ", 보통"
		elif Mk_stat == 4:
			Mk_stat = str(Mk_stat) + ", 위험"
		elif Mk_stat == 5:
			Mk_stat = str(Mk_stat) + ", 매우 위험"
		self.setupUi(self)
		self.pushButton.setText(Mk_stat)
		self.pushButton_2.setText(str(round(stk)) + " : " + str(round(100 - stk)))
