#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import main

sys.path.append('..\\')
import neural.nnet as net    

from PyQt5 import QtWidgets, QtGui


class MainApp(QtWidgets.QMainWindow, main.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.__current_net = net.FindingObjects()
        self.image = None

        self.openFileDialog.clicked.connect(self.loadImage)
        self.findObject.clicked.connect(self.processImage)

    def loadImage(self):
        directory = QtWidgets.QFileDialog.getOpenFileName(self)
        if not directory[0] == '':

            self.__current_net.loadData(self.__current_net.finding_fast)
            self.image = self.__current_net.loadImage(directory[0])

    
    def processImage(self):
        (self.__current_net.process(self.image)).save('out.jpg')

def main():
    application = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    application.exec_()

if __name__ == '__main__':
    main()
else:
    pass