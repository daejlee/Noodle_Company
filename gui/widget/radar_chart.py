import sys
import pandas as pd
from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from math import pi


## 데이터 준비
df = pd.DataFrame({
'company': ['c1', 'c2', 'c3', 'c4', 'c5'],
'score1': [10, 5, 3, 2, 7],
'score2': [4, 10, 3, 3, 8],
'score3': [9, 9, 7, 7, 8],
'score4': [4, 4, 10, 10, 6],
'score5': [2, 6, 8, 9, 8]
})


class MyWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
		self.setLayout(self.layout)
		self.setGeometry(200, 200, 800, 600)

	def initUI(self):
		self.fig = plt.figure(figsize=(8, 8))
		self.fig.set_facecolor('white')

		self.canvas = FigureCanvas(self.fig)

		layout = QVBoxLayout()
		layout.addWidget(self.canvas)

		cb = QComboBox()
		cb.addItem('Graph1')
		cb.addItem('Graph2')
		cb.activated[str].connect(self.onComboBoxChanged)
		layout.addWidget(cb)

		self.layout = layout
		self.onComboBoxChanged(cb.currentText())

	def onComboBoxChanged(self, text):
		if text == 'Graph1':
			self.doGraph1()
		elif text == 'Graph2':
			self.doGraph2()

	def doGraph1(self):
		## 하나의 회사 선택
		target_company = 'c1'
		labels = df.columns[1:]
		data = df.loc[df['company'] == target_company, labels].values.flatten().tolist()
		data.append(data[0])  # 시작점의 값 추가

		## 레이더 차트 그리기
		num_labels = len(labels)
		angles = [x / float(num_labels) * (2 * pi) for x in range(num_labels)]
		angles += angles[:1]

		ax = self.fig.add_subplot(111, polar=True)  # 서브플롯 추가 (111: 1x1 그리드의 첫 번째)

		ax.set_theta_offset(pi / 2)
		ax.set_theta_direction(-1)

		plt.xticks(angles[:-1], labels, fontsize=13)
		ax.tick_params(axis='x', which='major', pad=15)

		ax.set_rlabel_position(0)
		plt.yticks([0, 2, 4, 6, 8, 10], ['0', '2', '4', '6', '8', '10'], fontsize=10)
		plt.ylim(0, 10)

		# 레이더 차트 그리기
		ax.plot(angles, data, color='blue', linewidth=2, linestyle='solid')
		ax.fill(angles, data, color='blue', alpha=0.4)

		# 각 스코어 값 표시
		for i, (angle, score) in enumerate(zip(angles, data[:-1])):
			angle_deg = angle * 180 / pi  # 각도를 degree로 변환
			if angle_deg <= 90:
				ha = 'left'
				va = 'bottom'
			else:
				ha = 'right'
				va = 'bottom'
			ax.text(angle, score + 0.5, str(score), color='blue', ha=ha, va=va)

		# 회사명 표시
		x = 0  # x 좌표
		y = 0.9  # y 좌표
		self.fig.text(x, y, target_company, color='black', fontsize=24, ha='left', va='center')

		self.canvas.draw()


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MyWindow()
	window.show()
	app.exec_()
