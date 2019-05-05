#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import main_

import face_comparison_module
import finding_objects_module

sys.path.append('..\\')
import neural.nnet as net    

from PyQt5 import QtWidgets, QtGui

class MainApp(QtWidgets.QMainWindow, main_.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle('Main Menu')

        self.face_module.clicked.connect(self.first_module)
        self.object_module.clicked.connect(self.second_module)

        self.face_comparison = face_comparison_module.FaceComparison()
        self.finding_objects = finding_objects_module.FindingObjects()

    def first_module(self):
        self.face_comparison.show()
        self.close()

    def second_module(self):
        self.finding_objects.show()
        self.close()

def main():
    os.system('cls' if os.name=='nt' else 'clear')
    application = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    application.exec_()

if __name__ == '__main__':
    main()
else:
    pass