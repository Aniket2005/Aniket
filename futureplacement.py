from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from Connection import dbconnection as db
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
class placementpredict(QMainWindow):
    def populatecode(self):
        cn=db.createconnection()
        query="select distinct college_code from overallpassratio"
        cursor=cn.cursor()
        cursor.execute(query)
        totalrow=cursor.fetchall()
        for data in totalrow:
            self.cmbcode.addItems(data)

    def populatecollegename(self):
        cn = db.createconnection()
        code = self.cmbcode.currentText()
        query = "select college_name from overallpassratio where college_code=%s"
        cursor = cn.cursor()
        cursor.execute(query, (code))
        totalrow = cursor.fetchone()
        for data in totalrow:
            self.clgname.setText(data)
    def pred(self):
      if self.cmbcode.currentText() != "Select":
        cn=db.createconnection()
        query="select placed from overallpassratio where college_code=%s"
        cursor=cn.cursor()
        cursor.execute(query,(self.cmbcode.currentText()))
        totalrow=cursor.fetchall()
        listpass1=[]
        for data in totalrow:
            listpass1.append(data[0])
        a=[]
        b=[]
        c=[]
        d=[]
        e=[]
        f=[]
        a.append(listpass1[0])
        b.append(listpass1[1])
        c.append(listpass1[2])
        d.append(listpass1[3])
        e.append(listpass1[4])
        f.append(listpass1[5])
        passarray=np.array([a,b,c,d,e,f])
        print(passarray)

        cn = db.createconnection()
        query = "select year from overallpassratio where college_code=%s"
        cursor = cn.cursor()
        cursor.execute(query, (self.cmbcode.currentText()))
        totalrow = cursor.fetchall()
        listyear1 = []
        for data in totalrow:
            listyear1.append(data[0])
        aa = []
        bb = []
        cc = []
        dd = []
        ee = []
        ff = []
        aa.append(listyear1[0])
        bb.append(listyear1[1])
        cc.append(listyear1[2])
        dd.append(listyear1[3])
        ee.append(listyear1[4])
        ff.append(listyear1[5])
        yeararray = np.array([aa, bb, cc, dd, ee, ff])
        print(yeararray)
        # X_train,y_train=train_test_split(yeararray,passarray)
        X_train=yeararray
        y_train=passarray
        X_test=[[2019],[2020],[2021],[2022],[2023],[2024]]
        y_test=[[],[],[],[]]
        regressor=LinearRegression()
        regressor.fit(X_train,y_train)
        y_predictor=regressor.predict(X_test)
        # plt.scatter(X_test,y_test)
        plt.plot(X_test,y_predictor)
        plt.show()

      else:
         self.showMessage("Error!! College code not selected")


    def showMessage(self, message):
      msg = QMessageBox()
      msg.setWindowTitle("Error")

      msg.setText(message)
      msg.exec()

    def __init__(self):
        super(placementpredict,self).__init__()
        loadUi("futureplacement.ui",self)
        self.populatecode()
        self.cmbcode.currentIndexChanged.connect(self.populatecollegename)
        self.btnpredict.clicked.connect(self.pred)
import addcollegeresource_rc
if __name__=="__main__":
    import sys
    app=QApplication(sys.argv)
    obj=placementpredict()
    obj.show()
    sys.exit(app.exec())