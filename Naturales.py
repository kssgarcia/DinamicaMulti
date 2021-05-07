from pyqtgraph.Qt import QtGui, QtCore, QtWidgets
import numpy as np
import pyqtgraph as pg
from sympy import symbols, evalf, diff, sin, cos, Matrix, lambdify


class  CoordenadasNaturales:
    def __init__(self,win1, win2, win3, win4, app, I1, I2, I3, I4, phi2inicial, omega2inicial, alpha2inicial, time_simul):
        win1.resize(1200, 700)
        win1.setWindowTitle('simulacion')
        self.app = app
        self.barra1 = win1.plot(pen=pg.mkPen('b', width=3), symbolPen ='g',brush=pg.mkBrush(30, 255, 35, 255))
        self.barra2 = win1.plot(pen=pg.mkPen('g', width=3), symbolPen ='g')
        self.barra3 = win1.plot(pen=pg.mkPen('r', width=3), symbolPen ='g')
        self.barra4 = win1.plot(pen=pg.mkPen(color=(128,128,128), width=3))
        self.barra1.setBrush([11, 12])
        win1.setXRange(-2.5, 10, padding=0)
        win1.setYRange(-2.5, 10, padding=0)
        self.I1 = I1
        self.I2 = I2
        self.I3 = I3
        self.I4 = I4
        self.xA = 0
        self.yA = 0
        self.xB = 5.908
        self.yB = 1.0418
        self.phi2inicial = phi2inicial
        self.omega2inicial = omega2inicial
        self.alpha2inicial = alpha2inicial
        self.time_simul = time_simul
        #plot posicion
        win2.resize(1200, 700)
        win2.setWindowTitle('posicion')
        self.plot_posicion_1 = win2.plot(pen=pg.mkPen('b', width=3))
        self.plot_posicion_2 = win2.plot(pen=pg.mkPen('g', width=3))
        self.plot_posicion_3 = win2.plot(pen=pg.mkPen('r', width=3))
        self.posiciones_1 = []
        self.posiciones_2 = []
        self.posiciones_3 = []
        #plot velocidad
        win3.resize(1200, 700)
        win3.setWindowTitle('velocidad')
        self.plot_velocidad_1 = win3.plot(pen=pg.mkPen('b', width=3))
        self.plot_velocidad_2 = win3.plot(pen=pg.mkPen('g', width=3))
        self.plot_velocidad_3 = win3.plot(pen=pg.mkPen('r', width=3))
        self.velocidad_1 = []
        self.velocidad_2 = []
        self.velocidad_3 = []
        #plot aceleracion
        win4.resize(1200, 700)
        win4.setWindowTitle('aceleracion')
        self.plot_aceleracion_1 = win4.plot(pen=pg.mkPen('b', width=3))
        self.plot_aceleracion_2 = win4.plot(pen=pg.mkPen('g', width=3))
        self.plot_aceleracion_3 = win4.plot(pen=pg.mkPen('r', width=3))
        self.aceleracion_1 = []
        self.aceleracion_2 = []
        self.aceleracion_3 = []

    def SolucionNaturales(self):
        cont = 0
        x=[.4, 1, 2.2, 2]
        step = 0.01
        x1, y1, x2, y2, t = symbols('x1 y1 x2 y2 t')
        w_2, w_3, w_4 = symbols('w_2 w_3 w_4')
        self.w = np.array([[w_2], [w_3], [w_4]])
        q = np.array([[x1], [y1], [x2], [y2]])

        phi = [[ pow((x1-self.xA),2) + pow((y1-self.yA),2) - pow(self.I2,2)],
            [pow((x2-x1),2) + pow((y2-y1),2) - pow(self.I3,2)],
            [pow((x2-self.xB),2) + pow((y2-self.yB),2) - pow(self.I4,2)],
            [x1 - self.xA - self.I2*cos((0.5*self.alpha2inicial)*pow(t,2) + self.omega2inicial*t + self.phi2inicial)]]
        jaco = np.array(self.derivate(phi, q, None, 0))
        jaco_point = np.array(self.derivateMatrix(jaco, q, None, 0))
        ti = []
        x = np.reshape(x, (len(x), -1))

        phi = lambdify([x1, y1, x2, y2, t], phi)
        jaco = lambdify([x1, y1, x2, y2, t], jaco)
        jaco_point = lambdify([x1, y1, x2, y2, t], jaco_point)

        for i in np.arange(0, self.time_simul, step):
            float(i)
            cont += 1
            rest = 10
            while rest > 0.00001:
                phiEval = np.array(phi(x[0][0], x[1][0], x[2][0], x[3][0], i))
                jacobian = np.array(jaco(x[0][0], x[1][0], x[2][0], x[3][0], i))
                phiSys = np.array(phiEval).astype(np.float64)
                jacobianEval = np.array(jacobian).astype(np.float64)
                xf = x - np.dot(np.linalg.inv(jacobianEval), phiSys)
                x = xf
                rest = np.linalg.norm(phiSys)

            v_1 = [0, 0, 0, self.I2*(self.alpha2inicial*i+self.omega2inicial)*sin(0.5*pow(self.alpha2inicial*i,2) + self.omega2inicial*i + self.phi2inicial)]
            vi = np.dot(-np.linalg.inv(jacobianEval), np.reshape(v_1, (len(x), -1)))

            jacobina_point = np.array(jaco(x[0][0], x[1][0], x[2][0], x[3][0], i))

            a_1 = [0, 0, 0, ((self.I2*self.alpha2inicial*sin(0.5*pow(self.alpha2inicial*i,2) + self.omega2inicial*i + self.phi2inicial)) + self.I2*pow((self.alpha2inicial*i+self.omega2inicial),2)*cos(0.5*pow((self.alpha2inicial*i),2) + self.omega2inicial*i + self.phi2inicial))]
            ai = np.dot(-np.linalg.inv(jacobianEval),(np.dot(-jacobina_point,vi)+np.reshape(a_1, (len(x), -1))))
            ti.append(float(i))

            self.barra1.setData([self.xA, xf[0][0]], [self.yA, xf[1][0]])
            self.barra2.setData([xf[0][0], xf[2][0]], [xf[1][0], xf[3][0]])
            self.barra3.setData([xf[2][0], self.xB], [xf[3][0], self.yB])
            self.barra4.setData([self.xB, self.xA], [self.yB, self.yA])
            # graficar la posicion
            self.posiciones_1.append(xf[0][0])
            self.posiciones_2.append(xf[1][0])
            self.posiciones_3.append(xf[2][0])
            self.plot_posicion_1.setData(ti, self.posiciones_1)
            self.plot_posicion_2.setData(ti, self.posiciones_2)
            self.plot_posicion_3.setData(ti, self.posiciones_3)
            # # graficar la velocidad
            self.velocidad_1.append(float(vi[0][0]))
            self.velocidad_2.append(float(vi[1][0]))
            self.velocidad_3.append(float(vi[2][0]))
            self.plot_velocidad_1.setData(ti, self.velocidad_1)
            self.plot_velocidad_2.setData(ti, self.velocidad_2)
            self.plot_velocidad_3.setData(ti, self.velocidad_3)
            # # graficar la aceleracion
            self.aceleracion_1.append(float(ai[0][0]))
            self.aceleracion_2.append(float(ai[1][0]))
            self.aceleracion_3.append(float(ai[2][0]))
            self.plot_aceleracion_1.setData(ti, self.aceleracion_1)
            self.plot_aceleracion_2.setData(ti, self.aceleracion_2)
            self.plot_aceleracion_3.setData(ti, self.aceleracion_3)
        
            if i >= self.time_simul:
                break
            self.app.processEvents()

        
    def derivate(self, functionOver, derivationVar, container=None, initIter=0):
        if container == None:
            container = []
        holder = []
        for i in range(len(derivationVar)):
            deriv = diff(functionOver[initIter][0], derivationVar[i][0])
            holder.append(deriv)
        container.append(holder)
        initIter += 1
        if initIter < len(functionOver):
            return self.derivate(functionOver, derivationVar, container, initIter)
        else:
            return container

    def derivateMatrix(self, functionOver, derivationVar, container=None, initIter=0):
        if container == None:
            container = []
        holder = []
        for i in range(len(derivationVar)):
            deriv = diff(functionOver[initIter][i], derivationVar[i][0])
            holder.append(deriv)
        container.append(holder)
        initIter += 1
        if initIter < len(functionOver):
            return self.derivateMatrix(functionOver, derivationVar, container, initIter)
        else:
            return container


# if __name__ == '__main__':
#     import sys
#     if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
#         QtGui.QApplication.instance().exec_()