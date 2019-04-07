#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import main
from PyQt5 import QtWidgets

class MainApp(QtWidgets.QMainWindow, main.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

def main():
    application = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    application.exec_()

if __name__ == '__main__':
    main()
else:
    pass