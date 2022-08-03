from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys

import numpy as np
import matplotlib.pyplot as plt


class Ui(QMainWindow):

    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('maincalc.ui', self)
        self.show()
        self.pushRun.clicked.connect(self.runcalc)

    def runcalc(self):
        """
        public void runcalc

        MODIFIES: self

        EFFECTS: executes the corresponding methods depending on the
                 current tab (either compute or graph) open.
        """
        if self.tabWidget.currentIndex() == 0:
            self.compute()
        elif self.tabWidget.currentIndex() == 1:
            self.graph()
        else:
            print(-1)

    def compute(self):
        """
        REQUIRES: valid compute text

        EFFECTS: computes arithmetic

        :return:
        """
        return None

    def graph(self):
        """
        REQUIRES: valid equation/inequality

        EFFECTS: displays a graph of the equation

        :return:
        """
        return None


calc = QApplication(sys.argv)
mainWin = Ui()

if __name__ == "__main__":
    calc.exec()
