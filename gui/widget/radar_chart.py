import sys
import pandas as pd
from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvas
from math import pi
from PyQt5 import uic

from matplotlib.figure import Figure

## 데이터 준비
df = pd.DataFrame({
    'company': ['c1', 'c2', 'c3', 'c4', 'c5'],
    'score1': [10, 5, 3, 2, 7],
    'score2': [4, 10, 3, 3, 8],
    'score3': [9, 9, 7, 7, 8],
    'score4': [4, 4, 10, 10, 6],
    'score5': [2, 6, 8, 9, 8]
})

class MyCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        fig.set_facecolor('white')
        self.axes = fig.add_subplot(111, polar=True)

        super().__init__(fig)

        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def plotGraph1(self):
        ## 하나의 회사 선택
        target_company = 'c1'
        labels = df.columns[1:]
        data = df.loc[df['company'] == target_company, labels].values.flatten().tolist()
        data.append(data[0])  # 시작점의 값 추가

        ## 레이더 차트 그리기
        num_labels = len(labels)
        angles = [x / float(num_labels) * (2 * pi) for x in range(num_labels)]
        angles += angles[:1]

        self.axes.clear()

        self.axes.set_theta_offset(pi / 2)
        self.axes.set_theta_direction(-1)

        self.axes.set_xticks(angles[:-1])
        self.axes.set_xticklabels(labels, fontsize=13)
        self.axes.tick_params(axis='x', which='major', pad=15)

        self.axes.set_rlabel_position(0)
        self.axes.set_yticks([0, 2, 4, 6, 8, 10])
        self.axes.set_yticklabels(['0', '2', '4', '6', '8', '10'], fontsize=10)
        self.axes.set_ylim(0, 10)

        self.axes.plot(angles, data, color='blue', linewidth=2, linestyle='solid')
        self.axes.fill(angles, data, color='blue', alpha=0.4)

        for i, (angle, score) in enumerate(zip(angles, data[:-1])):
            angle_deg = angle * 180 / pi
            if angle_deg <= 90:
                ha = 'left'
                va = 'bottom'
            else:
                ha = 'right'
                va = 'bottom'
            self.axes.text(angle, score + 0.5, str(score), color='blue', ha=ha, va=va)

        self.draw()

    def plotGraph2(self):
        ## 여러 회사 선택
        target_companies = ['c2', 'c3', 'c4', 'c5']
        labels = df.columns[1:]

        self.axes.clear()

        self.axes.set_theta_offset(pi / 2)
        self.axes.set_theta_direction(-1)

        self.axes.set_xticks([])
        self.axes.set_yticks([])

        colors = ['orange', 'green', 'red', 'purple']

        for i, company in enumerate(target_companies):
            data = df.loc[df['company'] == company, labels].values.flatten().tolist()
            data.append(data[0])  # 시작점의 값 추가

            num_labels = len(labels)
            angles = [x / float(num_labels) * (2 * pi) for x in range(num_labels)]
            angles += angles[:1]

            self.axes.plot(angles, data, color=colors[i], linewidth=1, linestyle='solid')
            self.axes.fill(angles, data, color=colors[i], alpha=0.3)

            for angle, score in zip(angles, data[:-1]):
                angle_deg = angle * 180 / pi
                if angle_deg <= 90:
                    ha = 'left'
                    va = 'bottom'
                else:
                    ha = 'right'
                    va = 'bottom'
                self.axes.text(angle, score + 0.5, str(score), color=colors[i], ha=ha, va=va)

        self.draw()

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("c:/Users/user/Desktop/Noodle_Company/gui/widget/monitoring.ui", self)
        self.canvas = FigureCanvasQTAgg(self.centralwidget)
        self.canvas.setGeometry(100, 70, 541, 461)
        self.pushButton.clicked.connect(self.canvas.plotGraph1)
        self.pushButton_2.clicked.connect(self.canvas.plotGraph2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()