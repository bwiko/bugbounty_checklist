#!/usr/bin/python 

from libs.adding import Ui_Adding
from libs.checklist import Ui_CheckList
from libs.listes import Ui_Listes
from PyQt5 import QtCore, QtGui, QtWidgets
from libs.confirmation import Ui_Confirm     
from libs.data_base import db 
from libs.Save_Form import Ui_Notsaved

class SaveForm(QtWidgets.QWidget,Ui_Notsaved): 
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent=parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.closeMain)
        self.pushButton_2.clicked.connect(self.close)
        self.pushButton_3.clicked.connect(self.save)

    def setMainClass(self,Mclass): 
        self.MainC = Mclass 
        
    def save(self): 
        self.MainC.Save_state()
        self.MainC.close() 
        self.close() 
    def closeMain(self): 
        self.close() 
        self.MainC.close() 

class Confirm(QtWidgets.QWidget,Ui_Confirm) :
    _id=-1
    DBC = db()
    DBC.connection("./base/database.db") 
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent=parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.dellet_domains)

    def setMainClass(self,MainC):
        self.MainC=MainC

    def dellet_domains(self):
        self.DBC.delldomain(self._id)

        self.MainC.MyList.clear()
        self.MainC.viewfunction(0,self.MainC.MyList)
        self.close()

class Adding(QtWidgets.QWidget,Ui_Adding) : 
    DBC = db()
    DBC.connection("./base/database.db")
    _id=0
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent=parent)
        self.setupUi(self)
        self.ADD.clicked.connect(self.Addingtodb)
        self.Cancel.clicked.connect(self.Close)
        
    def rob(self): 
        
        self.Name.setStyleSheet("""
                        border-style : none ; """ )
        self.URL_LINE.setStyleSheet("""
                        border-style : none ; """ )

    def setMainClass(self,MainC):
        self.MainC=MainC
    
    def VideLine_edite(self):
        self.URL_LINE.setText("")
        self.Name.setText("")
    def Close(self): 
        self.VideLine_edite() 
        self.close() 
    def Addingtodb(self): 
        
        COND = self.isntVide(self.URL_LINE)  
        COND = self.isntVide(self.Name) and COND    
        if COND  : 
            name = self.Name.text()
            url = self.URL_LINE.text()
            if self.choice == 0 : 
                 

                self.DBC.addomain(name,url,0) #adding domain to data base 
            elif self.choice == 1 : 
                self.DBC.updatedomain(name,url,self._id)
            elif self.choice == 2 : 
                self.DBC.addomain(name,url,self._id)
            self.close()
            self.MainC.MyList.clear()
            self.MainC.viewfunction(0,self.MainC.MyList)
            
            if self.choice == 0 :
                QtWidgets.QMessageBox.about(self, "Tip", "The domain added successfully !!")
            elif self.choice == 1 : 
                QtWidgets.QMessageBox.about(self, "Tip", "Updated successfully !!") 
            elif self.choice == 2 : 
                QtWidgets.QMessageBox.about(self, "Tip", "The subdomain added successfully !!")
            self.VideLine_edite()
    def Prepare_Modify(self): 
        L_domain = self.DBC.select_domain(self._id)
        ########## for set the line_edite with the text of the domain 
      
        self.Name.setText(L_domain[2])
        self.URL_LINE.setText(L_domain[3])
        
  
    
    def isntVide(self,linEd): 
        if linEd.text() == "" : 
            linEd.setStyleSheet("""
                        border-style : solid ; 
                        border-width:2px;
                        border-color : #EB3737;

                    """)
            return False
        else : 
            return True 
class CHeckList(QtWidgets.QWidget,Ui_CheckList) : 
    DBC = db()
    DBC.connection("./base/database.db")
    Is_changed = False
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent=parent)
        self.setupUi(self)
        self.aresaved = SaveForm() 
        self.aresaved.setMainClass(self)
        self.pushButton_2.clicked.connect(self.Close)
        self.pushButton.clicked.connect(self.Save_state)
       
        self.add_event_(self.l_Recon)
        self.add_event_(self.l_Manual_Check)
        self.add_event_(self.l_Risky_Funcktionality)
        self.add_event_(self.l_Access_Control)
        self.add_event_(self.l_C_V_Vulnerability)
    
    def prepareIs_changed(self): 
        self.Is_changed = False
    
    def Save_state(self): 

        # i try to reload all check box to ovoid the bug that appared in CODE_BUG1234 ( just for search the problem )
        #self.prepare_all()
        

        #this function whas create because in sqlite there is no arrays which made me  to create some pattern of string then  i select it and  handle it as arrays 
        RE_array = ""
        AC_array = ""
        MC_array = "" 
        CV_array = "" 
        RI_array = "" 

        for i in self.l_Recon : 
            
            if i.isChecked() : 
                RE_array += ",1"
            else :
                RE_array += ",0"
        
        for i in self.l_Manual_Check : 
            if i.isChecked() : 
                MC_array += ",1"
            else :
                MC_array += ",0"
        
        for i in self.l_Access_Control : 
            if i.isChecked() : 
                AC_array += ",1"
            else :
                AC_array += ",0"
        for i in self.l_C_V_Vulnerability : 
            if i.isChecked() : 
                CV_array += ",1"
            else :
                CV_array += ",0"

        for i in self.l_Risky_Funcktionality : 
            if i.isChecked() : 
                RI_array += ",1"
            else :
                RI_array += ",0"
        _id = self._id 
        self.DBC.updateMANUAL_CHECK(MC_array,_id)    
        self.DBC.updateACCESS_CONTROL(AC_array,_id)
        self.DBC.updateRecon(RE_array,_id)
        self.DBC.updateCS_VUNERABILITY(CV_array,_id)
        self.DBC.updateRISKY_FUNC(RI_array,_id)
        self.Is_changed = False 
        QtWidgets.QMessageBox.about(self, "Tip", "Saved  !!")
        self.Show_fun(self._id) 
    
    def setTITLE(self,_idd): 
        domanname = self.DBC.select_domain(_idd)
        self.setWindowTitle("Check list of "+domanname[2]+"{"+domanname[3]+"}")
    def Show_fun(self,_idd) : 
        
        acExist=self.DBC.TIECL(_idd)
        
        if acExist == [] : 
            self.DBC.PreparList(_idd) 
            
        elif acExist[0][0] != "None" : 
            Lists = self.DBC.select_checklist(_idd)
            self.Check_thechkboxexs(self.l_Recon,Lists[0])
            self.Check_thechkboxexs(self.l_Access_Control,Lists[1])
            self.Check_thechkboxexs(self.l_Manual_Check,Lists[2])
            self.Check_thechkboxexs(self.l_C_V_Vulnerability,Lists[3])
            self.Check_thechkboxexs(self.l_Risky_Funcktionality,Lists[4])
    def Check_thechkboxexs(self,CH_list,ArrayString): 
         
        Array = ArrayString.split(",")[1:]
        lastindex = len(Array)
        j=0 
        
        while j < lastindex : 
            if Array[j] == "1" : 
                #check the box please 
                CH_list[j].setChecked(True)
            j+=1
    def add_event_(self,ch_eckbox_list): 
        for i in ch_eckbox_list : 
            i.stateChanged.connect(self.Ischanged)

    def Ischanged(self): 
    
        self.Is_changed = True 
    
    def Close(self): 

        
        if self.Is_changed  : 

            self.aresaved.show() 
        else :
            self.close()  
class Main(QtWidgets.QWidget,Ui_Listes) : 
    DBC = db()
    DBC.connection("./base/database.db")
    def __init__(self,parent=None):
        self.addtolist = Adding() 
        self.addtolist.setMainClass(self)
        
        self.confirm = Confirm() 
        self.confirm.setMainClass(self)
        QtWidgets.QWidget.__init__(self,parent=parent)
        self.setupUi(self)

        
        self.MyList.itemClicked.connect(self.selectitems)

        self.attack.clicked.connect(self.lister) 
        self.attack.setShortcut("Ctrl+E")
        self.add.clicked.connect(self.adder)
        self.add.setShortcut("Ctrl+A")
        self.modify_b.clicked.connect(self.mod)
        self.modify_b.setShortcut("Ctrl+M")
        self.subdomain_b.clicked.connect(self.addsubdomain)
        self.subdomain_b.setShortcut("Ctrl+Alt+A")
        self.dell_b.clicked.connect(self.delete)
        self.dell_b.setShortcut("Del")
    
    def selectitems(self) : #enable the icons and get id of domain for adding and dellet or modify the domain 
        itemindex =self.MyList.currentItem()
        self._id = itemindex.getId()
        
        self.dell_b.setEnabled(True)
        self.subdomain_b.setEnabled(True)
        self.modify_b.setEnabled(True)
        self.attack.setEnabled(True)

    def delete(self): 

    	self.confirm._id =  self._id 
    	self.confirm.show() 
    def lister(self):
        #--------------------------------CODE_BUG1234------------------------------
        #this has an bug i don't understand how it show it says wrapped C/C++ object of type
        #QCheckBox has been deleted Aborted
        #so i try to call all preparelist function to reload and add all checkbox to lists agan 
        #don't work i try some other method after reading some manga 
        #the problem has been solved SOL_CODE_BUG1234  
        self.listcheck = CHeckList()
        #self.listcheck.prepare_all()
        self.listcheck._id =self._id
        self.listcheck.setTITLE(self._id)
        self.listcheck.Show_fun(self._id)
        self.listcheck.Is_changed =False 
        self.listcheck.show()
    
    def adder(self):
        

        self.addtolist.choice = 0 
        self.addtolist._id = self._id
        self.addtolist.rob()
        self.addtolist.show() 
    
    def mod(self): 
        self.addtolist.choice = 1 
        self.addtolist._id = self._id
        self.addtolist.Prepare_Modify()
        
        self.addtolist.show() 
    
    def addsubdomain(self): 
        self.addtolist.choice = 2 
        self.addtolist._id = self._id 
        self.addtolist.show()  

import icon_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Main()
    #ui = Ui_MainWindow()
    #ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
#the solotion of Bug: CODE_BUG1234 is in the checklist.py on SOL_CODE_BUG1234