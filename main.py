from PyQt5 import QtWidgets, uic
import sys


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi("maincalc.ui", self)
        self.show()

calc = QtWidgets.QApplication(sys.argv)
mainWin = Ui()


if __name__ == "__main__":
    calc.exec()