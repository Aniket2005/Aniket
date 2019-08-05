from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from Connection import dbconnection as db
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
class placementchart(QMainWindow):

    def populatecode(self):
        cn=db.createconnection()
        query="select college_code from add_college"
        cursor=cn.cursor()
        cursor.execute(query)
        totalrow=cursor.fetchall()
        for data in totalrow:
            self.comboBoxcode.addItems(data)

    def populatecollege(self):
        self.comboBoxcourse.clear()
        cn = db.createconnection()
        code = self.comboBoxcode.currentText()
        query = "select college_name from add_college where college_code=%s"
        cursor = cn.cursor()
        cursor.execute(query, (code))
        totalrow = cursor.fetchone()
        for data in totalrow:
            self.clgname.setText(data)
        query1 = "select branch from college_details where college_code=%s"
        cursor1 = cn.cursor()
        cursor1.execute(query1, (code))
        totalrow1 = cursor1.fetchall()
        for data1 in totalrow1:
            self.comboBoxcourse.addItems(data1)
    def plotchart(self):
        cn=db.createconnection()
        code=self.comboBoxcode.currentText()
        name=self.clgname.text()
        branch=self.comboBoxcourse.currentText()
        query="select Placed from passratio where college_code=%s && branch=%s"
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


        plt.plot(b,a,label="Placement vs Year")
        plt.xlabel("Year")
        plt.ylabel("Placement")
        plt.legend()
        plt.show()



    def __init__(self):
        super(placementchart,self).__init__()
        loadUi("placementchart.ui",self)
        self.populatecode()
        self.comboBoxcode.currentIndexChanged.connect(self.populatecollege)
        self.btnchart.clicked.connect(self.plotchart)
if __name__=="__main__":
    import sys
    app=QApplication(sys.argv)
    obj=placementchart()
    obj.show()
    sys.exit(app.exec())
