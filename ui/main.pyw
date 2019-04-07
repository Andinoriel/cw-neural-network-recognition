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

        self.image = None

        self.openFileDialog.clicked.connect(self.loadImage)
        self.findObject.clicked.connect(self.processImage)

    def loadImage(self):
        directory = QtWidgets.QFileDialog.getOpenFileName(self)
        if not directory[0] == '':
            net.findingLoadData(net.finding_fast)
            self.image = net.findingLoadImage(directory[0])            
    
    def processImage(self):
        if not self.image == None:
            (net.processImage(self.image)).save('out.jpg')

def main():
    application = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    application.exec_()

if __name__ == '__main__':
    main()
else:
    pass