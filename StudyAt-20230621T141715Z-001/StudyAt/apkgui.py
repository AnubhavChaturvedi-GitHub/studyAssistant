import sys
import time

import brain.main
from ui import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt , QTime ,QTimer , QDate
from PyQt5.uic import loadUiType
from brain.main import main
import sys


class MainThread(QThread):

    def __init__(self):
        super(MainThread,self).__init__()


    def run(self):
        main()





startexe = MainThread()


class gui_start(QMainWindow):
    def __init__(self):
        super().__init__()
        self.sagui = Ui_Form()
        self.sagui.setupUi(self)
        self.sagui.startbutton.clicked.connect(self.starttask)
        self.sagui.stopbutton.clicked.connect(self.stoptask)

        output = "                                  \n " \
                 "       I am Study Assistant and I am here to assist you "
        self.sagui.studyasot.setText(output)


    def starttask(self):
        startexe.start()

    def stoptask(self):
        startexe.stop(self)





Guiapp = QApplication(sys.argv)
sa_gui = gui_start()
sa_gui.show()
Guiapp.exec_()