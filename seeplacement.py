from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi
from Connection import dbconnection as db
import pymysql
class seeplacement(QMainWindow):

    def populatecombo(self):
        cn=db.createconnection()
        query="select distinct college_code from passratio"
        cursor=cn.cursor()
        cursor.execute(query)
        totalrow=cursor.fetchall()
        for data in totalrow:
            self.comboBoxcode.addItems(data)

    def populatecode(self):
        cn = db.createconnection()
        self.clgcode=self.comboBoxcode.currentText()
        query="select college_name from passratio where college_code=%s"
        cursor = cn.cursor()
        cursor.execute(query,(self.clgcode))
        totalrow=cursor.fetchone()
        for data in totalrow:
            self.clgname.setText(data)
        self.clgname.setReadOnly(True)
        self.populatetable()


    def populatetable(self):
        cn=db.createconnection()
        self.clgcode = self.comboBoxcode.currentText()
        query="select branch,year,Placed from passratio where college_code=%s"
        cursor=cn.cursor()
        a=cursor.execute(query,(self.clgcode))
        self.tableWidget.setRowCount(a)
        totalrow=cursor.fetchall()
        for rowno,rowdata in enumerate(totalrow):
            for colno,coldata in enumerate(rowdata):
                print("hi"+str(coldata))
                self.tableWidget.setItem(rowno,colno,QTableWidgetItem(str(coldata)))
    def __init__(self):
        super(seeplacement,self).__init__()
        loadUi("seeplacement.ui",self)

        self.tableWidget.setHorizontalHeaderLabels(("Course","Year","Placed"))
        self.populatecombo()
        self.comboBoxcode.currentIndexChanged.connect(self.populatecode)


import managerlogin_rc
if __name__=="__main__":
    import sys
    app=QApplication(sys.argv)
    objsee=seeplacement()
    objsee.show()
    sys.exit(app.exec())