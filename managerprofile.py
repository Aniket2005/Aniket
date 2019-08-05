from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMessageBox
from Connection import dbconnection as db
from manager import*
from managerlogin import *

class Managerprofile(QMainWindow):

     def __init__(self):
        super(Managerprofile,self).__init__()
        loadUi("managerprofile.ui",self)
        # self.userid=self.txtuserid.text()
        # print(self.userid)

        # self.txtuserid.setReadOnly(True)
        self.btnupdate.clicked.connect(self.updatemanager)
        self.btngo.clicked.connect(self.fetch)



     def fetch(self):
        self.userid=self.txtuserid.text()
        # self.txtuserid.setReadOnly(True
        con = db.createconnection()
        query = "select * from managerprofile where UserId=%s"
        cursor = con.cursor()
        cursor.execute(query,(self.userid))
        con.commit()
        rows = cursor.fetchall()
        for i in rows:
           self.txtusername.setText(i[0])
           #self.txtuserid.setText(i[1])
           self.txtphone.setText(i[2])
           self.txtdob.setText(i[3])
           self.txtaddress.setText(i[4])
           self.txtcity.setText(i[5])
           self.txtcollege.setText(i[6])



     # def details(self):
     #    self.txtuserid.setReadOnly(True)
     #    cn = db.createconnection()
     #    self.userid = self.txtuserid.text()
     #    query = "select Name,Email,Password from manager where UserId=%s"
     #    cursor = cn.cursor()
     #    a = cursor.execute(query, (self.userid))
     #    totalrows = cursor.fetchall()
     #    if (a):
     #        for rowdata in totalrows:
     #            self.txtname.setText(rowdata[0])
     #            self.txtemail.setText(rowdata[1])
     #            self.txtpassword.setText(rowdata[2])
     #    else:
     #        msg.messagebox("Invalid UserId")



     def updatemanager(self):
         import manager
         con = db.createconnection()

         self.a=self.txtusername.text()

         self.b=self.txtphone.text()
         self.c=self.txtdob.text()
         self.d=self.txtaddress.text()
         self.e=self.txtcity.text()
         self.f=self.txtcollege.text()
         query = "update managerprofile set Name=%s,Phone=%s,DoB=%s,Address=%s,City=%s,College=%s where UserId=%s"
         cursor = con.cursor()
         cursor.execute(query,(self.a,self.b,self.c,self.d,self.e,self.f,self.userid))
         con.commit()
         self.back=manager.manager()
         self.back.show()
         self.back.lbluser.setText(self.userid)
         self.close()

         #rows=cursor.fetchall()
         #for i in rows:
             #self.txtusername.setText()=i[0]
             # self.txtuserid.setText()=i[1]
             # self.txtphone.setText()=i[2]
             # self.txtdob.setText()=i[3]
             # self.txtaddress.setText()=i[4]
             # self.txtcity.setText()=i[5]
             # self.txtcollege.setText()=i[6]
           #  print(i[0])
import managerlogin_rc
if __name__=="__main__":
    import sys
    app=QApplication(sys.argv)
    obj=Managerprofile()
    obj.show()
    sys.exit(app.exec())