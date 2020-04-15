
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from database import sender
from database import recevier
import subject
from wp import *
all_names=[['ANSARI SALMAN SARVAR'], ['BAGAYATKAR ANIKET SURAJ'], ['BHINGLE ABHISHEK B'], ['CHAWARA RUTUJA SURESH'], ['CHODANKAR AJAY ARVIND'], ['CHORMARE RAHUL JALINDAR'], ['CHOWKEKAR SAHIL'], ['DABHOLKAR SIDDHI NARESH'], ['DESAI PARTH JAYESH'], ['DESHMUKH PRANJALI KIRAN'], ['FEGADE VIRESH SHASHIKANT'], ['GIRKAR KSHITIJ BHARAT'], ['GORASIYA TANUSHREE JIVRAJ'], ['GORE ANUSHKA NARENDRA'], ['GOSAVI HITESH'], ['HOUZWALA LOUKIK JITENDRA'], ['INGALE DIMPLE NITIN'], ['JADHAV HEMANGI'], ['JADHAV PARIKSHIT'], ['JAMGE VIKAS AMRUT'], ['KESARKAR MANAV ASHOK'], ['KOKANE VED NANDADEEP'], ['KONDEKAR PARTH GURUDAS'], ['KORE MRUNMAI SHEKHAR'], ['KOYTEKAR ISHIKA K'], ['KULKARNI PRANAV B'], ['LATE AMEYA MANGESH'], ['MALVI BHUMIT PRAVIN'], ['MANE PRANJAL'], ['MEHTA MEET MANOJ'], ['MENON GOPIKHA UMESH'], ['MHATRE BHAKTI PRAKASH'], ['MHATRE MANASVI'], ['MHATRE SAKSHI MANISH'], ['MITTAL HARSH RAJKUMAR'], ['MORE VINIT VIPIN'], ['PALEKAR DIVYA RAJ'], ['PANCHAL NEEL JIGNESH'], ['PANDEY ADITYA RATNESH'], ['PANDEY PIYUSH KRIPA S'], ['PANDEY RACHNA RATNESH'], ['PANJA PROMITA PRABIR'], ['PARIKH SAUMYA AJAY'], ['PATIL AARATI'], ['PATIL SHUBHAM'], ['PATIL SNEHAL'], ['PATIL VEDANT DEVENDRA'], ['POOJARI RAHUL K'], ['RAI VAIBHAV RAJENDRA P'], ['RAMANE PRATHAMESH P'], ['RAORANE VINITA PRAVIN'], ['RATHOD ANIKET YOGESH'], ['RAUL YASH CHAKOR'], ['SAH NEHA RANJEET'], ['SALUNKE NIWANT SHARAD'], ['SANAP KALYANI'], ['SAVE PUSHKAR NILESH'], ['SAWANT PRANJALI VILAS'], ['SENTA DARSHAN P'], ['SHEDGE SHRUTI'], ['SHETTY SONIT HARISH'], ['SHINDE MAYUR POPAT'], ['SHINKAR RUTUJA MANOJ'], ['SHIVADE YASH R'], ['SONAWANE SWARAJ S'], ['SUHAGIYA SANKET R'], ['THAKARE SANDESH MOHAN'], ['THAKUR MIHIR ASHISH'], ['TIWARI ANAND SANTOSH'], ['VANMALI DAIDEEPYA'], ['VARTHA SIDDHARTH SANJAY'], ['VASAIKAR SIDDHANT SUNIL'], ['VEDPATHAK RITHWIK SANJIV'], ['WALINJKAR ABHISHEK A']]

data = []



class Ui_table(object):
    tableName1 = []

    def __init__(self,msg):
        self.tableName1 = msg
    '''def closeWindow(self):
       import sys
       self.tableWidget.hide()
       self.save.hide()
       self.back.hide()
       subject.Ui_sub.setupUi1(self)

    def total(self):
        for k in range(1):
            i=data[k]
            c=0
            for j in range(1,33):
                if i[j]=='None' or i[j]=='0':
                    pass
                else:
                    c+=1
            #print(c)
            per=(c/30)*100
            #print("per= ",per)

        data.clear()'''

    def get(self):
        a = self.tableName1[0] + "_" + self.tableName1[1]
        recevier.recv(a)
        for i in range(74):
            for k in range(33):
                 value=recevier.list1[i][k]
                 self.tableWidget.setItem(i, k, QtWidgets.QTableWidgetItem(str(value)))
    def total1(self):
        a = self.tableName1[0] + "_" + self.tableName1[1]

        sender.drop(a)
        #print(len(self.tableName1))
        #print(self.tableName1[0] + "_" + self.tableName1[1])

        #print("a: ",a)
        sender.create(a)
        for k in range(74):
            i=data[k]
            #print(data)
            #print("none= ",i.count('None'))
            if i.count('None')+i.count('')==31:
                self.tableWidget.setItem(k, 32, QtWidgets.QTableWidgetItem(str(0.00)))

                i[32]=0.0
                sender.insert1(i,a)
            else:
                one=i.count('1')
                zero=i.count('0')
                tot=one+zero
                #print(c)
                per=round((one/tot)*100,2)
                self.tableWidget.setItem(k,32,QtWidgets.QTableWidgetItem(str(per)))
                i[32]=per
                sender.insert1(i,a)

            #print("per= ",per)
        l=[]
        l1 = [data[2][0], str(data[2][32]), str(+919819191672),self.tableName1]
        l2 = [data[4][0], str(data[4][32]), str(+917738110960),self.tableName1]
        l3 = [data[10][0], str(data[10][32]), str(+918291105704),self.tableName1]
        l.append(l1)
        l.append(l2)
        l.append(l3)
        for i in range(3):
            sending_msg(l[i])

        defaulter = []
        for i in range(74):
            if data[i][32] < 75:
                d = [str(i + 1), data[i][0], str(data[i][32])]
                defaulter.append(d)
        sending_msg1(defaulter,self.tableName1)
        #print(defaulter)

        data.clear()
        self.showMsg1()

    def total(self):
        a = self.tableName1[0] + "_" + self.tableName1[1]

        sender.drop(a)
        #print(len(self.tableName1))
        #print(self.tableName1[0] + "_" + self.tableName1[1])

        #print("a: ",a)
        sender.create(a)
        for k in range(74):
            i=data[k]
            #print(data)
            #print("none= ",i.count('None'))
            if i.count('None')+i.count('')==31:
                self.tableWidget.setItem(k, 32, QtWidgets.QTableWidgetItem(str(0.00)))

                i[32]=0.0
                sender.insert1(i,a)
            else:
                one=i.count('1')
                zero=i.count('0')
                tot=one+zero
                #print(c)
                per=round((one/tot)*100,2)
                self.tableWidget.setItem(k,32,QtWidgets.QTableWidgetItem(str(per)))
                i[32]=per
                sender.insert1(i,a)

            #print("per= ",per)

        data.clear()
        self.showMsg()
    def showMsg(self):
        info = QMessageBox()
        info.setWindowTitle("MESSAGE")
        info.setText("DATA SUCCESSFULLY SAVED")
        x = info.exec_()
    def showMsg1(self):
        info = QMessageBox()
        info.setWindowTitle(" ")
        info.setText("MESSAGE SENT")
        x = info.exec_()


    def function(self):
        #print("at top of function")
        model = self.tableWidget.model()

        for row in range(model.rowCount()):
            data.append([])
            for column in range(model.columnCount()):
                index = model.index(row, column)
        # We suppose data are strings
                data[row].append(str(model.data(index)))
        #print(data)
        #print("i m in function")
        self.total()

    def function1(self):
        #print("at top of function")
        model = self.tableWidget.model()

        for row in range(model.rowCount()):
            data.append([])
            for column in range(model.columnCount()):
                index = model.index(row, column)
        # We suppose data are strings
                data[row].append(str(model.data(index)))
        #print(data)
        #print("i m in function")
        self.total1()


    def setupUi(self, table):
        table.setObjectName("table")
        table.resize(1376, 768)
        self.centralwidget = QtWidgets.QWidget(table)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 1300, 660))
        self.tableWidget.setRowCount(74)
        self.tableWidget.setColumnCount(33)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("1")
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()

        #self.tableWidget.setColumnWidth(0, 100)
        header = self.tableWidget.horizontalHeader()
        #header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        for i in range(33):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
        #header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(23, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(24, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(25, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(26, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(27, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(28, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(29, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(30, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(31, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(32, item)

        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(600, 665, 89, 25))
        self.save.setObjectName("save")
        self.save.clicked.connect(self.function)

        self.send = QtWidgets.QPushButton(self.centralwidget)
        self.send.setGeometry(QtCore.QRect(900, 665, 100, 25))
        self.send.setObjectName("send")
        self.send.clicked.connect(self.alert)


        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(300, 665, 89, 25))
        self.back.setObjectName("back")
        self.back.clicked.connect(lambda :self.close_scr(table))

        table.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(table)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        table.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(table)
        self.statusbar.setObjectName("statusbar")
        table.setStatusBar(self.statusbar)

        self.retranslateUi(table)
        QtCore.QMetaObject.connectSlotsByName(table)

        for k in range(74):
            self.tableWidget.setItem(k, 0, QtWidgets.QTableWidgetItem(str(all_names[k][0])))
            self.tableWidget.setItem(k, 32, QtWidgets.QTableWidgetItem(str("NIL")))

        self.get()

    def alert(self):
        self.function1()

    def close_scr(self,table):
        self.tableName1.clear()
        #subject.tableName.clear()
        tableName = ["subject", "month"]
        recevier.list1.clear()
        #print("clearing list ",subject.tableName)
        table.hide()
    def retranslateUi(self, table):
        _translate = QtCore.QCoreApplication.translate
        table.setWindowTitle(_translate("table", "table"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("table", "NAMES"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("table", "2"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("table", "3"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("table", "4"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("table", "5"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("table", "6"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("table", "7"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("table", "8"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("table", "9"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("table", "10"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("table", "11"))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("table", "12"))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("table", "13"))
        item = self.tableWidget.horizontalHeaderItem(14)
        item.setText(_translate("table", "14"))
        item = self.tableWidget.horizontalHeaderItem(15)
        item.setText(_translate("table", "15"))
        item = self.tableWidget.horizontalHeaderItem(16)
        item.setText(_translate("table", "16"))
        item = self.tableWidget.horizontalHeaderItem(17)
        item.setText(_translate("table", "17"))
        item = self.tableWidget.horizontalHeaderItem(18)
        item.setText(_translate("table", "18"))
        item = self.tableWidget.horizontalHeaderItem(19)
        item.setText(_translate("table", "19"))
        item = self.tableWidget.horizontalHeaderItem(20)
        item.setText(_translate("table", "20"))
        item = self.tableWidget.horizontalHeaderItem(21)
        item.setText(_translate("table", "21"))
        item = self.tableWidget.horizontalHeaderItem(22)
        item.setText(_translate("table", "22"))
        item = self.tableWidget.horizontalHeaderItem(23)
        item.setText(_translate("table", "23"))
        item = self.tableWidget.horizontalHeaderItem(24)
        item.setText(_translate("table", "24"))
        item = self.tableWidget.horizontalHeaderItem(25)
        item.setText(_translate("table", "25"))
        item = self.tableWidget.horizontalHeaderItem(26)
        item.setText(_translate("table", "26"))
        item = self.tableWidget.horizontalHeaderItem(27)
        item.setText(_translate("table", "27"))
        item = self.tableWidget.horizontalHeaderItem(28)
        item.setText(_translate("table", "28"))
        item = self.tableWidget.horizontalHeaderItem(29)
        item.setText(_translate("table", "29"))
        item = self.tableWidget.horizontalHeaderItem(30)
        item.setText(_translate("table", "30"))
        item = self.tableWidget.horizontalHeaderItem(31)
        item.setText(_translate("table", "31"))
        item = self.tableWidget.horizontalHeaderItem(32)
        item.setText(_translate("table", "TOTAL %"))
        self.save.setText(_translate("table", "SAVE"))
        self.back.setText(_translate("table", "BACK"))
        self.send.setText(_translate("table", "SEND ALERTS"))


'''if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    table = QtWidgets.QMainWindow()
    ui = Ui_table()
    ui.setupUi(table)
    table.show()
    sys.exit(app.exec_())'''
