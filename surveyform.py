from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi
from Connection import dbconnection as db
import pymysql as py
import matplotlib.pyplot
class surveyform(QMainWindow):


    def populatecollegecombo(self):
        cn=db.createconnection()
        query="select college_code from add_college"
        cursor=cn.cursor()
        cursor.execute(query)
        totalrow=cursor.fetchall()
        for data  in totalrow:
            self.comboBox.addItems(data)
    def populatecollegecode(self):
        cn = db.createconnection()
        self.clgcode=self.comboBox.currentText()
        query="select college_name from add_college where college_code=%s"
        cursor = cn.cursor()
        cursor.execute(query,(self.clgcode))
        totalrow=cursor.fetchone()
        for data in totalrow:
            self.clgname.setText(data)
        self.clgname.setReadOnly(True)

    def insdata(self):
        self.clgcode = self.comboBox.currentText()
        self.collegename = self.clgname.text()
        self.placemen=self.placement.text()
        self.disciplin=self.discipline.text()
        self.passingratio=self.passratio.text()
        self.infrastructure=self.infra.text()
        # print(self.clgname)
        # print(self.clgcode)
        # print(self.branch)
        # print(self.fees)
        # print(self.duration)
        cn = db.createconnection()
        query = "insert into surveyform(College_name,College_code,Placement,Discipline,PassingRatio,Infrastructure) values(%s,%s,%s,%s,%s,%s)"
        cursor = cn.cursor()
        cursor.execute(query, (self.collegename, self.clgcode, self.placemen,self.disciplin, self.passingratio, self.infrastructure))
        # query1 = "select college_name,branch from college_details where college_name=%s && branch=%s"
        # cursor1 = cn.cursor()
        # a = cursor1.execute(query1, (self.clgname, self.branch))
        # if (a == 1):
        cn.commit()


    def __init__(self):
        super(surveyform,self).__init__()
        loadUi("surveyform.ui",self)
        self.populatecollegecombo()
        self.comboBox.currentIndexChanged.connect(self.populatecollegecode)
        self.btnsubmit.clicked.connect(self.insdata)
        #self.pushButtonExit.clicked.connect(self.exitdata)

import managerlogin_rc
if __name__=="__main__":
    import sys

    app=QApplication(sys.argv)

    obj=surveyform()
    obj.show()
    sys.exit(app.exec())