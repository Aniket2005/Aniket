from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi
from Connection import dbconnection as db
from msg import msg as m
from adminhome import *
from home import *
from adminforgotpwd import adminforgotpwd
from home import homepy
class admin(QFrame):

   try:
       def re(self):
           self.r = adminforgotpwd()
           self.r.show()
           self.close()
       def showpage(self):
            self.objadminhome=Adminhome()
            self.objadminhome.show()
            self.close()
       def h(self):
           self.hh=homepy()
           self.hh.show()
           self.close()
       def signin(self):
            cn=db.createconnection()
            self.username=self.txtusername.text()
            self.password=self.txtpass.text()
            query="select username,password from adminlogin where username=%s && password=%s"
            cursor=cn.cursor()
            a=cursor.execute(query,(self.username,self.password))
            cursor.fetchone()
            if(a):
                print("okkk")
                self.showpage()

            else:
                m.messagebox("Inccorect details")

       def __init__(self):
            super(admin,self).__init__()
            loadUi("admin.ui",self)
            self.loginbtn.clicked.connect(self.signin)
            self.forgotbtn.clicked.connect(self.re)
            self.btnhome.clicked.connect(self.h)
   except:
       print("hhhhhhhhhhh")
import img_rc
if __name__=="__main__":
    import sys

    app=QApplication(sys.argv)

    objadmin=admin()
    objadmin.show()
    sys.exit(app.exec())