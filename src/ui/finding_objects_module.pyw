#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import finding_objects_module_

sys.path.append('..\\')
import neural.nnet as net

from PyQt5 import QtWidgets, QtCore, QtGui

class FindingObjects(QtWidgets.QMainWindow, finding_objects_module_.Ui_FindObject):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.__path = self.__image_ = self.__image_data_ = None

        self.load_image.clicked.connect(self.load_image_)
        self.find_objects.clicked.connect(self.find_objects_)
        self.danger_mode.clicked.connect(self.danger_mode_)

        self.find_objects.setEnabled(False)
        self.mode_slow.setEnabled(False)
        self.mode_slow.hide()

    def load_image_(self):
        directory = QtWidgets.QFileDialog.getOpenFileName(self)
        if not directory[0] == '':
            self.__path = directory[0]
            self.__image_ = QtGui.QPixmap(directory[0])
            self.__image_ = self.__image_.scaled(self.image.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
            self.image.setPixmap(self.__image_)
            QtWidgets.QMessageBox.about(self, 'Result', 'When processing the image, the computer may not respond - please wait until execution is complete.')
            self.find_objects.setEnabled(True)

    def find_objects_(self):
        os.system('cls' if os.name=='nt' else 'clear')

        findler = net.FindingObjects()

        mode = None
        if self.mode_slow.isChecked():
            mode = findler.finding_slow
        elif self.mode_normal.isChecked():
            mode = findler.finding_normal
        elif self.mode_fast.isChecked():
            mode = findler.finding_fast

        findler.loadData(mode)
        findler.tensorboardDebug()

        self.__image_data_ = findler.loadImage(self.__path)
        (findler.process(self.__image_data_)).save('output.jpg')
        self.__image_ = QtGui.QPixmap('output.jpg')
        self.__image_ = self.__image_.scaled(self.image.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.image.setPixmap(self.__image_)

    def danger_mode_(self):
        qm = QtWidgets.QMessageBox()
        answ = qm.question(self, 'Confirm' , 'This mode may cause the computer to freeze and inability to continue working. Are you sure about your choice?')

        if answ == QtWidgets.QMessageBox.Yes:
            self.mode_slow.setEnabled(True)
            self.mode_slow.show()
            self.danger_mode.hide()
        else:
            pass
