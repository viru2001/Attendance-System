
from newSem import *
from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_first_pg(object):
    '''def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow1()
        self.ui.setupUi(self.window)
        first_pg.hide()
        self.window.show()
    def closeAll(self):
        self.label.hide()
        self.FE.hide()
        self.SE.hide()
        self.TE.hide()
        self.BE.hide()

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 180, 89, 25))
        self.pushButton.setObjectName("pushButton")
       # first_pg.setCentralWidget(self.centralwidget)
        self.pushButton.show()'''
    def setupUi(self, first_pg):
        first_pg.setObjectName("first_pg")
        first_pg.resize(1376, 768)
        self.centralwidget = QtWidgets.QWidget(first_pg)
        self.centralwidget.setObjectName("centralwidget")
        self.SE = QtWidgets.QPushButton(self.centralwidget)
        self.SE.setGeometry(QtCore.QRect(600, 260, 150, 50))
        self.SE.setObjectName("SE")
        self.SE.setFont(QtGui.QFont("Ubuntu", 20))

        self.SE.clicked.connect(self.sem_scr)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(530, 100, 400, 50))
        self.label.setObjectName("label")
        self.label.setFont(QtGui.QFont("Ubuntu", 30))
        self.FE = QtWidgets.QPushButton(self.centralwidget)
        self.FE.setGeometry(QtCore.QRect(600, 180, 150, 50))
        self.FE.setObjectName("FE")
        self.FE.setFont(QtGui.QFont("Ubuntu", 20))
        self.TE = QtWidgets.QPushButton(self.centralwidget)
        self.TE.setGeometry(QtCore.QRect(600, 340, 150, 50))
        self.TE.setObjectName("TE")
        self.TE.setFont(QtGui.QFont("Ubuntu", 20))
        self.BE = QtWidgets.QPushButton(self.centralwidget)
        self.BE.setGeometry(QtCore.QRect(600, 420, 150, 50))
        self.BE.setObjectName("BE")
        self.BE.setFont(QtGui.QFont("Ubuntu", 20))
        first_pg.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(first_pg)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        first_pg.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(first_pg)
        self.statusbar.setObjectName("statusbar")
        first_pg.setStatusBar(self.statusbar)

        self.retranslateUi(first_pg)
        QtCore.QMetaObject.connectSlotsByName(first_pg)

    def sem_scr(self):
        self.Sem = QtWidgets.QMainWindow()
        self.ui = Ui_Sem()
        self.ui.setupUi(self.Sem)
        self.Sem.show()
    def retranslateUi(self, first_pg):
        _translate = QtCore.QCoreApplication.translate
        first_pg.setWindowTitle(_translate("first_pg", "Year Selection"))
        self.SE.setText(_translate("first_pg", "SE"))
        self.label.setText(_translate("first_pg", "SELECT THE YEAR"))
        self.FE.setText(_translate("first_pg", "FE"))
        self.TE.setText(_translate("first_pg", "TE"))
        self.BE.setText(_translate("first_pg", "BE"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    first_pg = QtWidgets.QMainWindow()
    ui = Ui_first_pg()
    ui.setupUi(first_pg)
    first_pg.show()
    sys.exit(app.exec_())
