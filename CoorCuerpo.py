from pyqtgraph.Qt import QtGui, QtCore, QtWidgets
import numpy as np
import pyqtgraph as pg
from sympy import symbols, evalf, diff, sin, cos, Matrix, lambdify


class  CoordenadasCuerpo:
    def __init__(self,win, app, I1, I2, I3, I4, phi_1, phi2inicial, omega2inicial, alpha2inicial, time_simul):
        win[0].resize(1200, 700)
        win[0].setTitle('simulacion')
        self.app = app
        self.barra1 = win[0].plot(pen=pg.mkPen('b', width=3), symbolPen ='g',brush=pg.mkBrush(30, 255, 35, 255))
        self.barra2 = win[0].plot(pen=pg.mkPen('g', width=3), symbolPen ='g')
        self.barra3 = win[0].plot(pen=pg.mkPen('r', width=3), symbolPen ='g')
        self.barra4 = win[0].plot(pen=pg.mkPen(color=(128,128,128), width=3))
        self.barra1.setBrush([11, 12])
        win[0].setXRange(-2.5, 10, padding=0)
        win[0].setYRange(-2.5, 10, padding=0)
        #entradas
        self.I1 = I1
        self.I2 = I2
        self.I3 = I3
        self.I4 = I4
        self.phi_1 = phi_1
        self.phi2inicial = phi2inicial
        self.omega2inicial = omega2inicial
        self.alpha2inicial = alpha2inicial
        self.time_simul = time_simul
        # propiedades inerciales
        self.m1 = 1.2
        self.m2 = 0.4
        self.m3 = 0.8
        self.m4 = 1
        self.Iner1 = (1/12)*self.m1*pow(self.I1, 2)
        self.Iner2 = (1/12)*self.m2*pow(self.I2, 2)
        self.Iner3 = (1/12)*self.m3*pow(self.I3, 2)
        self.Iner4 = (1/12)*self.m4*pow(self.I4, 2)
        self.inerciales = np.array([self.m1, self.m1, self.Iner1, self.m2, self.m2, self.Iner2, self.m3, self.m3, self.Iner3, self.m4, self.m4, self.Iner4])
        self.matriz_inercial = np.multiply(np.identity(12),self.inerciales)
        self.fuerza = np.array([[0], [-self.m1*9.81], [0], [0], [-self.m2*9.81], [0], [0], [-self.m3*9.81], [0], [0], [-self.m4*9.81], [0]])
        #plot posicion
        win[1].resize(1200, 700)
        win[1].setTitle('posicion')
        self.plot_posicion_1 = win[1].plot(pen=pg.mkPen('b', width=3))
        self.plot_posicion_2 = win[1].plot(pen=pg.mkPen('g', width=3))
        self.plot_posicion_3 = win[1].plot(pen=pg.mkPen('r', width=3))
        self.posiciones_1 = []
        self.posiciones_2 = []
        self.posiciones_3 = []
        #plot velocidad a
        win[2].resize(599, 400)
        win[2].setTitle('velocidad barra 2 | azul=X verde=Y rojo=Phi')
        self.plot_velocidad_1a = win[2].plot(pen=pg.mkPen('b', width=3))
        self.plot_velocidad_2a = win[2].plot(pen=pg.mkPen('g', width=3))
        self.plot_velocidad_3a = win[2].plot(pen=pg.mkPen('r', width=3))
        self.velocidad_1a = []
        self.velocidad_2a = []
        self.velocidad_3a = []
        #plot velocidad b
        win[3].resize(599, 400)
        win[3].setTitle('velocidad barra 3 | azul=X verde=Y rojo=Phi')
        self.plot_velocidad_1b = win[3].plot(pen=pg.mkPen('b', width=3))
        self.plot_velocidad_2b = win[3].plot(pen=pg.mkPen('g', width=3))
        self.plot_velocidad_3b = win[3].plot(pen=pg.mkPen('r', width=3))
        self.velocidad_1b = []
        self.velocidad_2b = []
        self.velocidad_3b = []
        #plot velocidad c
        win[4].resize(599, 400)
        win[4].setTitle('velocidad barra 4 | azul=X verde=Y rojo=Phi')
        self.plot_velocidad_1c = win[4].plot(pen=pg.mkPen('b', width=3))
        self.plot_velocidad_2c = win[4].plot(pen=pg.mkPen('g', width=3))
        self.plot_velocidad_3c = win[4].plot(pen=pg.mkPen('r', width=3))
        self.velocidad_1c = []
        self.velocidad_2c = []
        self.velocidad_3c = []
        #plot aceleracion a
        win[5].resize(599, 400)
        win[5].setTitle('aceleracion barra 2 | azul=X verde=Y rojo=Phi')
        self.plot_aceleracion_1a = win[5].plot(pen=pg.mkPen('b', width=3))
        self.plot_aceleracion_2a = win[5].plot(pen=pg.mkPen('g', width=3))
        self.plot_aceleracion_3a = win[5].plot(pen=pg.mkPen('r', width=3))
        self.aceleracion_1a = []
        self.aceleracion_2a = []
        self.aceleracion_3a = []
        #plot aceleracion b
        win[6].resize(599, 400)
        win[6].setTitle('aceleracion barra 3 | azul=X verde=Y rojo=Phi')
        self.plot_aceleracion_1b = win[6].plot(pen=pg.mkPen('b', width=3))
        self.plot_aceleracion_2b = win[6].plot(pen=pg.mkPen('g', width=3))
        self.plot_aceleracion_3b = win[6].plot(pen=pg.mkPen('r', width=3))
        self.aceleracion_1b = []
        self.aceleracion_2b = []
        self.aceleracion_3b = []
        #plot aceleracion c
        win[7].resize(599, 400)
        win[7].setTitle('aceleracion barra 4 | azul=X verde=Y rojo=Phi')
        self.plot_aceleracion_1c = win[7].plot(pen=pg.mkPen('b', width=3))
        self.plot_aceleracion_2c = win[7].plot(pen=pg.mkPen('g', width=3))
        self.plot_aceleracion_3c = win[7].plot(pen=pg.mkPen('r', width=3))
        self.aceleracion_1c = []
        self.aceleracion_2c = []
        self.aceleracion_3c = []
        #plot fuerza a
        win[8].resize(599, 400)
        win[8].setTitle('fuerza barra 2 | azul=X verde=Y rojo=Phi')
        self.plot_fuerza_1a = win[8].plot(pen=pg.mkPen('b', width=3))
        self.plot_fuerza_2a = win[8].plot(pen=pg.mkPen('g', width=3))
        self.plot_fuerza_3a = win[8].plot(pen=pg.mkPen('r', width=3))
        self.fuerza_1a = []
        self.fuerza_2a = []
        self.fuerza_3a = []
        #plot fuerza b
        win[9].resize(599, 400)
        win[9].setTitle('fuerza barra 3 | azul=X verde=Y rojo=Phi')
        self.plot_fuerza_1b = win[9].plot(pen=pg.mkPen('b', width=3))
        self.plot_fuerza_2b = win[9].plot(pen=pg.mkPen('g', width=3))
        self.plot_fuerza_3b = win[9].plot(pen=pg.mkPen('r', width=3))
        self.fuerza_1b = []
        self.fuerza_2b = []
        self.fuerza_3b = []
        #plot fuerza c
        win[10].resize(599, 400)
        win[10].setTitle('fuerza barra 4 | azul=X verde=Y rojo=Phi')
        self.plot_fuerza_1c = win[10].plot(pen=pg.mkPen('b', width=3))
        self.plot_fuerza_2c = win[10].plot(pen=pg.mkPen('g', width=3))
        self.plot_fuerza_3c = win[10].plot(pen=pg.mkPen('r', width=3))
        self.fuerza_1c = []
        self.fuerza_2c = []
        self.fuerza_3c = []

    def SolucionCuerpo(self):
        cont = 0
        x=[0, 3, 0, 1, 0, 0, 2.4, 1.9, 1.3, 4.4, 1.9, 2.2]
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
                phiEval = np.array(phi(x[0][0], x[1][0], self.phi_1, x[3][0], x[4][0], x[5][0], x[6][0], x[7][0], x[8][0], x[9][0], x[10][0], x[11][0], i))
                jacobian = np.array(jaco(x[0][0], x[1][0], self.phi_1, x[3][0], x[4][0], x[5][0], x[6][0], x[7][0], x[8][0], x[9][0], x[10][0], x[11][0], i))
                xf = x - np.dot(np.linalg.solve(jacobian, np.identity(jacobian.shape[0])), phiEval)
                x = xf
                rest = np.linalg.norm(phiEval)

            v_1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -self.alpha2inicial*i-self.omega2inicial]
            vi = np.dot(-np.linalg.solve(jacobian, np.identity(jacobian.shape[0])), np.reshape(v_1, (len(x), -1)))
            jacobina_point = np.array(jaco_point(x[0][0], x[1][0], self.phi_1, x[3][0], x[4][0], x[5][0], x[6][0], x[7][0], x[8][0], x[9][0], x[10][0], x[11][0], i))
    
            a_1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -self.alpha2inicial]
            ai = np.dot(np.linalg.solve(jacobian, np.identity(jacobian.shape[0])),(np.dot(-jacobina_point,vi)-np.reshape(a_1, (len(x), -1))))
            ti.append(float(i))
            lambi = np.dot(np.transpose(np.linalg.solve(jacobian, np.identity(jacobian.shape[0]))), (np.dot(self.matriz_inercial, ai) - self.fuerza))
            br1_x = float(self.I2*cos(xf[5][0]))
            br1_y = float(self.I2*sin(xf[5][0]))
            self.barra1.setData([0, br1_x], [0, br1_y])
            br2_x = float(br1_x+self.I3*cos(xf[8][0]))
            br2_y = float(br1_y+self.I3*sin(xf[8][0]))
            self.barra2.setData([br1_x, br2_x], [br1_y, br2_y])
            br4_x = float(self.I1*cos(xf[2][0]))
            br4_y = float(self.I1*sin(xf[2][0]))
            self.barra3.setData([br2_x, br4_x], [br2_y, br4_y])
            self.barra4.setData([br4_x, 0], [br4_y, 0])
            # graficar la posicion
            self.posiciones_1.append(xf[5][0])
            self.posiciones_2.append(xf[8][0])
            self.posiciones_3.append(xf[11][0])
            self.plot_posicion_1.setData(ti, self.posiciones_1)
            self.plot_posicion_2.setData(ti, self.posiciones_2)
            self.plot_posicion_3.setData(ti, self.posiciones_3)
            # graficar la velocidad a
            self.velocidad_1a.append(float(vi[3][0]))
            self.velocidad_2a.append(float(vi[4][0]))
            self.velocidad_3a.append(float(vi[5][0]))
            self.plot_velocidad_1a.setData(ti, self.velocidad_1a)
            self.plot_velocidad_2a.setData(ti, self.velocidad_2a)
            self.plot_velocidad_3a.setData(ti, self.velocidad_3a)
            # graficar la velocidad b
            self.velocidad_1b.append(float(vi[6][0]))
            self.velocidad_2b.append(float(vi[7][0]))
            self.velocidad_3b.append(float(vi[8][0]))
            self.plot_velocidad_1b.setData(ti, self.velocidad_1b)
            self.plot_velocidad_2b.setData(ti, self.velocidad_2b)
            self.plot_velocidad_3b.setData(ti, self.velocidad_3b)
            # graficar la velocidad c
            self.velocidad_1c.append(float(vi[9][0]))
            self.velocidad_2c.append(float(vi[10][0]))
            self.velocidad_3c.append(float(vi[11][0]))
            self.plot_velocidad_1c.setData(ti, self.velocidad_1c)
            self.plot_velocidad_2c.setData(ti, self.velocidad_2c)
            self.plot_velocidad_3c.setData(ti, self.velocidad_3c)
            # graficar la aceleracion a
            self.aceleracion_1a.append(float(ai[3][0]))
            self.aceleracion_2a.append(float(ai[4][0]))
            self.aceleracion_3a.append(float(ai[5][0]))
            self.plot_aceleracion_1a.setData(ti, self.aceleracion_1a)
            self.plot_aceleracion_2a.setData(ti, self.aceleracion_2a)
            self.plot_aceleracion_3a.setData(ti, self.aceleracion_3a)
            # graficar la aceleracion b
            self.aceleracion_1b.append(float(ai[6][0]))
            self.aceleracion_2b.append(float(ai[7][0]))
            self.aceleracion_3b.append(float(ai[8][0]))
            self.plot_aceleracion_1b.setData(ti, self.aceleracion_1b)
            self.plot_aceleracion_2b.setData(ti, self.aceleracion_2b)
            self.plot_aceleracion_3b.setData(ti, self.aceleracion_3b)
            # graficar la aceleracion c
            self.aceleracion_1c.append(float(ai[9][0]))
            self.aceleracion_2c.append(float(ai[10][0]))
            self.aceleracion_3c.append(float(ai[11][0]))
            self.plot_aceleracion_1c.setData(ti, self.aceleracion_1c)
            self.plot_aceleracion_2c.setData(ti, self.aceleracion_2c)
            self.plot_aceleracion_3c.setData(ti, self.aceleracion_3c)
            # graficar la fuerza a
            self.fuerza_1a.append(float(lambi[3][0]))
            self.fuerza_2a.append(float(lambi[4][0]))
            self.fuerza_3a.append(float(lambi[5][0]))
            self.plot_fuerza_1a.setData(ti, self.fuerza_1a)
            self.plot_fuerza_2a.setData(ti, self.fuerza_2a)
            self.plot_fuerza_3a.setData(ti, self.fuerza_3a)
            # graficar la fuerza b
            self.fuerza_1b.append(float(lambi[6][0]))
            self.fuerza_2b.append(float(lambi[7][0]))
            self.fuerza_3b.append(float(lambi[8][0]))
            self.plot_fuerza_1b.setData(ti, self.fuerza_1b)
            self.plot_fuerza_2b.setData(ti, self.fuerza_2b)
            self.plot_fuerza_3b.setData(ti, self.fuerza_3b)
            # graficar la fuerza c
            self.fuerza_1c.append(float(lambi[9][0]))
            self.fuerza_2c.append(float(lambi[10][0]))
            self.fuerza_3c.append(float(lambi[11][0]))
            self.plot_fuerza_1c.setData(ti, self.fuerza_1c)
            self.plot_fuerza_2c.setData(ti, self.fuerza_2c)
            self.plot_fuerza_3c.setData(ti, self.fuerza_3c)

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


