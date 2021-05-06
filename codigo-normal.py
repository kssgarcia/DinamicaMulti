from pyqtgraph.Qt import QtGui, QtCore, QtWidgets
import numpy as np
import pyqtgraph as pg
from sympy import symbols, evalf, diff, sin, cos, Matrix

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
        self.xA = 0
        self.yA = 0
        self.xB = 5.908
        self.yB = 1.0418
        self.phi2inicial = phi2inicial
        self.omega2inicial = omega2inicial
        self.alpha2inicial = alpha2inicial
        cont = 0
        x=[.4, 1, 2.2, 2]
        step = 0.01
        self.time_simul = time_simul
        x1, y1, x2, y2, t = symbols('x1 y1 x2 y2 t')
        w_2, w_3, w_4 = symbols('w_2 w_3 w_4')
        self.w = np.array([[w_2], [w_3], [w_4]])
        q = np.array([[x1], [y1], [x2], [y2]])

        phi = [[ pow((x1-self.xA),2) + pow((y1-self.yA),2) - pow(self.I2,2)],
            [pow((x2-x1),2) + pow((y2-y1),2) - pow(self.I3,2)],
            [pow((x2-self.xB),2) + pow((y2-self.yB),2) - pow(self.I4,2)],
            [x1 - self.xA - self.I2*cos((0.5*alpha2inicial)*pow(t,2) + omega2inicial*t + phi2inicial)]]


        jaco = np.array(self.derivate(phi, q, None, 0))
        jaco_point = np.array(self.derivateMatrix(jaco, q, None, 0))


        V = []
        P = []
        A = []
        ti = []
        x = np.reshape(x, (len(x), -1))

        for i in np.arange(0, time_simul, step):
            float(i)
            cont += 1
            rest = 10
            while rest > 0.00001:
                phiEval = Matrix(phi).subs(dict(x1=x[0][0], y1=x[1][0], x2=x[2][0], y2=x[3][0], t=i))
                jacobian = Matrix(jaco).subs(dict(x1=x[0][0], y1=x[1][0], x2=x[2][0], y2=x[3][0], t=i))
                phiSys = np.array(phiEval).astype(np.float64)
                jacobianEval = np.array(jacobian).astype(np.float64)
                xf = x - np.dot(np.linalg.inv(jacobianEval), phiSys)
                x = xf
                rest = np.linalg.norm(phiSys)
            P.append(xf)
            v_1 = [0, 0, 0, self.I2*(self.alpha2inicial*i+self.omega2inicial)*sin(0.5*pow(self.alpha2inicial*i,2) + self.omega2inicial*i + self.phi2inicial)]
            vi = np.dot(-np.linalg.inv(jacobianEval), np.reshape(v_1, (len(x), -1)))
            V.append(vi)
            #.subs(dict(x1=x[0][0], x2=x[1][0], x3=x[2][0], x4=x[3][0], w_2=vi[0][0], w_3=vi[1][0], w_4=vi[2][0]))
            jacobina_point = Matrix(jaco_point)
            a_1 = [0, 0, 0, ((self.I2*self.alpha2inicial*sin(0.5*pow(self.alpha2inicial*i,2) + self.omega2inicial*i + self.phi2inicial)) + self.I2*pow((self.alpha2inicial*i+self.omega2inicial),2)*cos(0.5*pow((self.alpha2inicial*i),2) + self.omega2inicial*i + self.phi2inicial))]
            ai = np.dot(-np.linalg.inv(jacobianEval),((jacobina_point*vi)+np.reshape(a_1, (len(x), -1))))
            A.append(ai)


            self.barra1.setData([self.xA, xf[0][0]], [self.yA, xf[1][0]])
            self.barra2.setData([xf[0][0], xf[2][0]], [xf[1][0], xf[3][0]])
            self.barra3.setData([xf[2][0], self.xB], [xf[3][0], self.yB])
            self.barra4.setData([self.xB, self.xA], [self.yB, self.yA])
            if i >= time_simul:
                break
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
        object_1 =  CierreVectorial()
        object_1.SolucionVectorial(6, 2, 4, 5, 0, 1, 1, 1.5)
        QtGui.QApplication.instance().exec_()
