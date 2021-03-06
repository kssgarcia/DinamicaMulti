from pyqtgraph.Qt import QtGui, QtCore, QtWidgets
import numpy as np
import pyqtgraph as pg
from sympy import symbols, evalf, diff, sin, cos, Matrix, lambdify
import time

class  CoordenadasNaturales:
    def __init__(self,win1, win2, win3, win4, win5, app, I1, I2, I3, I4, phi_1, phi2inicial, omega2inicial, alpha2inicial, time_simul):
        win1.resize(1200, 700)
        win1.setTitle('simulacion')
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
        self.xA = 0
        self.yA = 0
        self.xB = self.I1 * np.cos(phi_1)
        self.yB = self.I1 * np.sin(phi_1)
        self.phi2inicial = phi2inicial
        self.omega2inicial = omega2inicial
        self.alpha2inicial = alpha2inicial
        self.time_simul = time_simul
        self.m1 = 1.2
        self.m2 = 0.4
        self.m3 = 0.8
        self.m4 = 1
        self.M1 = np.array([[0.333*self.I1, 1.667*self.I1],
                                        [1.6667*self.I1, 0.333*self.I1]])
        self.M2 = np.array([[0.333*self.I2, 1.667*self.I2],
                                        [1.6667*self.I2, 0.333*self.I2]])
        self.M3 = np.array([[0.333*self.I3, 1.667*self.I3],
                                        [1.6667*self.I3, 0.333*self.I3]])
        self.M4 = np.array([[0.333*self.I4, 1.667*self.I4],
                                        [1.6667*self.I4, 0.333*self.I4]])    

        self.M_x1 = np.concatenate(((self.m1/self.I1)*self.M1, (self.m2/self.I2)*self.M2), axis=1)
        self.M_x2 = np.concatenate(((self.m3/self.I3)*self.M3, (self.m4/self.I4)*self.M4), axis=1)
        self.M_completa = np.concatenate((self.M_x1, self.M_x2), axis=0)                                    
        #plot posicion
        win2.resize(1200, 700)
        win2.setTitle('posicion | azul=X2 verde=Y2 rojo=X3 negro=Y3')
        self.plot_posicion_1 = win2.plot(pen=pg.mkPen('b', width=3))
        self.plot_posicion_2 = win2.plot(pen=pg.mkPen('g', width=3))
        self.plot_posicion_3 = win2.plot(pen=pg.mkPen('r', width=3))
        self.plot_posicion_4 = win2.plot(pen=pg.mkPen('k', width=3))
        self.posiciones_1 = []
        self.posiciones_2 = []
        self.posiciones_3 = []
        self.posiciones_4 = []
        #plot velocidad
        win3.resize(1200, 700)
        win3.setTitle('velocidad | azul=X2 verde=Y2 rojo=X3 negro=Y3')
        self.plot_velocidad_1 = win3.plot(pen=pg.mkPen('b', width=3))
        self.plot_velocidad_2 = win3.plot(pen=pg.mkPen('g', width=3))
        self.plot_velocidad_3 = win3.plot(pen=pg.mkPen('r', width=3))
        self.plot_velocidad_4 = win3.plot(pen=pg.mkPen('k', width=3))
        self.velocidad_1 = []
        self.velocidad_2 = []
        self.velocidad_3 = []
        self.velocidad_4 = []
        #plot aceleracion
        win4.resize(1200, 700)
        win4.setTitle('aceleracion | azul=X2 verde=Y2 rojo=X3 negro=Y3')
        self.plot_aceleracion_1 = win4.plot(pen=pg.mkPen('b', width=3))
        self.plot_aceleracion_2 = win4.plot(pen=pg.mkPen('g', width=3))
        self.plot_aceleracion_3 = win4.plot(pen=pg.mkPen('r', width=3))
        self.plot_aceleracion_4 = win4.plot(pen=pg.mkPen('k', width=3))
        self.aceleracion_1 = []
        self.aceleracion_2 = []
        self.aceleracion_3 = []
        self.aceleracion_4 = []
        #plot fuerza
        win5.resize(1200, 700)
        win5.setTitle('fuerza | azul=X2 verde=Y2 rojo=X3 negro=Y3')
        self.plot_fuerza_1 = win5.plot(pen=pg.mkPen('b', width=3))
        self.plot_fuerza_2 = win5.plot(pen=pg.mkPen('g', width=3))
        self.plot_fuerza_3 = win5.plot(pen=pg.mkPen('r', width=3))
        self.plot_fuerza_4 = win5.plot(pen=pg.mkPen('k', width=3))
        self.fuerza_1 = []
        self.fuerza_2 = []
        self.fuerza_3 = []
        self.fuerza_4 = []

    def SolucionNaturales(self):
        cont = 0
        x=[0, 0, .4, 1, 2.2, 2, 5, 1]
        step = 0.01
        x0, y0, x1, y1, x2, y2, x3, y3, t = symbols('x0 y0 x1 y1 x2 y2 x3 y3 t')
        q = np.array([[x0], [y0],[x1], [y1], [x2], [y2], [x3], [y3]])

        phi = np.array([[ pow((x1-x0),2) + pow((y1-y0),2) - pow(self.I2,2)],
            [pow((x2-x1),2) + pow((y2-y1),2) - pow(self.I3,2)],
            [pow((x3-x2),2) + pow((y3-y2),2) - pow(self.I4,2)],
            [x0 - self.xA],
            [y0 - self.yA],
            [x3 - self.xB],
            [y3 - self.yB],
            [x1 - self.xA - self.I2*cos((0.5*self.alpha2inicial)*np.power(t,2) + self.omega2inicial*t + self.phi2inicial)]])
        jaco = np.array(self.derivate(phi, q, None, 0))
        jaco_point = np.array(self.derivateMatrix(jaco, q, None, 0))
        ti = []
        x = np.reshape(x, (len(x), -1))

        phi = lambdify([x0, y0, x1, y1, x2, y2, x3, y3, t], phi)
        jaco = lambdify([x0, y0, x1, y1, x2, y2, x3, y3, t], jaco)
        jaco_point = lambdify([x0, y0, x1, y1, x2, y2, x3, y3, t], jaco_point)
        for i in np.arange(0, self.time_simul, step):
            float(i)
            cont += 1
            rest = 10
            while rest > 0.00001:
                phiEval = np.array(phi(x[0][0], x[1][0], x[2][0], x[3][0], x[4][0], x[5][0], x[6][0], x[7][0], i))
                jacobian = np.array(jaco(x[0][0], x[1][0], x[2][0], x[3][0], x[4][0], x[5][0], x[6][0], x[7][0], i))
                xf = x - np.dot(np.linalg.inv(jacobian), phiEval)
                x = xf
                rest = np.linalg.norm(phiEval)

            v_1 = np.array([0, 0, 0, 0, 0, 0, 0, self.I2*(self.alpha2inicial*i+self.omega2inicial)*sin(0.5*np.power(self.alpha2inicial*i,2) + self.omega2inicial*i + self.phi2inicial)])
            vi = np.dot(-np.linalg.inv(jacobian), np.reshape(v_1, (len(x), -1)))

            jacobina_point = np.array(jaco(x[0][0], x[1][0], x[2][0], x[3][0], x[4][0], x[5][0], x[6][0], x[7][0], i))

            a_1 = np.array([0, 0, 0, 0, 0, 0, 0, ((self.I2*self.alpha2inicial*sin(0.5*np.power(self.alpha2inicial*i,2) + self.omega2inicial*i + self.phi2inicial)) + self.I2*np.power((self.alpha2inicial*i+self.omega2inicial),2)*cos(0.5*pow((self.alpha2inicial*i),2) + self.omega2inicial*i + self.phi2inicial))])
            ai = np.dot(-np.linalg.inv(jacobian),(np.dot(-jacobina_point,vi)+np.reshape(a_1, (len(x), -1))))
            ti.append(float(i))

            self.barra1.setData([self.xA, xf[2][0]], [self.yA, xf[3][0]])
            self.barra2.setData([xf[2][0], xf[4][0]], [xf[3][0], xf[5][0]])
            self.barra3.setData([xf[4][0], self.xB], [xf[5][0], self.yB])
            self.barra4.setData([self.xB, self.xA], [self.yB, self.yA])

            # graficar la posicion
            self.posiciones_1.append(xf[2][0])
            self.posiciones_2.append(xf[3][0])
            self.posiciones_3.append(xf[4][0])
            self.posiciones_4.append(xf[5][0])
            self.plot_posicion_1.setData(ti, self.posiciones_1)
            self.plot_posicion_2.setData(ti, self.posiciones_2)
            self.plot_posicion_3.setData(ti, self.posiciones_3)
            self.plot_posicion_4.setData(ti, self.posiciones_4)
            # graficar la velocidad
            self.velocidad_1.append(float(vi[2][0]))
            self.velocidad_2.append(float(vi[3][0]))
            self.velocidad_3.append(float(vi[4][0]))
            self.velocidad_4.append(float(vi[5][0]))
            self.plot_velocidad_1.setData(ti, self.velocidad_1)
            self.plot_velocidad_2.setData(ti, self.velocidad_2)
            self.plot_velocidad_3.setData(ti, self.velocidad_3)
            self.plot_velocidad_4.setData(ti, self.velocidad_4)
            # graficar la aceleracion
            self.aceleracion_1.append(float(ai[2][0]))
            self.aceleracion_2.append(float(ai[3][0]))
            self.aceleracion_3.append(float(ai[4][0]))
            self.aceleracion_4.append(float(ai[5][0]))
            self.plot_aceleracion_1.setData(ti, self.aceleracion_1)
            self.plot_aceleracion_2.setData(ti, self.aceleracion_2)
            self.plot_aceleracion_3.setData(ti, self.aceleracion_3)
            self.plot_aceleracion_4.setData(ti, self.aceleracion_4)
            # # graficar la fuerza
            # self.fuerza_1.append(float(ai[2][0]))
            # self.fuerza_2.append(float(ai[3][0]))
            # self.fuerza_3.append(float(ai[4][0]))
            # self.fuerza_4.append(float(ai[5][0]))
            # self.plot_fuerza_1.setData(ti, self.fuerza_1)
            # self.plot_fuerza_2.setData(ti, self.fuerza_2)
            # self.plot_fuerza_3.setData(ti, self.fuerza_3)
            # self.plot_fuerza_4.setData(ti, self.fuerza_4)

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

