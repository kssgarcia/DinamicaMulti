from pyqtgraph.Qt import QtGui, QtCore, QtWidgets
import numpy as np
import pyqtgraph as pg
from sympy import symbols, evalf, diff, sin, cos, Matrix
from PyQt5.QtCore import QThread, pyqtSignal
import time 

class Coordenadas(QThread):
    data = pyqtSignal(int)
    def __init__(self, n, time, parent=None):
        QThread.__init__(self, parent)
        self.n = n
        self.time = time

    def run(self):
        for i in range(self.time):
            a = i*2
            time.sleep(2)
            self.data.emit(self.n)

            