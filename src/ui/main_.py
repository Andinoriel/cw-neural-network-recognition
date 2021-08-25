# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(254, 168)
        MainWindow.setMinimumSize(QtCore.QSize(254, 168))
        MainWindow.setMaximumSize(QtCore.QSize(254, 168))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.face_module = QtWidgets.QPushButton(self.centralwidget)
        self.face_module.setGeometry(QtCore.QRect(60, 30, 131, 51))
        self.face_module.setObjectName("face_module")
        self.object_module = QtWidgets.QPushButton(self.centralwidget)
        self.object_module.setGeometry(QtCore.QRect(60, 90, 131, 51))
        self.object_module.setObjectName("object_module")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.face_module.setText(_translate("MainWindow", "Face recognition module"))
        self.object_module.setText(_translate("MainWindow", "Finding objects module"))

