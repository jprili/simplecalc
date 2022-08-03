from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys


class Ui(QMainWindow):

    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('maincalc.ui', self)
        self.show()
        self.pushRun.clicked.connect(self.runcalc)

    def runcalc(self):
        if self.tabWidget.currentIndex() == 0:
            print(0)
        elif self.tabWidget.currentIndex() == 1:
            print(1)
        else:
            print(-1)


calc = QApplication(sys.argv)
mainWin = Ui()

if __name__ == "__main__":
    calc.exec()
