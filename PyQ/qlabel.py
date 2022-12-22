from PyQt5 import QtWidgets
from PyQt5 import QtCore


class Mywindows(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("파이썬 GUI")

        label1 = QtWidgets.QLabel("Label1", self)
        label1.setAlignment(QtCore.Qt.AlignCenter)
        label1.resize(60, 30)

        label2 = QtWidgets.QLabel("Label2", self)
        label2.setAlignment(QtCore.Qt.AlignLeft)
        label2.setStyleSheet("color: red; font-size:20px")
        label2.resize(60, 30)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)

        self.setLayout(layout)
        self.resize(400, 300)
        self.show()


app = QtWidgets.QApplication([])
win = Mywindows()
app.exec_()
