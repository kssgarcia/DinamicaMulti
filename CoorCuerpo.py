from pyqtgraph.Qt import QtGui, QtCore, QtWidgets
import numpy as np
import pyqtgraph as pg
from sympy import symbols, evalf, diff, sin, cos, Matrix, lambdify


class  CoordenadasCuerpo:
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
        #entradas
        self.I1 = I1
        self.I2 = I2
        self.I3 = I3
        self.I4 = I4
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

    def SolucionCuerpo(self):
        cont = 0
        x=[3, 0, 0, 1, 0, 0, 2.4, 1.9, 1.3, 4.4, 1.9, 2.2]
        step = 0.01
        x1, y1, phi1, x2, y2, phi2, x3, y3, phi3, x4, y4, phi4, t = symbols('x1 y1 phi1 x2 y2 phi2 x3 y3 phi3 x4 y4 phi4 t')
        q = np.array([[x1], [y1], [phi1], [x2], [y2], [phi2], [x3], [y3], [phi3], [x4], [y4], [phi4]])

        phi = [[x1-cos(phi1)*(self.I1/2) - x2+cos(phi2)*(self.I2/2)],
            [y1-sin(phi1)*(self.I1/2) - y2+sin(phi2)*(self.I2/2)],
            [x2+cos(phi2)*(self.I2/2) - x3+cos(phi3)*(self.I3/2)],
            [y2+sin(phi2)*(self.I2/2) - y3+sin(phi3)*(self.I3/2)],
            [x3+cos(phi3)*(self.I3/2) - x4-cos(phi4)*(self.I4/2)],
            [y3+sin(phi3)*(self.I3/2) - y4-sin(phi4)*(self.I4/2)],
            [x1+cos(phi1)*(self.I1/2) - x4+cos(phi4)*(self.I4/2)],
            [y1+sin(phi1)*(self.I1/2) - y4+sin(phi4)*(self.I4/2)],
            [ x1 - (self.I1/2) ],
            [ y1 ],
            [ phi1 ],
            [phi2-self.phi2inicial-self.omega2inicial*t-0.5*self.alpha2inicial*(pow(t,2))]]
        jaco = np.array(self.derivate(phi, q, None, 0))
        jaco_point = np.array(self.derivateMatrix(jaco, q, None, 0))
        ti = []
        x = np.reshape(x, (len(x), -1))
        phi = lambdify([x1, y1, phi1, x2, y2, phi2, x3, y3, phi3, x4, y4, phi4, t], phi)
        jaco = lambdify([x1, y1, phi1, x2, y2, phi2, x3, y3, phi3, x4, y4, phi4, t], jaco)
        jaco_point = lambdify([x1, y1, phi1, x2, y2, phi2, x3, y3, phi3, x4, y4, phi4, t], jaco_point)

        for i in np.arange(0, self.time_simul, step):
            float(i)
            cont += 1
            rest = 10
            while rest > 0.00001:
                phiEval = np.array(phi(x[0][0], x[1][0], x[2][0], x[3][0], x[4][0], x[5][0], x[6][0], x[7][0], x[8][0], x[9][0], x[10][0], x[11][0], i))
                jacobian = np.array(jaco(x[0][0], x[1][0], x[2][0], x[3][0], x[4][0], x[5][0], x[6][0], x[7][0], x[8][0], x[9][0], x[10][0], x[11][0], i))
                xf = x - np.dot(np.linalg.solve(jacobian, np.identity(jacobian.shape[0])), phiEval)
                x = xf
                rest = np.linalg.norm(phiEval)

            v_1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -self.alpha2inicial*i-self.omega2inicial]
            vi = np.dot(-np.linalg.solve(jacobian, np.identity(jacobian.shape[0])), np.reshape(v_1, (len(x), -1)))
            jacobina_point = np.array(jaco_point(x[0][0], x[1][0], x[2][0], x[3][0], x[4][0], x[5][0], x[6][0], x[7][0], x[8][0], x[9][0], x[10][0], x[11][0], i))
    
            a_1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -self.alpha2inicial]
            ai = np.dot(np.linalg.solve(jacobian, np.identity(jacobian.shape[0])),(np.dot(-jacobina_point,vi)-np.reshape(a_1, (len(x), -1))))
            ti.append(float(i))

            br1_x = float(self.I1*cos(xf[3][0]))
            br1_y = float(self.I1*sin(xf[3][0]))
            self.barra1.setData([0, br1_x], [0, br1_y])
            br2_x = float(br1_x+self.I3*cos(xf[6][0]))
            br2_y = float(br1_y+self.I3*sin(xf[6][0]))
            self.barra2.setData([br1_x, br2_x], [br1_y, br2_y])
            br3_x = float(self.I1*cos(xf[9][0]))
            br3_y = float(self.I1*sin(xf[9][0]))
            self.barra3.setData([br2_x, br3_x], [br2_y, br3_y])
            self.barra4.setData([br3_x, 0], [br3_y, 0])
            # # graficar la posicion
            # self.posiciones_1.append(xf[0][0])
            # self.posiciones_2.append(xf[1][0])
            # self.posiciones_3.append(xf[2][0])
            # self.plot_posicion_1.setData(ti, self.posiciones_1)
            # self.plot_posicion_2.setData(ti, self.posiciones_2)
            # self.plot_posicion_3.setData(ti, self.posiciones_3)
            # # # graficar la velocidad
            # self.velocidad_1.append(float(vi[0][0]))
            # self.velocidad_2.append(float(vi[1][0]))
            # self.velocidad_3.append(float(vi[2][0]))
            # self.plot_velocidad_1.setData(ti, self.velocidad_1)
            # self.plot_velocidad_2.setData(ti, self.velocidad_2)
            # self.plot_velocidad_3.setData(ti, self.velocidad_3)
            # # # graficar la aceleracion
            # self.aceleracion_1.append(float(ai[0][0]))
            # self.aceleracion_2.append(float(ai[1][0]))
            # self.aceleracion_3.append(float(ai[2][0]))
            # self.plot_aceleracion_1.setData(ti, self.aceleracion_1)
            # self.plot_aceleracion_2.setData(ti, self.aceleracion_2)
            # self.plot_aceleracion_3.setData(ti, self.aceleracion_3)
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