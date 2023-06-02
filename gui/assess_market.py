from PyQt5.QtWidgets import *
from PyQt5 import uic
from get_sync_data import get_KOSPI
from PyQt5.QtGui import *

form_class_AM = uic.loadUiType("C:/Users/savif/workspace/Noodle_Company/gui/ui/assess_market.ui")[0]
form_class_BI = uic.loadUiType("C:/Users/savif/workspace/Noodle_Company/gui/ui/BI_detail.ui")[0]

class BI_detail(QMainWindow, form_class_BI):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.move(1200, 150)
		self.pushButton.clicked.connect(self.hide)

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
			Mk_stat = str(Mk_stat)  + f"(BI: {round(BI)})" + ", 매우 양호"
		elif Mk_stat == 2:
			Mk_stat = str(Mk_stat)  + f"(BI: {round(BI)})" + ", 양호"
		elif Mk_stat == 3:
			Mk_stat = str(Mk_stat)  + f"(BI: {round(BI)})"+ ", 보통"
		elif Mk_stat == 4:
			Mk_stat = str(Mk_stat)  + f"(BI: {round(BI)})"+ ", 위험"
		elif Mk_stat == 5:
			Mk_stat = str(Mk_stat)  + f"(BI: {round(BI)})"+ ", 매우 위험"
		self.setupUi(self)
		qPixmapVar = QPixmap()
		qPixmapVar.load("C:/Users/savif/workspace/Noodle_Company/gui/image/buffet.png")
		self.label_3.setPixmap(qPixmapVar)
		self.label.setText(f'<html><head/><body><p><span style=" font-size:18pt; color:#aa55ff;">현재 주식 시장의 과열도 : {Mk_stat}</span></p></body></html>')
		self.label_2.setText(f'<html><head/><body><p><span style=" font-size:18pt; color:#aa55ff;">권장되는 주식 / 채권 비율: {str(round(stk)) + " : " + str(round(100 - stk))}</span></p></body></html>')
