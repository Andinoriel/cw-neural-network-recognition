# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'finding_objects_module_.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FindObject(object):
    def setupUi(self, FindObject):
        FindObject.setObjectName("FindObject")
        FindObject.resize(800, 600)
        FindObject.setMinimumSize(QtCore.QSize(800, 600))
        FindObject.setMaximumSize(QtCore.QSize(800, 600))
        self.find_objects = QtWidgets.QPushButton(FindObject)
        self.find_objects.setGeometry(QtCore.QRect(430, 490, 91, 41))
        self.find_objects.setObjectName("find_objects")
        self.load_image = QtWidgets.QPushButton(FindObject)
        self.load_image.setGeometry(QtCore.QRect(280, 490, 91, 41))
        self.load_image.setObjectName("load_image")
        self.image = QtWidgets.QLabel(FindObject)
        self.image.setGeometry(QtCore.QRect(10, 10, 781, 451))
        self.image.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.image.setText("")
        self.image.setObjectName("image")

        self.retranslateUi(FindObject)
        QtCore.QMetaObject.connectSlotsByName(FindObject)

    def retranslateUi(self, FindObject):
        _translate = QtCore.QCoreApplication.translate
        FindObject.setWindowTitle(_translate("FindObject", "Form"))
        self.find_objects.setText(_translate("FindObject", "Find\n"
"objects"))
        self.load_image.setText(_translate("FindObject", "Load\n"
"image"))

