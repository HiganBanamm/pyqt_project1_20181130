# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
import sys
from Ui_interest import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        #self.ui.comboBox.addItem('1')
        self.ui.comboBox.addItems(["{0}".format(x) for x in range(2,31)])
    
#     def count(self):
#         principal = self.spinBox.value()
#         rate = self.spinBox_2.value()
#         years = self.comboBox.currentText()
#         amount = principal * ((1+rate/100)**years)
#         self.lineEdit.setText("RMB{0:.2f}".format(amount))
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        计算
        """
        principal = self.ui.spinBox.value()
        print(principal)
        rate = self.ui.spinBox_2.value()
        print(rate)
        years = self.ui.comboBox.currentText()
        print(years)
        a = rate /100.00
        print(a)
        b = 1+a
        print(b)
        c = b *years
        print(c)
        amount = principal * c
        #amount = principal * ((1+(rate/100.0))**years)
        self.ui.label_5.setText("RMB{0:.2f}".format(amount))
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())