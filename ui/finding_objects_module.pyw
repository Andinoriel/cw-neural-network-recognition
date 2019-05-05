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
        os.system('cls' if os.name=='nt' else 'clear')

        self.setWindowTitle('Find Object')

        self.__path = self.__image_ = self.__image_data_ = None

        self.load_image.clicked.connect(self.load_image_)
        self.find_objects.clicked.connect(self.find_objects_)
        self.find_objects.setEnabled(False)
    
    def load_image_(self):
        directory = QtWidgets.QFileDialog.getOpenFileName(self)
        if not directory[0] == '':
            self.__path = directory[0]
            self.__image_ = QtGui.QPixmap(directory[0])
            self.__image_ = self.__image_.scaled(self.image.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
            self.image.setPixmap(self.__image_)
            self.find_objects.setEnabled(True)

    def find_objects_(self):
        findler = net.FindingObjects()
        findler.loadData(findler.finding_fast)

        self.__image_data_ = findler.loadImage(self.__path)
        (findler.process(self.__image_data_)).save('output.jpg')
        self.__image_ = QtGui.QPixmap('output.jpg')
        self.__image_ = self.__image_.scaled(self.image.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.image.setPixmap(self.__image_)