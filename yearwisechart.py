from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from Connection import dbconnection as db
import matplotlib.pyplot as plt
class yearwiseplot(QMainWindow):
    def populatecode(self):
        cn=db.createconnection()
        query="select distinct college_code from passratio"
        cursor=cn.cursor()
        cursor.execute(query)
        totalrow=cursor.fetchall()
        for data in totalrow:
            self.cmbcode.addItems(data)
    def populateyear(self):
        code = self.cmbcode.currentText()
        cn=db.createconnection()
        query="select distinct year from passratio where college_code=%s"
        cursor=cn.cursor()
        cursor.execute(query,(code))
        totalrow=cursor.fetchall()
        for data in totalrow:
            self.cmbyear.addItems(data)
    def populatecollege(self):
            self.cmbyear.clear()
            cn = db.createconnection()
            code = self.cmbcode.currentText()
            query = "select college_name from passratio where college_code=%s"
            cursor = cn.cursor()
            cursor.execute(query, (code))
            totalrow = cursor.fetchone()
            for data in totalrow:
                self.txtclgname.setText(data)

            self.populateyear()
    def plotchart(self):
        cn = db.createconnection()
        code = self.cmbcode.currentText()
        year=self.cmbyear.currentText()
        query = "select passratio from passratio where college_code=%s && year=%s"
        cursor = cn.cursor()
        cursor.execute(query, (code,year))
        totalrow = cursor.fetchall()
        a = []
        for data in totalrow:
            for i in range(len(data)):
                a.append(int(data[i]))

        print(a)
        query1 = "select branch from passratio where college_code=%s && year=%s"
        cursor1 = cn.cursor()
        cursor1.execute(query1, (code,year))
        totalrow = cursor1.fetchall()
        b = []
        for data in totalrow:
            for i in range(len(data)):
                b.append(data[i])

        plt.plot(b, a, label="Passing Ratio vs Courses")
        plt.xlabel("Courses")
        plt.ylabel("Passing Ratio")
        plt.legend()
        plt.show()

    def __init__(self):
        super(yearwiseplot,self).__init__()
        loadUi("yearwisechart.ui",self)
        self.populatecode()
        self.cmbcode.currentIndexChanged.connect(self.populatecollege)
        self.btnsubmit.clicked.connect(self.plotchart)
import yearwise_rc
if __name__=="__main__":
    import sys
    app=QApplication(sys.argv)
    obj=yearwiseplot()
    obj.show()
    sys.exit(app.exec())