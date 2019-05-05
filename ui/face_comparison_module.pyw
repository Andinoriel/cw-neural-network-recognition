#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import face_comparison_module_

sys.path.append('..\\')
import neural.nnet as net

from PyQt5 import QtWidgets, QtCore, QtGui

class FaceComparison(QtWidgets.QMainWindow, face_comparison_module_.Ui_FaceComparison):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        os.system('cls' if os.name=='nt' else 'clear')

        self.setWindowTitle('Face Comparison')

        self.__image_first = self.__image_second = None
        self.__path_first = self.__path_second = None

        self.load_image_1.clicked.connect(self.load_first_image)
        self.load_image_2.clicked.connect(self.load_second_image)      
        self.compare_image.clicked.connect(self.compare)

        self.compare_image.setEnabled(False)
        self.__flag_1 = self.__flag_2 = False

        self.__descriptor_value = 0.6

    def load_first_image(self):
        directory = QtWidgets.QFileDialog.getOpenFileName(self)
        if not directory[0] == '':
            self.__path_first = directory[0]
            self.__image_first = QtGui.QPixmap(directory[0])
            self.__image_first = self.__image_first.scaled(self.image_1.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
            self.image_1.setPixmap(self.__image_first)

            self.__flag_1 = True
            if self.__flag_1 and self.__flag_2:
                self.compare_image.setEnabled(True)

    def load_second_image(self):
        directory = QtWidgets.QFileDialog.getOpenFileName(self)
        if not directory[0] == '':
            self.__path_second = directory[0]
            self.__image_second = QtGui.QPixmap(directory[0])
            self.__image_second = self.__image_second.scaled(self.image_2.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
            self.image_2.setPixmap(self.__image_second)

            self.__flag_2 = True
            if self.__flag_1 and self.__flag_2:
                self.compare_image.setEnabled(True)

    def compare(self):
        comparator = net.PersonComparison()
        comparator.loadData()

        comparator.addPhoto(self.__path_first)
        comparator.addPhoto(self.__path_second)

        determinator_1 = comparator.determinePhoto(comparator.comparisonPhoto[0])
        determinator_2 = comparator.determinePhoto(comparator.comparisonPhoto[1])
        result = comparator.calculateDistance(determinator_1, determinator_2)

        if result<self.__descriptor_value:
            QtWidgets.QMessageBox.about(self, 'Result', 'Face Recognition: the same person is depicted.')
        else:
            QtWidgets.QMessageBox.about(self, 'Result', 'Face Recognition: not the same person is depicted.')
            
