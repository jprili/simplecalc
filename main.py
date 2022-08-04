from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys

import sympy
import numpy as np
import matplotlib.pyplot as plt
import datetime


class Ui(QMainWindow):

    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('maincalc.ui', self)
        self.show()
        self.pushRun.clicked.connect(self.runcalc)
        self.pushClear.clicked.connect(self.clearLog)

    def clearLog(self):
        self.plainTextLog.setPlainText("")

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
        """

        try:
            now = datetime.datetime.now()
            curr = self.plainTextCom.toPlainText()
            out = sympy.sympify(str(curr))

            self.plainTextLog.append("\n______ \n" + now.strftime("%Y-%m-%d %H:%M:%S") + "\n" +
                                              str(curr) + "\n" + str(out))

        except:
            self.plainTextLog.append("\n______ \n" + now.strftime("%Y-%m-%d %H:%M:%S") + "\n" +
                                              str(curr) + "\n" + "Error. Try Again")




    def graph(self):
        """
        REQUIRES: valid equation/inequality

        EFFECTS: displays a graph of the equation
        """

        print('graph')


if __name__ == "__main__":
    calc = QApplication(sys.argv)
    mainWin = Ui()
    calc.exec()
