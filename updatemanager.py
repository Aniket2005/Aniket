from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from Connection import dbconnection as db
from msg import msg
from home import *
from adminhome import *
import pymysql
class Updatemanager(QMainWindow):





    def fetch(self):
        self.txtuserid.setReadOnly(True)
        cn=db.createconnection()
        self.userid=self.txtuserid.text()
        query="select Name,Email,Password from manager where UserId=%s"
        cursor=cn.cursor()
        a=cursor.execute(query,(self.userid))
        totalrows=cursor.fetchall()
        if(a):
            for rowdata in totalrows:
                self.txtname.setText(rowdata[0])
                self.txtemail.setText(rowdata[1])
                self.txtpassword.setText(rowdata[2])
        else:
            msg.messagebox("Invalid UserId")



    def dlgbutton(self,buttonvalue):
        m=buttonvalue.text()
        if m=="OK":
            self.close()
    def update(self):

        cn = db.createconnection()
        self.userid=self.txtuserid.text()
        self.name=self.txtname.text()
        self.email=self.txtemail.text()
        a1=self.email.find('@')
        a2=self.email.find('.')
        print(a1)
        print(a2)
        c=a2-a1
        if(a1>0):

            if(c<2):
                messs = QMessageBox()
                messs.setText("invalid email")
                messs.setIcon(QMessageBox.Information)
                messs.setStandardButtons(QMessageBox.Ok)
                messs.exec()
                print("hhhhhhh")
            else:
                self.password=self.txtpassword.text()
                query="update manager set Name=%s,Email=%s,Password=%s where UserId=%s"
                cursor=cn.cursor()
                cursor.execute(query,(self.name,self.email,self.password,self.userid))
                cn.commit()
                mess=QMessageBox()
                mess.setText("Profile Updated")
                mess.setIcon(QMessageBox.Information)
                mess.setStandardButtons(QMessageBox.Ok)



                mess.buttonClicked.connect(self.dlgbutton)
                a = mess.exec()
        else:
            messss = QMessageBox()
            messss.setText("invalid email"
                           "")
            messss.setIcon(QMessageBox.Information)
            messss.setStandardButtons(QMessageBox.Ok)
            messss.exec()

    def __init__(self):
        super(Updatemanager,self).__init__()
        loadUi("updatemanager.ui",self)

        # self.btnback.clicked.connect(self.backk)
        self.btngetdetails.clicked.connect(self.fetch)

        self.btnupdate.clicked.connect(self.update)
import updatemanager_rc
if __name__=="__main__":
    import sys
    app=QApplication(sys.argv)
    objupdatemanager=Updatemanager()
    objupdatemanager.show()
    sys.exit(app.exec())