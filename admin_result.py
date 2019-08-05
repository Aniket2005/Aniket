from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from msg import msg
from Connection import dbconnection as db
class admin_result(QMainWindow):
    def populatecollege(self):
        cn=db.createconnection()
        code=self.cmbcode.currentText()
        query="select college_name from add_college where college_code=%s"
        cursor=cn.cursor()
        cursor.execute(query,(code))
        totalrow=cursor.fetchone()
        for data in totalrow:
            self.lblname.setText(data)
        query1="select branch from college_details where college_code=%s"
        cursor1=cn.cursor()
        cursor1.execute(query1,(code))
        totalrow1=cursor1.fetchall()
        for data1 in totalrow1:
            self.cmbbranch.addItems(data1)
    def populatecode(self):
        cn = db.createconnection()
        query = "select college_code from add_college"
        cursor = cn.cursor()
        cursor.execute(query)
        totalrow = cursor.fetchall()
        for data in totalrow:
            self.cmbcode.addItems(data)
    def populatetable(self):
        cn=db.createconnection()
        query="select year,passratio from passratio where college_code=%s && branch=%s"
        cursor=cn.cursor()
        a=cursor.execute(query,(self.cmbcode.currentText(),self.cmbbranch.currentText()))
        if a:
            self.tbl.setRowCount(a)
            totalrow=cursor.fetchall()
            for rowno,rowdata in enumerate(totalrow):
                for colno,coldata in enumerate(rowdata):
                    self.tbl.setItem(rowno,colno,QTableWidgetItem(str(coldata)))
        else:
            msg.messagebox("Record Not Found")
    def __init__(self):
        super(admin_result,self).__init__()
        loadUi("admin_result.ui",self)
        self.populatecode()
        self.cmbcode.currentIndexChanged.connect(self.populatecollege)
        self.tbl.setHorizontalHeaderLabels(("Year","Passing Percent"))
        self.btnsubmit.clicked.connect(self.populatetable)
if __name__=="__main__":
    import sys
    app=QApplication(sys.argv)
    obj=admin_result()
    obj.show()
    sys.exit(app.exec())