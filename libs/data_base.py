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
			

			CREATE TABLE RECON(ID INTEGER PRIMARY KEY AUTOINCREMENT , 
			IDD INTEGER ,  
			VALUE_S TEXT ,
			FOREIGN KEY(IDD) REFERENCES DOMAIN(ID) 
			);
			CREATE TABLE MANUAL_CHECK(ID INTEGER PRIMARY KEY AUTOINCREMENT , 
			IDD INTEGER ,
			 
			VALUE_S TEXT , 
			FOREIGN KEY(IDD) REFERENCES DOMAIN(ID) 
			);
			CREATE TABLE ACCESS_CONTROL(ID INTEGER PRIMARY KEY AUTOINCREMENT , 
			IDD INTEGER ,
			 
			VALUE_S TEXT , 
			FOREIGN KEY(IDD) REFERENCES DOMAIN(ID) 
			);
			CREATE TABLE CS_VUNERABILITY(ID INTEGER PRIMARY KEY AUTOINCREMENT , 
			IDD INTEGER ,
			 
			VALUE_S TEXT ,
			FOREIGN KEY(IDD) REFERENCES DOMAIN(ID) 
			);
			CREATE TABLE RISKY_FUNC(ID INTEGER PRIMARY KEY AUTOINCREMENT , 
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
		self.cur.execute("INSERT INTO RECON(VALUE_S,IDD) VALUES (?,?) ",(array,domainid,))

		self.cur.execute("INSERT INTO MANUAL_CHECK(VALUE_S,IDD) VALUES (?,?) ",(array,domainid,))

		self.cur.execute("INSERT INTO ACCESS_CONTROL(VALUE_S,IDD) VALUES (?,?) ",(array,domainid,))

		self.cur.execute("INSERT INTO CS_VUNERABILITY(VALUE_S,IDD) VALUES (?,?) ",(array,domainid,))

		self.cur.execute("INSERT INTO RISKY_FUNC(VALUE_S,IDD) VALUES (?,?) ",(array,domainid,))
		
		self.connec.commit() 
	
	def updateMANUAL_CHECK(self,array,domainID): 
		self.cur.execute("UPDATE MANUAL_CHECK SET VALUE_S=? WHERE IDD=?  ",(array,domainID,))
		self.connec.commit() 

	def updateACCESS_CONTROL(self,array,domainID): 
		self.cur.execute("UPDATE ACCESS_CONTROL SET VALUE_S=? WHERE IDD=? ",(array,domainID,))
		self.connec.commit() 
	
	def updateRecon(self,array,domainID): 
		self.cur.execute("UPDATE RECON SET VALUE_S=? WHERE IDD=? ",(array,domainID,))
		self.connec.commit() 
	
	def updateCS_VUNERABILITY(self,array,domainID): 
		self.cur.execute("UPDATE CS_VUNERABILITY SET VALUE_S=? WHERE IDD=? ",(array,domainID,))
		self.connec.commit() 
	
	def updateRISKY_FUNC(self,array,domainID): 
		self.cur.execute("UPDATE RISKY_FUNC SET VALUE_S=? WHERE IDD=? ",(array,domainID,))
		self.connec.commit() 

	

	
	
	def DDC(self,id): 
		#delete domain and here check lists 
		
		self.cur.execute("DELETE FROM MANUAL_CHECK WHERE  IDD=?",(id,))
		self.cur.execute("DELETE FROM ACCESS_CONTROL WHERE IDD=? ",(id,))
		self.cur.execute("DELETE FROM RECON WHERE  IDD=? ",(id,))
		self.cur.execute("DELETE FROM CS_VUNERABILITY WHERE  IDD=? ",(id,))
		self.cur.execute("DELETE FROM RISKY_FUNC WHERE  IDD=? ",(id,))
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
		self.cur.execute("SELECT VALUE_S FROM MANUAL_CHECK WHERE IDD=?",(domainID,))
		LIST_MC = self.cur.fetchall()
		
		self.cur.execute("SELECT VALUE_S FROM ACCESS_CONTROL WHERE IDD=?",(domainID,))
		LIST_AC = self.cur.fetchall()

		self.cur.execute("SELECT VALUE_S FROM RECON WHERE IDD=?",(domainID,))
		LIST_RE = self.cur.fetchall()

		self.cur.execute("SELECT VALUE_S FROM CS_VUNERABILITY WHERE IDD=?",(domainID,))
		LIST_CSV = self.cur.fetchall()

		self.cur.execute("SELECT VALUE_S FROM RISKY_FUNC WHERE IDD=?",(domainID,))
		LIST_RF = self.cur.fetchall()
		lists = [LIST_RE[0][0],LIST_AC[0][0],LIST_MC[0][0],LIST_CSV[0][0],LIST_RF[0][0]]
		return lists 
	def TIECL(self,_idd): 
		#to test if the dimain create his list 
		self.cur.execute("SELECT VALUE_S FROM RECON WHERE IDD=?",(_idd,))
		lis_t = self.cur.fetchall() 
		
		return lis_t
	
	def Splite_asarray(self,String): 
		return String.split(",")
#you can use this code to create new data base change the name of it her and in main class also 
# Bd = db()
# Bd.connection("../base/database.db")

# Bd.createdb()