from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from Connection import dbconnection as db
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
class chartbranch(QMainWindow):
    def populatecode(self):
        cn=db.createconnection()
        query="select college_code from add_college"
        cursor=cn.cursor()
        cursor.execute(query)
        totalrow=cursor.fetchall()
        for data in totalrow:
            self.cmbcode.addItems(data)

    def populatecollege(self):
        self.cmbbranch.clear()
        cn = db.createconnection()
        code = self.cmbcode.currentText()
        query = "select college_name from add_college where college_code=%s"
        cursor = cn.cursor()
        cursor.execute(query, (code))
        totalrow = cursor.fetchone()
        for data in totalrow:
            self.txtname.setText(data)
        query1 = "select branch from college_details where college_code=%s"
        cursor1 = cn.cursor()
        cursor1.execute(query1, (code))
        totalrow1 = cursor1.fetchall()
        for data1 in totalrow1:
            self.cmbbranch.addItems(data1)
    def plotchart(self):
        cn=db.createconnection()
        code=self.cmbcode.currentText()
        name=self.txtname.text()
        branch=self.cmbbranch.currentText()
        query="select passratio from passratio where college_code=%s && branch=%s"
        cursor=cn.cursor()
        cursor.execute(query,(code,branch))
        totalrow=cursor.fetchall()
        a=[]
        for data in totalrow:
            for i in range(len(data)):
                a.append(int(data[i]))

        print(a)
        query1 = "select year from passratio where college_code=%s && branch=%s"
        cursor1 = cn.cursor()
        cursor1.execute(query1, (code, branch))
        totalrow = cursor1.fetchall()
        b= []
        for data in totalrow:
            for i in range(len(data)):
                b.append(int(data[i]))


        plt.plot(b,a,label="Passing Ratio vs Year")
        plt.xlabel("Year")
        plt.ylabel("Passing Ratio")
        plt.legend()
        plt.show()
        # plt.plot([10, 20, 30, 40, 50], [40, 50, 60, 70, 80], label="India")
        # plt.plot([10, 20, 30, 40, 50], [30, 50, 20, 80, 10], label="Australia")
        # plt.xlabel("Over")
        # plt.ylabel("runs")
        # plt.title("runsdemo")
        # plt.legend()
        # plt.show()



    def __init__(self):
        super(chartbranch,self).__init__()
        loadUi("chart_passratio_branchwise.ui",self)
        self.populatecode()
        self.cmbcode.currentIndexChanged.connect(self.populatecollege)
        self.btnchart.clicked.connect(self.plotchart)
if __name__=="__main__":
    import sys
    app=QApplication(sys.argv)
    obj=chartbranch()
    obj.show()
    sys.exit(app.exec())
