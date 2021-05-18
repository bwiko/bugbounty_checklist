# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connfirm.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Confirm(object):
    connd = False 
    _id = -1 
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(240, 66)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 2, 1, 1)

        self.pushButton.clicked.connect(self.YES)
        self.pushButton_2.clicked.connect(self.close)
       
        
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
        self.pushButton_2.setText(_translate("Form", "No"))
        self.label.setText(_translate("Form", "are you sure yu want dellete that "))
        self.pushButton.setText(_translate("Form", "Yes"))
        self.pushButton.setShortcut("Return")
        self.pushButton_2.setShortcut("Esc")
    
    def YES(self): 
        self.conn= True 
        self.close()