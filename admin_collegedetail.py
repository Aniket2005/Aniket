from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from Connection import dbconnection as db
class admin_collegedetail(QMainWindow):
    def populatecombo(self):
        cn=db.createconnection()
        query="select college_code from add_College"
        cursor=cn.cursor()
        cursor.execute(query)
        totalrow=cursor.fetchall()
        for data in totalrow:
            self.cmbcode.addItems(data)
    def go(self):
        cn=db.createconnection()
        self.code=self.cmbcode.currentText()
        if self.code=="Select":
            print("jjjjj")
            self.me=QMessageBox()
            self.me.setWindowTitle("Sure")
            self.me.setText("Select any college code")
            self.me.setIcon(QMessageBox.Information)
            self.me.exec()
        else:
            query="select college_name,affilation from add_college where college_code=%s"
            cursor=cn.cursor()
            cursor.execute(query,(self.code))
            totalrows=cursor.fetchall()
            for data in totalrows:
                self.txtcollegename.setText(data[0])
                self.txtaffiliation.setText(data[1])
            # self.name=self.txtcollegename
            query1="select branch from college_details where college_code=%s"
            cursor1=cn.cursor()
            a=cursor1.execute(query1,(self.code))
            self.tblbranch.setRowCount(a)
            totalrow=cursor1.fetchall()
            for rowno,rowdata in enumerate(totalrow):
                for colno,coldata in enumerate(rowdata):
                    self.tblbranch.setItem(rowno,colno,QTableWidgetItem(str(coldata)))
            # for data in totalrow:
            #     self.tblbranch.setItem(0,0,QTableWidgetItem(str(data[0])))

    def __init__(self):
        super(admin_collegedetail,self).__init__()
        loadUi("admin_collegedetail.ui",self)
        self.txtcollegename.setReadOnly(True)
        self.txtaffiliation.setReadOnly(True)
        self.cmbcode.addItem("Select")
        self.populatecombo()
        self.tblbranch.setHorizontalHeaderLabels(("Branch",))
        self.cmbcode.currentIndexChanged.connect(self.go)
if __name__=="__main__":
    import sys
    app=QApplication(sys.argv)
    objadmincollegedetail=admin_collegedetail()
    objadmincollegedetail.show()
    sys.exit(app.exec())
