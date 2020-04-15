# -*- coding: utf-8 -*-

from subject import *
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Sem(object):
    '''def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        Sem.hide()
        self.window.show()'''
    def setupUi(self, Sem):
        Sem.setObjectName("Sem")
        Sem.resize(1376, 768)
        self.centralwidget = QtWidgets.QWidget(Sem)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(550, 90, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.three = QtWidgets.QPushButton(self.centralwidget)
        self.three.setGeometry(QtCore.QRect(300, 230, 251, 231))
        font = QtGui.QFont()
        font.setPointSize(75)
        self.three.setFont(font)
        self.three.setObjectName("three")

        self.four = QtWidgets.QPushButton(self.centralwidget)
        self.four.setGeometry(QtCore.QRect(800, 230, 251, 231))
        font = QtGui.QFont()
        font.setPointSize(75)
        self.four.setFont(font)
        self.four.setObjectName("four")

        self.four.clicked.connect(self.subject_scr)

        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(300, 480, 89, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.back.setFont(font)
        self.back.setObjectName("back")

        self.back.clicked.connect(lambda :self.close_scr(Sem))
        Sem.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Sem)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        Sem.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Sem)
        self.statusbar.setObjectName("statusbar")
        Sem.setStatusBar(self.statusbar)

        self.retranslateUi(Sem)
        QtCore.QMetaObject.connectSlotsByName(Sem)

    def close_scr(self,sem):
        sem.hide()
    def subject_scr(self):
        print("hii")
        self.sub = QtWidgets.QMainWindow()
        self.ui = Ui_sub()
        self.ui.setupUi(self.sub)
        self.sub.show()
        print("hello")
    def retranslateUi(self, Sem):
        _translate = QtCore.QCoreApplication.translate
        Sem.setWindowTitle(_translate("Sem", "Sem"))
        self.label.setText(_translate("Sem", "SELECT SEMESTER"))
        self.three.setText(_translate("Sem", "III"))
        self.four.setText(_translate("Sem", "IV"))
        self.back.setText(_translate("Sem", "BACK"))


'''if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Sem = QtWidgets.QMainWindow()
    ui = Ui_Sem()
    ui.setupUi(Sem)
    Sem.show()
    sys.exit(app.exec_())'''

