from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from msg import msg
from adminhome import Adminhome
from Connection import dbconnection as db
import pymysql
class adminreset(QMainWindow):
    def dlgbutton(self,buttonvalue):
        m=buttonvalue.text()
        if m=="OK":
            self.am=Adminhome()
            self.am.show()
            self.close()
    def up(self):
        ans=self.txtanswer.text()
        newpwd=self.txtnewpwd.text()
        con=self.txtconnewpwd.text()
        if ans=="cat":
            if newpwd==con:
               cn=db.createconnection()
               query="update adminlogin set password=%s where username=%s"
               name="admin"
               cursor=cn.cursor()
               cursor.execute(query,(newpwd,name))
               cn.commit()
               self.cm=QMessageBox()
               self.cm.setWindowTitle("Password Change")
               self.cm.setIcon(QMessageBox.Information)
               self.cm.setText("Password Changed Successfully")
               self.cm.setStandardButtons(QMessageBox.Ok)
               q=self.cm.buttonClicked.connect(self.dlgbutton)
               self.cm.exec()
            else:
                msg.messagebox("Password doesnot match")
        else:
            msg.messagebox("Answer doesnot match")
    def __init__(self):
        super(adminreset,self).__init__()
        loadUi("adminforgotpwdotp.ui",self)
        self.btnupdate.clicked.connect(self.up)
if __name__=="__main__":
    import sys
    app=QApplication(sys.argv)
    obj=adminreset()
    obj.show()
    sys.exit(app.exec())