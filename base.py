from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
import pyqtgraph as pg
import get_elements
import CierreVec
import Naturales

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # crear la ventana y el font y css
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1900, 1200)
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        # font.setPointSize(.5)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("font: 8pt \"MS PGothic\";\n"
                        "background-color: rgb(54, 79, 107);\n"
                        "font-size: 12px;\n"
                        "\n"
                        "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QPushButton {\n"
                                        "background: rgb(156, 29, 231);\n"
                                        "border: none;\n"
                                        "border-radius: 20px;\n"
                                        "color: white;\n"
                                        "font-weight: bold;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "background: rgb(63, 93, 125);\n"
                                        "}\n"
                                        "\n"
                                        "\n"
                                        "\n"
                                        "\n"
                                        "")
        self.centralwidget.setObjectName("centralwidget")
        # crea las Tab generales
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 40, 1900, 1000))
        self.tabWidget.setStyleSheet("QTabWidget::pane {\n"
                                        "    border: none;\n"
                                        "}\n"
                                        "\n"
                                        "QTabWidget::tab-bar:top {\n"
                                        "    top: 5px;\n"
                                        "}\n"
                                        "QTabWidget::tab-bar:bottom {\n"
                                        "    bottom: 1px;\n"
                                        "}\n"
                                        "\n"
                                        "QTabWidget::tab-bar:left {\n"
                                        "    right: 1px;\n"
                                        "\n"
                                        "}\n"
                                        "\n"
                                        "QTabWidget::tab-bar:right {\n"
                                        "    left: 1px;\n"
                                        "}\n"
                                        "\n"
                                        "QTabBar::tab {\n"
                                        "    border: none;\n"
                                        "    color: white;\n"
                                        "    margin: 4px;\n"
                                        "    border-top-right-radius: 14px; \n"
                                        "    border-top-left-radius: 14px;\n"
                                        "}\n"
                                        "\n"
                                        "QTabBar::tab:selected {\n"
                                        "    background : rgb(156, 29, 231);\n"
                                        "    color: white;\n"
                                        "    font-size: 15px;\n"
                                        "    font-size: 15px;\n"
                                        "    width: 170px;\n"
                                        "    height: 30px;\n"
                                        "}\n"
                                        "\n"
                                        "QTabBar::tab:!selected {\n"
                                        "background: rgb(43, 63, 85);\n"
                                        "border: none;\n"
                                        "color: white;\n"
                                        "font-size: 15px;\n"
                                        "width: 170px;\n"
                                        "height: 30px;\n"
                                        "}\n"
                                        "\n"
                                        "QTabBar::tab:!selected:hover {\n"
                                        "    background: rgb(63, 93, 125);\n"
                                        "}\n"
                                        "\n"
                                        "QTabBar::tab:top:!selected {\n"
                                        "    margin-top: 3px;\n"
                                        "}\n"
                                        "\n"
                                        "QTabBar::tab:bottom:!selected {\n"
                                        "    margin-bottom: 3px;\n"
                                        "}\n"
                                        "\n"
                                        "QTabBar::tab:top, QTabBar::tab:bottom {\n"
                                        "    min-width: 8ex;\n"
                                        "    margin-right: -1px;\n"
                                        "    padding: 5px 10px 5px 10px;\n"
                                        "}\n"
                                        "\n"
                                        "QTabBar::tab:top:selected {\n"
                                        "    border-bottom-color: none;\n"
                                        "}\n"
                                        "\n"
                                        "QTabBar::tab:bottom:selected {\n"
                                        "    border-top-color: none;\n"
                                        "}\n"
                                        "\n"
                                        "QTabBar::tab:top:last, QTabBar::tab:bottom:last,\n"
                                        "QTabBar::tab:top:only-one, QTabBar::tab:bottom:only-one {\n"
                                        "    margin-right: 0;\n"
                                        "}\n"
                                        "\n"
                                        "QTabBar::tab:left:!selected {\n"
                                        "    margin-right: 3px;\n"
                                        "}\n"
                                        "\n"
                                        "QTabBar::tab:right:!selected {\n"
                                        "    margin-left: 3px;\n"
                                        "}\n"
                                        "\n"
                                        "QTabBar::tab:left, QTabBar::tab:right {\n"
                                        "    min-height: 8ex;\n"
                                        "    margin-bottom: -1px;\n"
                                        "    padding: 10px 5px 10px 5px;\n"
                                        "}\n"
                                        "\n"
                                        "\n"
                                        "\n"
                                        "QTabBar::tab:left:last, QTabBar::tab:right:last,\n"
                                        "QTabBar::tab:left:only-one, QTabBar::tab:right:only-one {\n"
                                        "    margin-bottom: 0;\n"
                                        "}")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        # crea los demas tabs generales
        self.tab_cnaturales = QtWidgets.QWidget()
        self.tab_cnaturales.setObjectName("tab_cnaturales")
        self.tabWidget.addTab(self.tab_cnaturales, "")
        self.tab_ccuerpo = QtWidgets.QWidget()
        self.tab_ccuerpo.setObjectName("tab_ccuerpo")
        self.tabWidget.addTab(self.tab_ccuerpo, "")
        # hace el set de la ventada principal
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1032, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        #crea el layout de los tabs generales
        self.layout_naturales()
        self.layout_vectorial()
        # crea todos los componentes de la venta de cierre vectorial
        self.CreateVectorial()
        self.CreateNaturales()
        # crea los textos de los tabs generales y configura los textos de la ventana principal
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_vectorial.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Cierre Vectorial"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_cnaturales), _translate("MainWindow", "Coordenadas Naturales"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_ccuerpo), _translate("MainWindow", "Coordenadas de Cuerpo"))
        # self.exit.setText(_translate("MainWindow", "Salir"))
        self.tabWidget_vectorial.setTabText(self.tabWidget_vectorial.indexOf(self.tab_simulacion), _translate("MainWindow", " Simulación"))
        self.tabWidget_vectorial.setTabText(self.tabWidget_vectorial.indexOf(self.tab_posicion), _translate("MainWindow", "Posición "))
        self.tabWidget_vectorial.setTabText(self.tabWidget_vectorial.indexOf(self.tab_velocidad), _translate("MainWindow", "Velocidad"))
        self.tabWidget_vectorial.setTabText(self.tabWidget_vectorial.indexOf(self.tab_aceleracion), _translate("MainWindow", "Aceleración "))
        self.tabWidget_naturales.setTabText(self.tabWidget_naturales.indexOf(self.tab_simulacion_na), _translate("MainWindow", " Simulación"))
        self.tabWidget_naturales.setTabText(self.tabWidget_naturales.indexOf(self.tab_posicion_na), _translate("MainWindow", "Posición "))
        self.tabWidget_naturales.setTabText(self.tabWidget_naturales.indexOf(self.tab_velocidad_na), _translate("MainWindow", "Velocidad"))
        self.tabWidget_naturales.setTabText(self.tabWidget_naturales.indexOf(self.tab_aceleracion_na), _translate("MainWindow", "Aceleración "))

    def CreateVectorial(self):
        _translate = QtCore.QCoreApplication.translate
        variables = get_elements.return_dict(CierreVec)
        i = 0
        valores_iniciales = [6 , 2, 4, 5, 0.1745, 0, 1, 1, 2]
        labels = {}
        entries = {}
        for v_iniciales, variable in zip(valores_iniciales, variables):
                i += 1
                labels[f'label_{i}'] = QtWidgets.QLabel(self.frame_vectorial)
                labels[f'label_{i}'].setGeometry(QtCore.QRect(20, 50 + i*50, 55, 16))
                labels[f'label_{i}'].setObjectName(f'label_{i}')
                labels[f'label_{i}'].setText(_translate("MainWindow", variable))

                entries[f'entry_{i}'] = QtWidgets.QDoubleSpinBox(self.frame_vectorial)
                entries[f'entry_{i}'].setGeometry(QtCore.QRect(140, 50 + i*50, 60, 25))
                entries[f'entry_{i}'].setProperty("value", v_iniciales)
                entries[f'entry_{i}'].setObjectName(f'entry_{i}')
        # entries_list = lambda: [i.value() for i in entries.values()] 
        # crea el boton de graficar en una tab
        self.graficarBtn_vectorial = QtWidgets.QPushButton(self.tab)
        self.graficarBtn_vectorial.setGeometry(QtCore.QRect(1700, 800, 121, 41))
        self.graficarBtn_vectorial.setStyleSheet("")
        self.graficarBtn_vectorial.setObjectName("graficarBtn_vectorial")
        self.graficarBtn_vectorial.clicked.connect(lambda: plots['plots_vectorial_0'].clear())
        self.graficarBtn_vectorial.clicked.connect(lambda: plots['plots_vectorial_1'].clear())
        self.graficarBtn_vectorial.clicked.connect(lambda: plots['plots_vectorial_2'].clear())
        self.graficarBtn_vectorial.clicked.connect(lambda: plots['plots_vectorial_3'].clear())
        self.graficarBtn_vectorial.clicked.connect(lambda: CierreVec.CierreVectorial(plots[f'plots_vectorial_0'], plots['plots_vectorial_1'], plots['plots_vectorial_2'], plots['plots_vectorial_3'], app, *[i.value() for i in entries.values()] ).SolucionVectorial())
        self.graficarBtn_vectorial.setText(_translate("MainWindow", "Graficar"))
        
        # crea la grafica de simulacion
        lista_plots = [self.tab_simulacion, self.tab_posicion, self.tab_velocidad, self.tab_aceleracion]
        plots = {}
        for i, plot in enumerate(lista_plots):
            plots[f'plots_vectorial_{i}'] = PlotWidget(plot, background='w')
            plots[f'plots_vectorial_{i}'].setGeometry(QtCore.QRect(60, 30, 1200, 700))
            plots[f'plots_vectorial_{i}'].setObjectName("graphicsView_simulacion")
            plots[f'plots_vectorial_{i}'].getAxis("left").setStyle(tickLength = 20)
            plots[f'plots_vectorial_{i}'].getAxis("bottom").setStyle(tickLength = 20)
            plots[f'plots_vectorial_{i}'].showGrid(x = True, y = True, alpha = 0.8)  

    def layout_vectorial(self):
        # crea el tab de graficas
        self.tabWidget_vectorial = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_vectorial.setGeometry(QtCore.QRect(270, 10, 1900, 900))
        self.tabWidget_vectorial.setObjectName("tabWidget_vectorial")
        # crea el tab de la simulacion
        self.tab_simulacion = QtWidgets.QWidget()
        self.tab_simulacion.setObjectName("tab_simulacion")
        self.tabWidget_vectorial.addTab(self.tab_simulacion, "")
        # crea la tab de posicion
        self.tab_posicion = QtWidgets.QWidget()
        self.tab_posicion.setObjectName("tab_posicion")
        self.tabWidget_vectorial.addTab(self.tab_posicion, "")
        # crea la tab de velocidad
        self.tab_velocidad = QtWidgets.QWidget()
        self.tab_velocidad.setObjectName("tab_velocidad")
        self.tabWidget_vectorial.addTab(self.tab_velocidad, "")
        # crea la tab de acelaracion
        self.tab_aceleracion = QtWidgets.QWidget()
        self.tab_aceleracion.setObjectName("tab_aceleracion")
        self.tabWidget_vectorial.addTab(self.tab_aceleracion, "")
        # crea el frame de los botones y los labels
        self.frame_vectorial = QtWidgets.QFrame(self.tab)
        self.frame_vectorial.setGeometry(QtCore.QRect(20, 50, 221, 631))
        self.frame_vectorial.setStyleSheet("QFrame {\n"
                                "background: rgb(43, 63, 85);\n"
                                "border: none;\n"
                                "border-radius: 20px;\n"
                                "}\n"
                                "\n"
                                "QDoubleSpinBox\n"
                                "{\n"
                                "border : none;\n"
                                "background : rgb(156, 29, 231);\n"
                                "font-size: 20px;\n"
                                "border-radius: 7px;\n"
                                "}\n"
                                "\n"
                                "QDoubleSpinBox::hover {\n"
                                "background: rgb(88, 27, 152);\n"
                                "}\n"
                                "\n"
                                "QLabel {\n"
                                "border: none;\n"
                                "border-radius: 5px;\n"
                                "color: white;\n"
                                "font-size: 15px;\n"
                                "}\n"
                                "")
        self.frame_vectorial.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_vectorial.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_vectorial.setObjectName("frame_vectorial")
        self.tabWidget.addTab(self.tab, "")

    def layout_naturales(self):
        # crea el tab de graficas
        self.tabWidget_naturales = QtWidgets.QTabWidget(self.tab_cnaturales)
        self.tabWidget_naturales.setGeometry(QtCore.QRect(270, 10, 1900, 900))
        self.tabWidget_naturales.setObjectName("tabWidget_naturales")
        # crea el tab de la simulacion
        self.tab_simulacion_na = QtWidgets.QWidget()
        self.tab_simulacion_na.setObjectName("tab_simulacion_na")
        self.tabWidget_naturales.addTab(self.tab_simulacion_na, "")
        # crea la tab de posicion
        self.tab_posicion_na = QtWidgets.QWidget()
        self.tab_posicion_na.setObjectName("tab_posicion_na")
        self.tabWidget_naturales.addTab(self.tab_posicion_na, "")
        # crea la tab de velocidad
        self.tab_velocidad_na = QtWidgets.QWidget()
        self.tab_velocidad_na.setObjectName("tab_velocidad_na")
        self.tabWidget_naturales.addTab(self.tab_velocidad_na, "")
        # crea la tab de acelaracion
        self.tab_aceleracion_na = QtWidgets.QWidget()
        self.tab_aceleracion_na.setObjectName("tab_aceleracion_na")
        self.tabWidget_naturales.addTab(self.tab_aceleracion_na, "")
        # crea el frame de los botones y los labels
        self.frame_naturales = QtWidgets.QFrame(self.tab_cnaturales)
        self.frame_naturales.setGeometry(QtCore.QRect(20, 50, 221, 631))
        self.frame_naturales.setStyleSheet("QFrame {\n"
                                "background: rgb(43, 63, 85);\n"
                                "border: none;\n"
                                "border-radius: 20px;\n"
                                "}\n"
                                "\n"
                                "QDoubleSpinBox\n"
                                "{\n"
                                "border : none;\n"
                                "background : rgb(156, 29, 231);\n"
                                "font-size: 20px;\n"
                                "border-radius: 7px;\n"
                                "}\n"
                                "\n"
                                "QDoubleSpinBox::hover {\n"
                                "background: rgb(88, 27, 152);\n"
                                "}\n"
                                "\n"
                                "QLabel {\n"
                                "border: none;\n"
                                "border-radius: 5px;\n"
                                "color: white;\n"
                                "font-size: 15px;\n"
                                "}\n"
                                "")
        self.frame_naturales.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_naturales.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_naturales.setObjectName("frame_naturales")
        self.tabWidget.addTab(self.tab_cnaturales, "")


    def CreateNaturales(self):
        _translate = QtCore.QCoreApplication.translate
        variables = get_elements.return_dict(Naturales)
        i = 0
        valores_iniciales = [6, 2, 4, 5, 0, 1, 1, 1.5]
        labels_na = {}
        entries_na = {}
        for v_iniciales, variable in zip(valores_iniciales, variables):
                i += 1
                labels_na[f'label_{i}'] = QtWidgets.QLabel(self.frame_naturales)
                labels_na[f'label_{i}'].setGeometry(QtCore.QRect(20, 50 + i*50, 55, 16))
                labels_na[f'label_{i}'].setObjectName(f'label_{i}')
                labels_na[f'label_{i}'].setText(_translate("MainWindow", variable))

                entries_na[f'entry_{i}'] = QtWidgets.QDoubleSpinBox(self.frame_naturales)
                entries_na[f'entry_{i}'].setGeometry(QtCore.QRect(140, 50 + i*50, 60, 25))
                entries_na[f'entry_{i}'].setProperty("value", v_iniciales)
                entries_na[f'entry_{i}'].setObjectName(f'entry_{i}')
        # entries_list = lambda: [i.value() for i in entries.values()] 
        # crea el boton de graficar en una tab
        self.graficarBtn_naturales = QtWidgets.QPushButton(self.tab_cnaturales)
        self.graficarBtn_naturales.setGeometry(QtCore.QRect(1700, 800, 121, 41))
        self.graficarBtn_naturales.setStyleSheet("")
        self.graficarBtn_naturales.setObjectName("graficarBtn_naturales")
        self.graficarBtn_naturales.clicked.connect(lambda: plots_na['plots_naturales_0'].clear())
        self.graficarBtn_naturales.clicked.connect(lambda: plots_na['plots_naturales_1'].clear())
        self.graficarBtn_naturales.clicked.connect(lambda: plots_na['plots_naturales_2'].clear())
        self.graficarBtn_naturales.clicked.connect(lambda: plots_na['plots_naturales_3'].clear())
        self.graficarBtn_naturales.clicked.connect(lambda: Naturales.CoordenadasNaturales(plots_na[f'plots_naturales_0'], plots_na['plots_naturales_1'], plots_na['plots_naturales_2'], plots_na['plots_naturales_3'], app, *[i.value() for i in entries_na.values()] ).SolucionNatural())
        self.graficarBtn_naturales.setText(_translate("MainWindow", "Graficar"))
        
        # crea la grafica de simulacion
        lista_plots_na = [self.tab_simulacion_na, self.tab_posicion_na, self.tab_velocidad_na, self.tab_aceleracion_na]
        plots_na = {}
        for i, plot in enumerate(lista_plots_na):
            plots_na[f'plots_naturales_{i}'] = PlotWidget(plot, background='w')
            plots_na[f'plots_naturales_{i}'].setGeometry(QtCore.QRect(60, 30, 1200, 700))
            plots_na[f'plots_naturales_{i}'].setObjectName("graphicsView_simulacion")
            plots_na[f'plots_naturales_{i}'].getAxis("left").setStyle(tickLength = 20)
            plots_na[f'plots_naturales_{i}'].getAxis("bottom").setStyle(tickLength = 20)
            plots_na[f'plots_naturales_{i}'].showGrid(x = True, y = True, alpha = 0.8)  


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


