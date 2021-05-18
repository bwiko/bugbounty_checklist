# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'listes.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from libs.data_base import db


class MyTreewidgetItem(QtWidgets.QTreeWidgetItem): 
    ID_DOMAIN=-1
    

    def setId(self,idd):
        self.ID_DOMAIN = idd
    def getId(self): 
        return self.ID_DOMAIN
class Ui_Listes(object):
    _id=0
    DB = db()
    
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(815, 460)
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap(":/ICON/006-icon-2562060.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(self.icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        #adding new function to make the app able to add new methodology 
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setMinimumSize(QtCore.QSize(170, 0))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem('Defualt Methodology')
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.toolButton = QtWidgets.QToolButton(Form)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/ICON/004-target.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon1)
        self.toolButton.setIconSize(QtCore.QSize(25, 21))
        self.toolButton.setAutoRaise(True)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout_2.addWidget(self.toolButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        #-------------------------------------------------------


        self.MyList = QtWidgets.QTreeWidget(Form)
        self.MyList.setObjectName("MyList")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/ICON/004-target.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MyList.headerItem().setIcon(0, icon1)
        
        self.icon2 = QtGui.QIcon()
        self.icon2.addPixmap(QtGui.QPixmap(":/ICON/005-http.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        # self.DB.connection(dbname)

        # ##this is the func to view all domain and sub domain this func 
        # self.viewfunction(0,self.MyList)

        ##
        self.verticalLayout.addWidget(self.MyList)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add = QtWidgets.QToolButton(Form)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/ICON/001-plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add.setIcon(icon3)
        self.add.setIconSize(QtCore.QSize(40, 40))
        self.add.setAutoRaise(True)
        self.add.setObjectName("add")
        self.horizontalLayout.addWidget(self.add)
        self.dell_b = QtWidgets.QToolButton(Form)
        self.dell_b.setEnabled(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/ICON/002-remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dell_b.setIcon(icon4)
        self.dell_b.setIconSize(QtCore.QSize(40, 40))
        self.dell_b.setAutoRaise(True)
        self.dell_b.setObjectName("dell_b")
        self.horizontalLayout.addWidget(self.dell_b)
        self.subdomain_b = QtWidgets.QToolButton(Form)
        self.subdomain_b.setEnabled(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/ICON/007-browser.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.subdomain_b.setIcon(icon5)
        self.subdomain_b.setIconSize(QtCore.QSize(40, 40))
        self.subdomain_b.setAutoRaise(True)
        self.subdomain_b.setObjectName("subdomain_b")
        self.horizontalLayout.addWidget(self.subdomain_b)
        self.modify_b = QtWidgets.QToolButton(Form)
        self.modify_b.setEnabled(False)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/ICON/003-technical-support.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.modify_b.setIcon(icon6)
        self.modify_b.setIconSize(QtCore.QSize(40, 40))
        self.modify_b.setAutoRaise(True)
        self.modify_b.setObjectName("modify_b")
        self.horizontalLayout.addWidget(self.modify_b)
        self.attack = QtWidgets.QToolButton(Form)
        self.attack.setEnabled(False)
        self.attack.setIcon(icon1)
        self.attack.setIconSize(QtCore.QSize(40, 40))
        self.attack.setAutoRaise(True)
        self.attack.setObjectName("attack")
        self.horizontalLayout.addWidget(self.attack)
        self.verticalLayout.addLayout(self.horizontalLayout)
        
        
        fg = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        fg.moveCenter(cp)
        self.move(fg.topLeft())

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "List of web sites"))
        self.MyList.headerItem().setText(0, _translate("Form", "target"))
        __sortingEnabled = self.MyList.isSortingEnabled()
        self.MyList.setSortingEnabled(False)
        
        
        self.MyList.setSortingEnabled(__sortingEnabled)
        self.add.setText(_translate("Form", "..."))
        self.dell_b.setText(_translate("Form", "..."))
        self.subdomain_b.setText(_translate("Form", "..."))
        self.modify_b.setText(_translate("Form", "..."))
        self.attack.setText(_translate("Form", "..."))
        
        self.add.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">ADD DOMAIN </span><span style=\" font-size:12pt; font-weight:600; vertical-align:sub;\">this is to add domain name you can just prees \"Ctrl+A\" </span></p></body></html>"))
        self.dell_b.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">DELETE  </span><span style=\" font-size:12pt; font-weight:600; vertical-align:sub;\">this is to delete domain you can just prees \"Suppr\"  </span></p></body></html>"))
        self.subdomain_b.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">ADD SUBDOMAIN  </span><span style=\" font-size:12pt; font-weight:600; vertical-align:sub;\">this is to add subdomain you can just prees \"Ctrl+Alt+A\"  </span></p></body></html>"))
        self.modify_b.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">MODIFY  </span><span style=\" font-size:12pt; font-weight:600; vertical-align:sub;\">this is to Modify domain you can just prees \"Ctrl+M\"  </span></p></body></html>"))
        self.attack.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">OPEN CHECKLISTS   </span><span style=\" font-size:12pt; font-weight:600; vertical-align:sub;\">this is to open the checklist of  domain you can just prees \"Ctrl+E\"  </span></p></body></html>"))
        self.toolButton.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">TEST THE METHODOLOGY FILE</span><span style=\" font-size:12pt; font-weight:600; vertical-align:sub;\">this button was mad to test the appearance of the checklist window  \"Ctrl+T\"  </span></p></body></html>"))
    

    def viewfunction(self,idd,treeparent) :
        listD = self.DB.selectdomain_by_parent(idd) #get all subdomain of domain that have idd as id 
        if listD != [] : 

            if idd == 0 : 
                icon= self.icon2
            else : 
                icon= self.icon 
            for i in listD : 
                item = MyTreewidgetItem(treeparent)
                item.setText(0,i[2])
                item.setIcon(0,icon)
                item.setId(i[0])
                self.viewfunction(i[0],item)

    
   
        
import icon_rc
