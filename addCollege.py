from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi
from Connection import dbconnection as db
import pymysql as py
from msg import msg
class addCollege(QMainWindow):
    def insertcollege(self):
        self.clg_name= self.txtcollegename.text()
        if self.clg_name=="":
            msg.messagebox("Please enter College Name")
        else:
            self.clg_code= self.txtcollegecode.text()
            if self.clg_code == "":
                msg.messagebox("Please enter College Code")
            else:
                self.aft=self.comboBox.currentText()
        # print(self.clg_name)
        # print(self.clg_code)
        # print(self.aft)
                con = db.createconnection()
                query = "insert into add_college(college_name,college_code,affilation) values(%s,%s,%s)"
                cursor = con.cursor()
                cursor.execute(query,(self.clg_name,self.clg_code,self.aft))
                con.commit()
                msg.messagebox("College added")
                print("College Added")
        # self.messagebox("Record Inserted")


    def __init__(self):
        super(addCollege,self).__init__()
        loadUi("addCollege.ui",self)
        self.btnadd.clicked.connect(self.insertcollege)
import addcollegeresource_rc
if __name__=="__main__":
    import sys
    app=QApplication(sys.argv)
    obj=addCollege()
    obj.show()
    sys.exit(app.exec())