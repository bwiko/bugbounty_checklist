# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scalable_checklist.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import os 

class Ui_CheckList_2(object):
    list_of_checkboxes = []
    L_CheckBox = []  
    config_file = ""
    Lihgt_theme = """background-color: #fafafa;
                color: #010203;
                """
    Dark_theme = """background-color: #19232D;
                color: #ffffff;
                """
    Switch_theme = False 
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(885, 580)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(667, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(Form)
#         self.tabWidget.setStyleSheet("QLabel     {\n"
# "font-weight: bold;\n"
# "font-size:16px;\n"
# "color: rgb(0, 0, 0);\n"
# "}\n"

# "}")
        
        self.tabWidget.setObjectName("tabWidget")
        
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 2)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "check liste"))
        self.pushButton_2.setText(_translate("Form", "cancel"))
        self.pushButton.setText(_translate("Form", "save"))
       
    
    def make_beauty(self,String): 
        if len(String) >= 85 : 
            return String[:85]+'\n'+String[85:]
        return String 
    def creat_tabs(self,list_tabe_name) : 
        self.tabWidget.clear()
        self.list_of_checkboxes.clear()
        i=0 
        list_taskes =self.get_TT_name()
        
        for tab in list_tabe_name : 
            tab_name = QtWidgets.QWidget()
            Tabe_name = QtWidgets.QWidget()
        
            horizontalLayout_2 = QtWidgets.QHBoxLayout(Tabe_name)
            
            ScrolArea = QtWidgets.QScrollArea(Tabe_name)
            ScrolArea.setWidgetResizable(True)
            
            scroLLayot = QtWidgets.QWidget()
            scroLLayot.setGeometry(QtCore.QRect(0, 0, 843, 478))
            #creating title 
             
            counter = 0 
            Ver_Layout = QtWidgets.QVBoxLayout()
            Ver_Layout_2 = QtWidgets.QVBoxLayout()
            Hor_Mian_Layouy = QtWidgets.QHBoxLayout(scroLLayot)
            self.L_CheckBox = []
            for T_T in   list_taskes[i]:  
                if T_T[:7] == '<title>' : 
                    if counter > 0 : 
                        switch = 1 
                    else : 
                        switch = 0 

                    
                    if switch == 0 : 

                        title = QtWidgets.QLabel(scroLLayot)
                        #title.setAlignment(QtCore.Qt.AlignCenter)
                        title.setText(T_T[7:])
                        title.setStyleSheet("font-weight: bold;\n"
                                            "font-size:16px;\n"
                                            "color: rgb(32, 74, 135);")
                        Ver_Layout.addWidget(title)
                        LINE = QtWidgets.QFrame(scroLLayot)
                        LINE.setFrameShape(QtWidgets.QFrame.HLine)
                        LINE.setFrameShadow(QtWidgets.QFrame.Sunken)
                        counter +=1
                        Ver_Layout.addWidget(LINE)
                    else  : 
                        title = QtWidgets.QLabel(scroLLayot)
                        
                        title.setText(T_T[7:])
                        
                        title.setStyleSheet("font-weight: bold;\n"
                                            "font-size:16px;\n"
                                            "color: rgb(32, 74, 135);")
                        Ver_Layout_2.addWidget(title)
                        LINE = QtWidgets.QFrame(scroLLayot)
                        LINE.setFrameShape(QtWidgets.QFrame.HLine)
                        LINE.setFrameShadow(QtWidgets.QFrame.Sunken)
                        counter -=1
                        Ver_Layout_2.addWidget(LINE)
                else :
                    CHB = QtWidgets.QCheckBox(scroLLayot)
                    CHB.setText(self.make_beauty(T_T))
                    CHB.stateChanged.connect(self.Ischanged)
                    if switch == 0 : 
                        
                        Ver_Layout.addWidget(CHB)
                        counter +=1
                    else : 
                        
                        Ver_Layout_2.addWidget(CHB)   
                        counter -=1
                    self.L_CheckBox.append(CHB)
                self.list_of_checkboxes.append(self.L_CheckBox)
            spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            
            Ver_Layout.addItem(spacerItem1)
            Ver_Layout_2.addItem(spacerItem2)
            Hor_Mian_Layouy.addLayout(Ver_Layout)
            Hor_Mian_Layouy.addLayout(Ver_Layout_2)
            if self.Switch_theme : 
                ScrolArea.setStyleSheet(self.Lihgt_theme)
            else : 
                ScrolArea.setStyleSheet(self.Dark_theme)

            ScrolArea.setWidget(scroLLayot)
            horizontalLayout_2.addWidget(ScrolArea)
            self.tabWidget.addTab(Tabe_name, tab)
            i+=1
            
    def Ischanged(self):
        self.Is_changed = True 
    def get_tab_name(self): 
        list_tabe_name = os.popen("cat '"+self.config_file+"' | grep -v '#' | cut -d':' -f1 | uniq | awk NF").read().split('\n')[:-1]
        return list_tabe_name  
    
    def get_TT_name(self):
        list_tabe_name = self.get_tab_name()
        taskes_list =[]
        for tab in list_tabe_name : 
            list_task = os.popen("cat '"+self.config_file+"' | grep -Ev '^#' |grep -E '^"+tab+":' | cut -d':' -f2 |awk NF").read().split('\n')[:-1]
            taskes_list.append(list_task)
        return taskes_list
    def set_config(self,path_name): 
        self.config_file = path_name
        
        self.creat_tabs(self.get_tab_name())

        
import icon_rc

