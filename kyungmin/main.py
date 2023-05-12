#QMainWindow 클래스는 PyQt에서 창을 만들기 위한 기본 클래스이며, MainWindow 클래스와 NextWindow 클래스는 각각 메인 창과 다음 창을 나타냄
from PyQt5.QtWidgets import QApplication
from first_screen import FirstScreen

if __name__ == '__main__':
    app = QApplication([])
    first_screen = FirstScreen()
    first_screen.show()
    app.exec_()
