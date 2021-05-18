#!/usr/bin/python

import sqlite3 



class db : 
	def connection(self,name):
		self.connec = sqlite3.connect(name)
		self.cur = self.connec.cursor() 

	def createdb(self): 
		 self.cur.executescript("""CREATE TABLE DOMAIN(ID INTEGER PRIMARY KEY AUTOINCREMENT, 
			PARENT INTEGER ,
			NAME VARCHAR(20),
			URL TEXT 

		 	);  
			
			CREATE TABLE TASK(ID INTEGER PRIMARY KEY AUTOINCREMENT , 
			IDD INTEGER ,  
			VALUE_S TEXT ,
			FOREIGN KEY(IDD) REFERENCES DOMAIN(ID) 
			);
			
		 	""") 
		 self.connec.commit() 

	def closedb(self): 
		self.connec.close() 


	def addomain(self,name,url,parent=0): 
		#add domain to data base !! 
		self.cur.execute(" INSERT INTO DOMAIN(NAME,URL,PARENT) VALUES (?,?,?)",(name,url,parent,))
		self.connec.commit() 
	
	
	
	def delldomain(self,id_d): 
		listD = self.selectdomain_by_parent(id_d) #get all subdomain of domain that have idd as id 
		if listD != [] : 
			for i in listD : 
				self.delldomain(i[0])
				
		self.DDC(id_d)
		
		self.connec.commit()
	
	

	def updatedomain(self,name,url,id): 

		self.cur.execute("UPDATE DOMAIN SET NAME=? , URL=? WHERE ID=?",(name,url,id,))
		self.connec.commit()

	

	def PreparList(self,domainid,array="None"): 
		self.cur.execute("INSERT INTO TASK(VALUE_S,IDD) VALUES (?,?) ",(array,domainid,))
		self.connec.commit() 
	
	def updateTASKS(self,array,domainID): 
		self.cur.execute("UPDATE TASK SET VALUE_S=? WHERE IDD=?  ",(array,domainID,))
		self.connec.commit() 


	

	
	
	def DDC(self,id): 
		#delete domain and here check lists 
		
		
		self.cur.execute("DELETE FROM TASK WHERE  IDD=? ",(id,))
		self.cur.execute("DELETE FROM DOMAIN WHERE ID = ? ",(id,))
		self.connec.commit() 
	def selectdomain_by_parent(self,parent):
		
		self.cur.execute("SELECT * FROM DOMAIN WHERE PARENT=? ",(parent,))
		return self.cur.fetchall()
	
	def select_domain(self,_id): 
		self.cur.execute("SELECT * FROM DOMAIN WHERE ID=? ",(_id,))
		list_ =  self.cur.fetchall()
		
		return list_[0]
	def select_checklist(self,domainID): 
		self.cur.execute("SELECT VALUE_S FROM TASK WHERE IDD=?",(domainID,))
		LIST_TASK_STATS = self.cur.fetchall()
		
		
		lists = LIST_TASK_STATS[0][0]
		return lists 
	def TIECL(self,_idd): 
		#to test if the dimain create his list 
		self.cur.execute("SELECT VALUE_S FROM TASK WHERE IDD=?",(_idd,))
		lis_t = self.cur.fetchall() 
		
		return lis_t
	
	def Splite_asarray(self,String): 
		return String.split(",")
#you can use this code to create new data base change the name of it her and in main class also 
# Bd = db()
# Bd.connection("../base/database.db")

# Bd.createdb()