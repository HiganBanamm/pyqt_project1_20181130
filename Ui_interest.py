# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Python\ptqt\PyqtCode\project20181130\interest.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(262, 251)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 150, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(self.centralWidget)
        self.widget.setGeometry(QtCore.QRect(30, 40, 211, 101))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.spinBox = QtWidgets.QSpinBox(self.widget)
        self.spinBox.setPrefix("")
        self.spinBox.setMinimum(0)
        self.spinBox.setMaximum(1000000000)
        self.spinBox.setSingleStep(1000)
        self.spinBox.setDisplayIntegerBase(10)
        self.spinBox.setObjectName("spinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBox)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.spinBox_2 = QtWidgets.QSpinBox(self.widget)
        self.spinBox_2.setPrefix("")
        self.spinBox_2.setMinimum(0)
        self.spinBox_2.setMaximum(100)
        self.spinBox_2.setSingleStep(5)
        self.spinBox_2.setObjectName("spinBox_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinBox_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_5)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "计算"))
        self.label.setText(_translate("MainWindow", "principal:"))
        self.label_2.setText(_translate("MainWindow", "Rate:"))
        self.label_3.setText(_translate("MainWindow", "Years:"))
        self.label_4.setText(_translate("MainWindow", "Amount:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

