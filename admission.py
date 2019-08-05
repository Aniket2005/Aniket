from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from Connection import dbconnection as db
from msg import msg
class admission(QMainWindow):
    def populatecode(self):
        cn=db.createconnection()
        query="select college_code from add_college"
        cursor=cn.cursor()
        cursor.execute(query)
        totalrow=cursor.fetchall()
        for data in totalrow:
            self.cmbcode.addItems(data)
    def populatecollege(self):
        if self.cmbcode.currentText()=="Select":
            self.lblname.setText("")
            # self.cmbbranch.currentIndex
        else:

            self.cmbbranch.clear()
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
        # self.populatebranch()
    def senddata(self):
        cn = db.createconnection()
        code = self.cmbcode.currentText()
        if code=="Select":
            msg.messagebox("Please select college code")
        else:
            branch=self.cmbbranch.currentText()
            if branch=="":
                msg.messagebox("Please select branch")
            else:
                if branch!="Select":
                    clgname=self.lblname.text()
                    year=self.yearbox.value()
                    adm=self.passbox.value()
                    querycheck = "select * from year_collegedetail where college_code=%s && Branch=%s && year=%s"
                    cursor=cn.cursor()
                    a=cursor.execute(querycheck,(code,branch,year))
                    if(a):

                        msg.messagebox("This record already exsist")
                    else:
                        query="insert into year_collegedetail(college_code,college_name,Branch,total_admission,year) values(%s,%s,%s,%s,%s)"
                        cursor=cn.cursor()
                        cursor.execute(query,(code,clgname,branch,adm,year))
                        cn.commit()
                        msg.messagebox("Accepted")
                else:
                    msg.messagebox("Select any branch")

    def __init__(self):
        super(admission,self).__init__()
        loadUi("admission.ui",self)
        self.populatecode()
        self.cmbcode.currentIndexChanged.connect(self.populatecollege)
        # self.cmbbranch.clear()
        self.btnsubmit.clicked.connect(self.senddata)

if __name__=="__main__":
    import sys
    app=QApplication(sys.argv)
    objadmission=admission()
    objadmission.show()
    sys.exit(app.exec())