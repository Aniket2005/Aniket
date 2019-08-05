from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi
from Connection import dbconnection as db
import pymysql as py
class collegedetails(QMainWindow):
    def exbtn(self,buttonvalue):
        m=buttonvalue.text()
        if m=="OK":
            self.lineEditFees.setText("")
            self.comboBoxBranch.setCurrentIndex(0)
            self.comboBoxDuration.setCurrentIndex(0)
    def dlgbutton(self,buttonvalue):
        m=buttonvalue.text()
        if m=="&Yes":
            self.lineEditFees.setText("")
            self.comboBoxBranch.setCurrentIndex(0)
            self.comboBoxDuration.setCurrentIndex(0)
        if m=="&No":
            self.exitdata()
        if m=="OK":
            self.lineEditFees.setText("")
            self.comboBoxBranch.setCurrentIndex(0)
            self.comboBoxDuration.setCurrentIndex(0)


    def populatecollegecombo(self):
        cn=db.createconnection()
        query="select college_name from add_college"
        cursor=cn.cursor()
        cursor.execute(query)
        totalrow=cursor.fetchall()
        for data  in totalrow:
            self.comboBoxCollegeName.addItems(data)
    def populatecollegecode(self):
        cn = db.createconnection()
        self.clgname=self.comboBoxCollegeName.currentText()
        query="select college_code from add_college where college_name=%s"
        cursor = cn.cursor()
        cursor.execute(query,(self.clgname))
        totalrow=cursor.fetchone()
        for data in totalrow:
            self.lineEditCollegeCode.setText(data)
        self.lineEditCollegeCode.setReadOnly(True)
    def exitdata(self):
        self.clgname = self.comboBoxCollegeName.currentText()
        cn=db.createconnection()
        query="select branch from college_details where college_name=%s"
        cursor=cn.cursor()
        self.a=cursor.execute(query,(self.clgname))
        if(self.a<3):
            self.message=QMessageBox()
            self.message.setText("College "+self.clgname+" "+"must have atleast three branches\nAdd more")
            self.message.setWindowTitle("Check")
            self.message.setIcon(QMessageBox.Information)
            self.message.buttonClicked.connect(self.exbtn)
            b=self.message.exec()
        else:
            self.close()
    def insdata(self):
        self.clgname=self.comboBoxCollegeName.currentText()
        self.clgcode=self.lineEditCollegeCode.text()
        self.branch = self.comboBoxBranch.currentText()
        self.fees= self.lineEditFees.text()
        self.duration= self.comboBoxDuration.currentText()
        # print(self.clgname)
        # print(self.clgcode)
        # print(self.branch)
        # print(self.fees)
        # print(self.duration)
        cn = db.createconnection()
        query="insert into college_details(college_name,college_code,branch,fees,duration) values(%s,%s,%s,%s,%s)"
        cursor = cn.cursor()
        cursor.execute(query, (self.clgname,self.clgcode,self.branch,self.fees,self.duration))
        query1="select college_name,branch from college_details where college_name=%s && branch=%s"
        cursor1=cn.cursor()
        a=cursor1.execute(query1,(self.clgname,self.branch))
        if(a==1):
            cn.commit()
            self.msggg = QMessageBox()
            self.msggg.setWindowTitle("Details inserted ")
            self.msggg.setText("Detail Added\nDou you want to add more?")
            self.msggg.setIcon(QMessageBox.Information)
            self.msggg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            self.msggg.buttonClicked.connect(self.dlgbutton)
            self.aa = self.msggg.exec()

        else:
            self.mess=QMessageBox()
            self.mess.setWindowTitle("Duplicated")
            self.mess.setText("Record already Exsist\nEnter new record")
            self.mess.setIcon(QMessageBox.Information)
            self.mess.buttonClicked.connect(self.dlgbutton)
            self.a1=self.mess.exec()
            print("Record alredy exsist")
        print("Details Added")


    def __init__(self):
        super(collegedetails,self).__init__()
        loadUi("collegedetails.ui",self)
        self.populatecollegecombo()
        self.comboBoxCollegeName.currentIndexChanged.connect(self.populatecollegecode)
        self.pushButtonAdd.clicked.connect(self.insdata)
        self.pushButtonExit.clicked.connect(self.exitdata)

import collegedetails_rc
if __name__=="__main__":
    import sys

    app=QApplication(sys.argv)

    obj=collegedetails()
    obj.show()
    sys.exit(app.exec())