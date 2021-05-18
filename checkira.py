#!/usr/bin/env python3 

from libs.adding import Ui_Adding
from libs.checklist_2 import Ui_CheckList_2
from libs.listes import Ui_Listes
from PyQt5 import QtCore, QtGui, QtWidgets
from libs.confirmation import Ui_Confirm     
from libs.data_base import db 
from libs.Save_Form import Ui_Notsaved
import os 
STT2 = open('darktxt.qss','r')
styl2=STT2.read()
Activ_white_mode = False
class SaveForm(QtWidgets.QWidget,Ui_Notsaved): 
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent=parent)
        self.setupUi(self)
        if Activ_white_mode : 
            self.setStyleSheet(styl2)
        
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
        self.MainC.outsideclose = False
        self.MainC.Is_changed = False 
        self.MainC.Closed_Without_Ch = True

        self.close() 
        self.MainC.close() 
        self.MainC.Show_fun(self.MainC._id)
class Checklist_2(QtWidgets.QWidget,Ui_CheckList_2) :
    _id=-1
    DBC = db()
    Closed_Without_Ch = False
    Is_changed = False
    outsideclose = True
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent=parent)
        self.setupUi(self)
        if Activ_white_mode :
            self.setStyleSheet(styl2)
            self.Switch_theme = True 
        self.aresaved = SaveForm() 
        self.aresaved.setMainClass(self)
        self.pushButton_2.clicked.connect(self.Close)
        self.pushButton.clicked.connect(self.Save_state)
        self.pushButton_2.setShortcut("Esc")
        self.pushButton.setShortcut("Ctrl+S")
    def setMainClass(self,MainC):
        self.MainC=MainC

    def Show_fun(self,_idd) : 
        
        acExist=self.DBC.TIECL(_idd)
        
        if acExist == [] : 
            self.DBC.PreparList(_idd) 
            
        elif acExist[0][0] != "None" : 
            Lists = self.DBC.select_checklist(_idd)
            list_value = Lists.split(':')
            In = len(list_value)
            j=0
            while(j < In):
                
                self.Check_thechkboxexs(self.list_of_checkboxes[j],list_value[j])
                j+=1
        elif acExist[0][0] == "None" and self.Closed_Without_Ch: 
            self.Unchack_all()

    def Save_state(self): 
        
        # i try to reload all check box to ovoid the bug that appared in CODE_BUG1234 ( just for search the problem )
        #self.prepare_all()
        total_value = ""
        
        for tap_task in self.list_of_checkboxes: 
            #this function whas create because in sqlite there is no arrays which made me  to create some pattern of string then  i select it and  handle it as arrays 
            task_value =''

            for i in tap_task : 
                
                if i.isChecked() : 

                    task_value += ",1"
                else :
                    task_value += ",0"
            
            
            total_value =total_value+":"+task_value
        total_value = total_value[1:]
        _id = self._id 
        
        self.DBC.updateTASKS(total_value,_id)    
        self.Is_changed = False 
        QtWidgets.QMessageBox.about(self, "Tip", "Saved  !!")
        self.Show_fun(self._id) 
    def Unchack_all(self): 
        for tap in self.list_of_checkboxes : 
                for checkbox in tap : 
                    checkbox.setChecked(False)
    def Check_thechkboxexs(self,CH_list,ArrayString): 
         
        Array = ArrayString.split(",")[1:]
        lastindex = len(Array)
        if lastindex > len(CH_list) : 
            lastindex = len(CH_list)

        j=0 
        
        while j < lastindex : 
            if Array[j] == "1" : 
                #check the box please 
                CH_list[j].setChecked(True)
            else : 
                #not check the box please 
                CH_list[j].setChecked(False)
            j+=1

    def closeEvent(self,e): 
        if self.outsideclose : 
            self.outsideclose = False
            self.Close() 
    def Close(self):
        if self.Is_changed  : 

            self.Is_changed = False 
            self.aresaved.show()
        else :
            self.close()  
        
    def setTITLE(self,_idd): 
        domanname = self.DBC.select_domain(_idd)
        self.setWindowTitle("Check list of "+domanname[2]+"{"+domanname[3]+"}")

    #comehere0
    
    def DbConnect(self,path):
        self.test_path = path 
        self.DBC.connection(path)
class Confirm(QtWidgets.QWidget,Ui_Confirm) :
    _id=-1
    DBC = db()
   
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent=parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.dellet_domains)
        if Activ_white_mode :

            self.setStyleSheet(styl2)
        
    def setMainClass(self,MainC):
        self.MainC=MainC

    def dellet_domains(self):
        self.DBC.delldomain(self._id)
        self.MainC.DiSable()
        self.MainC.MyList.clear()
        self.MainC.viewfunction(0,self.MainC.MyList)
        self.close()
    def DbConnect(self,path):
        self.DBC.connection(path)
class Adding(QtWidgets.QWidget,Ui_Adding) : 
    DBC = db()
    
    _id=0
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent=parent)
        self.setupUi(self)
        self.ADD.clicked.connect(self.Addingtodb)
        self.Cancel.clicked.connect(self.Close)
        if Activ_white_mode :
            self.setStyleSheet(styl2)
       
        self.Cancel.setShortcut("Esc")
        
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
    def DbConnect(self,path):
        self.DBC.connection(path)
class Main(QtWidgets.QWidget,Ui_Listes) : 
    Apppath = "."
    DBC = db()
    Dn_ex_Ca = False # this for prevent the comboBox from doing the click action when adding the file name  
   
    realname=""
    def __init__(self,parent=None):
        self.addtolist = Adding() 
        self.addtolist.setMainClass(self)
        self.listcheck = Checklist_2()

        self.confirm = Confirm() 
        self.confirm.setMainClass(self)
        QtWidgets.QWidget.__init__(self,parent=parent)
        self.setupUi(self)
        if Activ_white_mode :
            self.setStyleSheet(styl2)

        
        self.MyList.itemClicked.connect(self.selectitems)

        self.toolButton.clicked.connect(self.demo)
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
        
        #combobox event
        self.comboBox.currentTextChanged.connect(self.Change_db)

        #preparation data base 
        self.preapare_database()
        self.prepare_db()
        self.MyList.clear()
        self.viewfunction(0,self.MyList)
        
        
    def DiSable(self) :
        self.dell_b.setEnabled(False)
        self.subdomain_b.setEnabled(False)
        self.modify_b.setEnabled(False)
        self.attack.setEnabled(False)
    
    def selectitems(self) : #enable the icons and get id of domain for adding and dellet or modify the domain 
        itemindex =self.MyList.currentItem()
        self._id = itemindex.getId()
        
        self.dell_b.setEnabled(True)
        self.subdomain_b.setEnabled(True)
        self.modify_b.setEnabled(True)
        self.attack.setEnabled(True)

    def delete(self): 
        
        dbname=self.comboBox.currentText()
        self.confirm._id =  self._id 
        self.confirm.DbConnect( self.Apppath+'/base/'+dbname)
        self.confirm.show() 
    def lister(self):
        #--------------------------------CODE_BUG1234------------------------------
        #this has an bug i don't understand how it show it says wrapped C/C++ object of type
        #QCheckBox has been deleted Aborted
        #so i try to call all preparelist function to reload and add all checkbox to lists agan 
        #don't work i try some other method after reading some manga 
        #the problem has been solved SOL_CODE_BUG1234  
        
        self.listcheck.outsideclose = True
        self.listcheck.Is_changed = False
        
        dbname=self.comboBox.currentText()
        self.listcheck._id =self._id
        self.listcheck.DbConnect(self.Apppath+'/base/'+dbname)
        self.listcheck.setTITLE(self._id)
        self.listcheck.Unchack_all()
        self.listcheck.Show_fun(self._id)
        #self.listcheck.Is_changed =False 
        
        self.listcheck.Is_changed = False
        self.listcheck.showMaximized()
    def adder(self):
        

        self.addtolist.choice = 0 
        
        self.addtolist._id = self._id
        self.addtolist.rob()
        self.addtolist.ADD.setText("add domain")
        self.addtolist.ADD.setShortcut("Return")
        self.addtolist.show() 
    
    def mod(self): 
        self.addtolist.choice = 1 
        
        self.addtolist._id = self._id
        self.addtolist.Prepare_Modify()
        self.addtolist.ADD.setText("edit domain")
        self.addtolist.ADD.setShortcut("Return")
        self.addtolist.show() 
    
    def addsubdomain(self): 
        self.addtolist.choice = 2 
        
        self.addtolist._id = self._id 
        self.addtolist.ADD.setText("add subdomain")
        self.addtolist.ADD.setShortcut("Return")
        self.addtolist.show()  
    def preapare_database(self):
        configs_file=os.popen('ls -rt '+self.Apppath+'/methodologys').read().split('\n')[:-1]
        db_names=os.popen('ls -rt '+self.Apppath+'/base').read().split('\n')[:-1]
        index= len(configs_file)
        i = 0
        self.comboBox.clear()
        self.Dn_ex_Ca = False 
        while i < index : 
            
            name = configs_file[i].split('.')[0]
            self.comboBox.addItem(name)
            if name not in db_names : 
                DBC = db()
                DBC.connection(self.Apppath+"/base/"+name)
                DBC.createdb()
             
            i+=1
        self.Dn_ex_Ca = True
    def prepare_db(self): 
        #self.listcheck = Checklist_2() #miltuple checklists
        dbname=self.comboBox.currentText()
        self.realname =os.popen('ls '+self.Apppath+'/methodologys/ | grep -e ^"'+dbname+'"' ).read().replace('\n','')
        self.listcheck.set_config(self.Apppath+"/methodologys/"+self.realname)
        name =self.Apppath+'/base/'+dbname
        self.addtolist.DbConnect(name)
        self.confirm.DbConnect(name)
        self.listcheck._id =self._id
        self.listcheck.DbConnect(name)

        self.DbConnect(name)
    
    def Change_db(self): 
        if self.Dn_ex_Ca : 
            self.DiSable()
            self.prepare_db()
            self.MyList.clear()
            self.viewfunction(0,self.MyList)
            
    def demo(self): 
        self.listcheck._id =-1      
        
        self.listcheck.Is_changed = False
        self.listcheck.showMaximized()
    def DbConnect(self,path):
        self.DBC.connection(path)
        self.DB.connection(path)    
import icon_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Main()
    MainWindow.show()
    sys.exit(app.exec_())
#the solotion of Bug: CODE_BUG1234 is in the checklist.py on SOL_CODE_BUG1234