# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'face_comparison_module_.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FaceComparison(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        Form.setMinimumSize(QtCore.QSize(800, 600))
        Form.setMaximumSize(QtCore.QSize(800, 600))
        self.load_image_1 = QtWidgets.QPushButton(Form)
        self.load_image_1.setGeometry(QtCore.QRect(140, 480, 91, 41))
        self.load_image_1.setObjectName("load_image_1")
        self.load_image_2 = QtWidgets.QPushButton(Form)
        self.load_image_2.setGeometry(QtCore.QRect(560, 480, 91, 41))
        self.load_image_2.setObjectName("load_image_2")
        self.compare_image = QtWidgets.QPushButton(Form)
        self.compare_image.setGeometry(QtCore.QRect(350, 480, 91, 41))
        self.compare_image.setObjectName("compare_image")
        self.image_1 = QtWidgets.QLabel(Form)
        self.image_1.setGeometry(QtCore.QRect(60, 60, 261, 381))
        self.image_1.setText("")
        self.image_1.setObjectName("image_1")
        self.image_2 = QtWidgets.QLabel(Form)
        self.image_2.setGeometry(QtCore.QRect(490, 60, 261, 381))
        self.image_2.setText("")
        self.image_2.setObjectName("image_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.load_image_1.setText(_translate("Form", "Upload first \n"
"image"))
        self.load_image_2.setText(_translate("Form", "Upload second\n"
"image"))
        self.compare_image.setText(_translate("Form", "Compare\n"
"image"))

