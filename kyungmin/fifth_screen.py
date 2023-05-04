from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel


class FifthScreen(QWidget):
    def __init__(self, label_text, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()
        label = QLabel(label_text)
        layout.addWidget(label)
        self.setLayout(layout)