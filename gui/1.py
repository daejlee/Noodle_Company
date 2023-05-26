import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):

	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		#생성자 (QPushButton())의 첫 번째 파라미터에는 버튼에 표시될 텍스트를 입력하고, 두 번째 파라미터에는 버튼이 위치할 부모 위젯을 입력합니다.
		btn = QPushButton('Quit', self)
		btn.move(200, 200)
		btn.resize(btn.sizeHint())
		btn.clicked.connect(QCoreApplication.instance().quit)
		
		self.setWindowTitle('잔치국수 증권사')
		self.setWindowIcon(QIcon('web.png'))
		self.resize(1280, 720)
		
		
		self.show()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = MyApp()
	sys.exit(app.exec_())