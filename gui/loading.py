import sys
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import*
from PyQt5 import uic

form_class_loading = uic.loadUiType("C:/Users/savif/workspace/Noodle_Company/gui/ui/loading.ui")[0]

class loading(QMainWindow, form_class_loading):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.movie = QMovie("C:/Users/savif/workspace/Noodle_Company/gui/ui/image/loading_200px.gif", QByteArray(), self)
		self.movie.setCacheMode(QMovie.CacheAll)
		self.label.setMovie(self.movie)
		self.movie.start()
		# self.setWindowFlags(Qt.FramelessWindowHint)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	myWindow = loading()
	myWindow.show()
	app.exec_()