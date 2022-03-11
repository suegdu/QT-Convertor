
from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(620, 216)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 601, 371))
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setEnabled(True)
        self.groupBox_2.setGeometry(QtCore.QRect(240, 10, 391, 291))
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(230, 30, 113, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setGeometry(QtCore.QRect(230, 90, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(230, 10, 121, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(10, 120, 251, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 40, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(10, 50, 341, 16))
        self.label_10.setObjectName("label_10")
        self.label_3.setGeometry(QtCore.QRect(20, 20, 100, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 70, 91, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(30, 110, 151, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(30, 140, 131, 16))
        self.label_6.setObjectName("label_6")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(10, 60, 161, 16))
        self.label_11.setObjectName("label_11")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(30, 90, 141, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(40, 160, 121, 16))
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 620, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton_3.clicked.connect(self.worker)
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def worker(self):
        tr1 = self.lineEdit_2.text()
        tr2 = self.lineEdit.text()
       
        try:
         os.system(f"py -m PyQt5.uic.pyuic -x {tr1} -o {tr2}.py")
        except:
            os.system(f"python -m PyQt5.uic.pyuic -x {tr1} -o {tr2}.py")
        try:
            os.system(f"python3 -m PyQt5.uic.pyuic -x {tr1} -o {tr2}.py")
        except:
            pass

        
            
            

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QT .ui Convertor"))
        self.groupBox.setTitle(_translate("MainWindow", "QT .ui Convertor"))
        self.groupBox_2.setTitle(_translate("MainWindow", "To"))
        
        self.pushButton_3.setText(_translate("MainWindow", "Convert"))
        self.label.setText(_translate("MainWindow", "File Name (Without .py)"))
        self.label_2.setText(_translate("MainWindow", "Note: The Default Path Will Be The Same File Path."))
        self.label_3.setText(_translate("MainWindow", "File Path (With .ui):"))
        self.label_4.setText(_translate("MainWindow", "Example:"))
        self.label_5.setText(_translate("MainWindow", "Folder Path : Folder\\Projects\\"))
        self.label_6.setText(_translate("MainWindow", "You Have To Paste It As :"))
        self.label_7.setText(_translate("MainWindow", "The File Name Is : Test.ui"))
        self.label_8.setText(_translate("MainWindow", "Folder\\Projects\\Test.ui"))
        self.label_10.setText(_translate("MainWindow", "Note: Leaving The File Path Box Empty And Converting"))
        self.label_11.setText(_translate("MainWindow", "Will Convert An Empty .py File."))
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
