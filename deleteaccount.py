from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from Connection import dbconnection as db
import pymysql
from msg import msg
class Deleteaccount(QMainWindow):
    def dlgbutton(self,buttonvalue):
        m=buttonvalue.text()
        if m=="OK":
            self.close()
    def deleteacc(self):
        userid=self.txtuserid.text()
        cn=db.createconnection()
        query="delete from manager where UserId=%s"
        cursor=cn.cursor()
        a=cursor.execute(query,(userid))
        if(a):
            cn.commit()
            msgg=QMessageBox()
            msgg.setWindowTitle("Delete")
            msgg.setText("Record Deleted")
            msgg.setIcon(QMessageBox.Information)
            msgg.setStandardButtons(QMessageBox.Ok)
            msgg.buttonClicked.connect(self.dlgbutton)
            a=msgg.exec()
        else:
            msg.messagebox("UserId not found")



    def __init__(self):
        super(Deleteaccount,self).__init__()
        loadUi("deleteaccount.ui",self)
        self.btndelete.clicked.connect(self.deleteacc)

import deleteresource_rc
if __name__=="__main__":
    import sys
    app=QApplication(sys.argv)
    objdeleteaccount=Deleteaccount()
    objdeleteaccount.show()
    sys.exit(app.exec())