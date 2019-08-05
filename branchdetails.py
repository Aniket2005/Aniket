from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMessageBox
from Connection import dbconnection as db
class branchDetails(QMainWindow):
    def __init__(self):
        super(branchDetails, self).__init__()
        loadUi("branchdetails.ui", self)
        self.populatecode()
        self.collegecodecomboBox.currentIndexChanged.connect(self.populatecollegename)
        self.comboBoxCourse.currentIndexChanged.connect(self.populatetable)
        self.tbl.setHorizontalHeaderLabels(("Year","Total Admission"))
    def populatetable(self):
        cn=db.createconnection()
        query="select year,total_admission from year_collegedetail where college_code=%s && Branch=%s"
        cursor=cn.cursor()
        a=cursor.execute(query,(self.collegecodecomboBox.currentText(),self.comboBoxCourse.currentText()))
        totalrow=cursor.fetchall()
        print(a)
        self.tbl.setRowCount((a))
        for rowno,rowdata in enumerate(totalrow):
            for colno,coldata in enumerate(rowdata):
                self.tbl.setItem(rowno,colno,QTableWidgetItem(str(coldata)))
    def populatebranch(self):
        cn = db.createconnection()
        self.clgcode=self.collegecodecomboBox.currentText()
        query = "select branch from college_details where college_code=%s"
        cursor = cn.cursor()
        cursor.execute(query,(self.clgcode))
        totalrow = cursor.fetchall()
        for data in totalrow:
            self.comboBoxCourse.addItems(data)
    def populatecode(self):
        cn=db.createconnection()
        query="select college_code from add_college"
        cursor=cn.cursor()
        cursor.execute(query)
        totalrow=cursor.fetchall()
        for data in totalrow:
            self.collegecodecomboBox.addItems(data)
    def populatecollegename(self):
        self.comboBoxCourse.clear()
        cn = db.createconnection()
        self.clgname=self.collegecodecomboBox.currentText()
        query="select college_name from add_college where college_code=%s"
        cursor = cn.cursor()
        cursor.execute(query,(self.clgname))
        totalrow=cursor.fetchall()
        for data in totalrow:
            self.lineEditCollegeName.setText(data[0])
        self.lineEditCollegeName.setReadOnly(True)
        self.populatebranch()


if __name__=="__main__":
    import sys

    app=QApplication(sys.argv)

    objhome=branchDetails()
    objhome.show()
    sys.exit(app.exec())