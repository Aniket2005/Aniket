from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from Connection import dbconnection as db
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
class surveychart(QMainWindow):
    def populatecode(self):
        cn=db.createconnection()
        query="select college_code from add_college"
        cursor=cn.cursor()
        cursor.execute(query)
        totalrow=cursor.fetchall()
        for data in totalrow:
            self.comboBoxid.addItems(data)

    def populatecollege(self):
        self.comboBoxbranch.clear()
        cn = db.createconnection()
        code = self.comboBoxid.currentText()
        query = "select college_name from add_college where college_code=%s"
        cursor = cn.cursor()
        cursor.execute(query, (code))
        totalrow = cursor.fetchall()
        for data in totalrow:
            self.clgName.setText(data[0])
        query1 = "select branch from college_details where college_code=%s"
        cursor1 = cn.cursor()
        cursor1.execute(query1, (code))
        totalrow1 = cursor1.fetchall()
        for data1 in totalrow1:
            self.comboBoxbranch.addItems(data1)
    def plotchart(self):
        cn=db.createconnection()
        code=self.comboBoxid.currentText()
        name=self.clgName.text()
        branch=self.comboBoxbranch.currentText()
        query="select Placement,Discipline,PassingRatio,Infrastructure from surveyform where College_code=%s"
        cursor=cn.cursor()
        cursor.execute(query,(code))
        totalrow=cursor.fetchall()
        a=[]
        for data in totalrow:
            for i in range(len(data)):
                a.append(int(data[i]))

        print(a)
        listt=["placement","discipline","passingratio","Infrastructure"]
        # query1 = "select Placement,Discipline,PassingRatio,Infrastructure from surveyform where College_code=%s"
        # cursor1 = cn.cursor()
        # cursor1.execute(query1, (code, branch))
        # totalrow = cursor1.fetchall()
        # b= []
        # for data in totalrow:
        #     for i in range(len(data)):
        #         b.append(int(data[i]))


        plt.bar(listt,a,label="Passing Ratio vs Year")
        plt.xlabel("Values")
        plt.ylabel("Ratings")
        plt.legend()
        plt.show()



    def __init__(self):
        super(surveychart,self).__init__()
        loadUi("surveychart.ui",self)
        self.populatecode()
        self.comboBoxid.currentIndexChanged.connect(self.populatecollege)
        self.btngetChart.clicked.connect(self.plotchart)
if __name__=="__main__":
    import sys
    app=QApplication(sys.argv)
    obj=surveychart()
    obj.show()
    sys.exit(app.exec())
