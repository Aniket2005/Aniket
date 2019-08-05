from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from msg import msg
from Connection import dbconnection as db
import pymysql
class passing(QMainWindow):
    def populatepasscombo(self):
        cn=db.createconnection()
        code=self.cmbcode.currentText()
        query="select total_admission from year_collegedetail where college_code=%s"
        cursor=cn.cursor()
        cursor.execute(query,(code))
        totalrow=cursor.fetchone()
        for data in totalrow:
            print(data)
            self.passbox.setMaximum(int(data))
    def populatecode(self):
        cn=db.createconnection()
        query="select distinct college_code from year_collegedetail"
        cursor=cn.cursor()
        cursor.execute(query)
        totalrow=cursor.fetchall()
        for data in totalrow:
            self.cmbcode.addItems(data)
    def populatecollege(self):
        # self.cmbbranch.clear()
        self.cmbyear.clear()
        cn=db.createconnection()
        code=self.cmbcode.currentText()
        query="select college_name from year_collegedetail where college_code=%s"
        cursor=cn.cursor()
        cursor.execute(query,(code))
        totalrow=cursor.fetchone()
        for data in totalrow:
            self.lblname.setText(data)
        # self.populatebranch()
        self.populateyear()
    def populateyear(self):
        code = self.cmbcode.currentText()
        cn = db.createconnection()
        query = "select distinct year from year_collegedetail where college_code=%s"
        cursor = cn.cursor()
        cursor.execute(query, (code))
        totalrow = cursor.fetchall()
        for data in totalrow:
            self.cmbyear.addItems(data)

    def populatebranch(self):
        self.cmbbranch.clear()
        # self.cmbbranch.addItem("Select")
        code=self.cmbcode.currentText()
        cn=db.createconnection()
        query="select distinct Branch from year_collegedetail where college_code=%s && year=%s"
        cursor=cn.cursor()
        cursor.execute(query,(code,self.cmbyear.currentText()))
        totalrow=cursor.fetchall()
        for data in totalrow:
            self.cmbbranch.addItems(data)
    def populatepassing(self):
            if self.cmbyear.currentText()!="Select":
                cn=db.createconnection()
                query="select total_admission from year_collegedetail where college_code=%s && Branch=%s && year=%s"
                cursor=cn.cursor()
                cursor.execute(query,(self.cmbcode.currentText(),self.cmbbranch.currentText(),self.cmbyear.currentText()))
                totalrow=cursor.fetchone()
                if totalrow!=None:

                    for data in totalrow:
                        self.passbox.setMaximum(int(data))
            else:
                msg.messagebox("Select year")
    def senddata(self):
        cn = db.createconnection()
        code = self.cmbcode.currentText()
        if code=="Select":
            msg.messagebox("Please select college code")
        else:
            branch=self.cmbbranch.currentText()
            if branch!="Select":
                clgname=self.lblname.text()
                year=self.cmbyear.currentText()
                passs=self.passbox.value()
                querycheck = "select * from passratio where college_code=%s && branch=%s && year=%s"
                cursor=cn.cursor()
                a=cursor.execute(querycheck,(code,branch,year))
                if(a):
                    msg.messagebox("This record already exsist")
                else:
                    query1="select total_admission from year_collegedetail where college_code=%s && Branch=%s && year=%s"
                    cursor1=cn.cursor()
                    cursor1.execute(query1,(code,branch,year))
                    tota=cursor1.fetchall()
                    for data in tota:
                        a=int(data[0])
                        passrat=(passs*100)//a



                    query="insert into passratio(college_code,college_name,branch,passed,year,passratio) values(%s,%s,%s,%s,%s,%s)"
                    cursor=cn.cursor()
                    cursor.execute(query,(code,clgname,branch,passs,year,passrat))
                    cn.commit()
                    msg.messagebox("Accepted")
            else:
                msg.messagebox("Select any branch")


    def __init__(self):
        super(passing,self).__init__()
        loadUi("passing.ui",self)

        self.populatecode()

        self.cmbcode.currentIndexChanged.connect(self.populatecollege)



        self.cmbyear.currentIndexChanged.connect(self.populatebranch)
        # self.cmbyear.currentIndexChanged.connect(self.cmbbranch.clear)

        self.cmbbranch.currentIndexChanged.connect(self.populatepassing)
        self.btnsubmit.clicked.connect(self.senddata)


if __name__=="__main__":
    import sys
    app=QApplication(sys.argv)
    objpass=passing()
    objpass.show()
    sys.exit(app.exec())