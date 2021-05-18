# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adder.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from  libs.data_base import db 

class Myline(QtWidgets.QLineEdit):

    def __init__(self, parent):
        self.isn_tclicked = True 
        super(Myline, self).__init__(parent)
        self.parentWindow = parent

    def mousePressEvent(self, event):
        self.setStyleSheet("""
                        border-style : none ; """ ) 

        
        self.parentWindow.mousePressEvent(event)
class Ui_Adding(object):
    data_base = db()
    
    choice = -1 
    _id = -1 
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(403, 130)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.Name = Myline(Form)
        self.Name.setObjectName("Name")
        self.horizontalLayout.addWidget(self.Name)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.URL_LINE = Myline(Form)
        self.URL_LINE.setObjectName("URL_LINE")
        self.horizontalLayout_2.addWidget(self.URL_LINE)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(208, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Cancel = QtWidgets.QPushButton(Form)
        self.Cancel.setObjectName("Cancel")
        

        

        self.horizontalLayout_3.addWidget(self.Cancel)
        self.ADD = QtWidgets.QPushButton(Form)
        self.ADD.setObjectName("ADD")

        self.horizontalLayout_3.addWidget(self.ADD)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 1, 1, 1)
        #click eventes :: 

        

        #code to center the widget 
        fg = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        fg.moveCenter(cp)
        self.move(fg.topLeft())

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "name"))
        self.label_2.setText(_translate("Form", "url     "))
        self.Cancel.setText(_translate("Form", "cancel"))
        self.ADD.setText(_translate("Form", "add"))
        self.ADD.setShortcut("Return")
        self.Cancel.setShortcut("Esc")