from PyQt5 import QtWidgets
from PyQt5 import QtCore


class Mywindows(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("파이썬 GUI")

        button = QtWidgets.QPushButton(self)
        button.setText("일반버튼")

        disablebutton = QtWidgets.QPushButton(self)
        disablebutton.setText("비활성화버튼")
        disablebutton.setEnabled(False)

        checkbutton = QtWidgets.QPushButton(self)
        checkbutton.setText("체크버튼")
        checkbutton.setCheckable(True)
        checkbutton.toggle()

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(button)
        layout.addWidget(disablebutton)
        layout.addWidget(checkbutton)

        self.setLayout(layout)
        self.resize(400, 300)
        self.show()


app = QtWidgets.QApplication([])
win = Mywindows()
app.exec_()
