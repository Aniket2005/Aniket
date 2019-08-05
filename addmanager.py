from PyQt5.QtWidgets import *

from PyQt5.uic import loadUi
from Connection import dbconnection as db

import pymysql as pm
from PyQt5.QtWidgets import QMessageBox
class Addmanager(QMainWindow):
    def dlgbutton(self,buttonvalue):
        m=buttonvalue.text()
        if m=="OK":

            self.close()
    def messagebox(self,text):
        msg=QMessageBox()
        msg.setWindowTitle("Information")
        msg.setIcon(QMessageBox.Information)
        msg.setText(text)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.buttonClicked.connect(self.dlgbutton)
        a=msg.exec()
    def insertrecord(self,name,email,userid,password):
        con=db.createconnection()
        query="insert into manager(Name,Email,UserId,Password) values(%s,%s,%s,%s)"
        cursor=con.cursor()
        cursor.execute(query,(name,email,userid,password))
        con.commit()
        self.messagebox("Record Inserted")
    def display(self):
        firstname=self.txtfirstname.text()
        if firstname=="":
            self.mess = QMessageBox()
            self.mess.setWindowTitle("Wrong")
            self.mess.setText("Incomplete Entries")
            self.mess.setIcon(QMessageBox.Information)
            self.mess.exec()
        else:
            lastname=self.txtlastname.text()
            if lastname == "":
                self.mess = QMessageBox()
                self.mess.setWindowTitle("Wrong")
                self.mess.setText("Incomplete Entries")
                self.mess.setIcon(QMessageBox.Information)
                self.mess.exec()
            else:
                name=firstname+" "+lastname
                email=self.txtemail.text()
                userid=self.txtuserid.text()
                if userid=="":
                    self.mess = QMessageBox()
                    self.mess.setWindowTitle("Wrong")
                    self.mess.setText("Incomplete Entries")
                    self.mess.setIcon(QMessageBox.Information)
                    self.mess.exec()
                else:
                    password=self.txtpass.text()
                    confirmpass=self.txtconfirmpass.text()
                    if(password==confirmpass):
                        self.insertrecord(name,email,userid,password)
                    else:
                        self.mess=QMessageBox()
                        self.mess.setWindowTitle("Wrong")
                        self.mess.setText("Password Not Matched")
                        self.mess.setIcon(QMessageBox.Information)
                        self.mess.exec()
    def __init__(self):
        print("hyy")
        super(Addmanager,self).__init__()
        loadUi("addmanager.ui",self)
        self.btnregister.clicked.connect(self.display)
import addmanager_rc
if __name__=="__main__":
    import sys
    app=QApplication(sys.argv)
    objaddmanager=Addmanager()
    objaddmanager.show()

    sys.exit(app.exec())
