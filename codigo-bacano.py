from pyqtgraph.Qt import QtGui, QtCore, QtWidgets
import numpy as np
import pyqtgraph as pg
from sympy import symbols, evalf, diff, sin, cos, Matrix, lambdify
import time
import numba

class  CierreVectorial:


    def SolucionVectorial(self, I1, I2, I3, I4, phi2inicial, omega2inicial, alpha2inicial, time_simul):
        app = QtGui.QApplication([])
        win = pg.GraphicsWindow(title="My plotting examples")
        win.resize(1000,600)
        win.setWindowTitle('Cierre Vectorial')
        p1 = win.addPlot(title="plot1")

        self.barra1 = p1.plot(pen='y')
        self.barra2 = p1.plot(pen='r')
        self.barra3 = p1.plot(pen='y')
        self.barra4 = p1.plot(pen='r')

        self.I1 = I1
        self.I2 = I2
        self.I3 = I3
        self.I4 = I4
        self.phi2inicial = phi2inicial
        self.omega2inicial = omega2inicial
        self.alpha2inicial = alpha2inicial
        self.time_simul = time_simul

        cont = 0
        x=[3, 0, 0, 1, 0, 0, 2.4, 1.9, 1.3, 4.4, 1.9, 2.2]
        step = 0.01
        x1, y1, phi1, x2, y2, phi2, x3, y3, phi3, x4, y4, phi4, t = symbols('x1 y1 phi1 x2 y2 phi2 x3 y3 phi3 x4 y4 phi4 t')
        w_2, w_3, w_4 = symbols('w_2 w_3 w_4')
        self.w = np.array([[w_2], [w_3], [w_4]])
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
        A = []
        V = []
        P = []
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
            # V.append(vi)
            P.append(xf)
            jacobina_point = np.array(jaco_point(x[0][0], x[1][0], x[2][0], x[3][0], x[4][0], x[5][0], x[6][0], x[7][0], x[8][0], x[9][0], x[10][0], x[11][0], i))
            
            a_1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -self.alpha2inicial]
            ai = np.dot(np.linalg.solve(jacobian, np.identity(jacobian.shape[0])),(np.dot(-jacobina_point,vi)-np.reshape(a_1, (len(x), -1))))
            A.append(ai)
            V.append(vi)
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

            app.processEvents()


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
#------------------------------------------------------------------------

if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        start = time.time()
        object_1 =  CierreVectorial()
        object_1.SolucionVectorial(6, 2, 4, 5, 0, 1, 1, 2.5)
        print(time.time() - start)
        QtGui.QApplication.instance().exec_()
