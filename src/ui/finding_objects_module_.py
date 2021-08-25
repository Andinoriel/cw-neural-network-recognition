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
        self.find_objects.setGeometry(QtCore.QRect(20, 540, 91, 41))
        self.find_objects.setObjectName("find_objects")
        self.load_image = QtWidgets.QPushButton(FindObject)
        self.load_image.setGeometry(QtCore.QRect(20, 490, 91, 41))
        self.load_image.setObjectName("load_image")
        self.image = QtWidgets.QLabel(FindObject)
        self.image.setGeometry(QtCore.QRect(10, 10, 781, 451))
        self.image.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.image.setText("")
        self.image.setObjectName("image")
        self.mode_fast = QtWidgets.QRadioButton(FindObject)
        self.mode_fast.setGeometry(QtCore.QRect(130, 490, 141, 41))
        self.mode_fast.setChecked(True)
        self.mode_fast.setObjectName("mode_fast")
        self.mode_normal = QtWidgets.QRadioButton(FindObject)
        self.mode_normal.setGeometry(QtCore.QRect(130, 540, 151, 31))
        self.mode_normal.setObjectName("mode_normal")
        self.mode_slow = QtWidgets.QRadioButton(FindObject)
        self.mode_slow.setEnabled(True)
        self.mode_slow.setGeometry(QtCore.QRect(290, 510, 181, 41))
        self.mode_slow.setObjectName("mode_slow")
        self.danger_mode = QtWidgets.QPushButton(FindObject)
        self.danger_mode.setGeometry(QtCore.QRect(310, 510, 131, 41))
        self.danger_mode.setObjectName("danger_mode")

        self.retranslateUi(FindObject)
        QtCore.QMetaObject.connectSlotsByName(FindObject)

    def retranslateUi(self, FindObject):
        _translate = QtCore.QCoreApplication.translate
        FindObject.setWindowTitle(_translate("FindObject", "Find Object"))
        self.find_objects.setText(_translate("FindObject", "Find\n"
"objects"))
        self.load_image.setText(_translate("FindObject", "Load\n"
"image"))
        self.mode_fast.setText(_translate("FindObject", "Fast Mode - Effectively,\n"
"but not accurate results"))
        self.mode_normal.setText(_translate("FindObject", "Normal Mode - Balance \n"
"between quality and speed"))
        self.mode_slow.setText(_translate("FindObject", "Slow Mode - High accuracy, but \n"
"consumes a lot of resources"))
        self.danger_mode.setText(_translate("FindObject", "Enable danger mode"))

