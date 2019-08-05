from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from msg import msg
from Connection import dbconnection as db
import pymysql
class placement(QMainWindow):

    # def populatepasscombo(self):
    #     cn=db.createconnection()
    #     code=self.comboBoxcode.currentText()
    #     query="select passed from passratio where college_code=%s"
    #     cursor=cn.cursor()
    #     cursor.execute(query,(code))
    #     totalrow=cursor.fetchone()
    #     for data in totalrow:
    #         print(data)
    #         self.placed.setMaximum(int(data))

    def populatecode(self):
        cn=db.createconnection()
        query="select distinct college_code from passratio"
        cursor=cn.cursor()
        cursor.execute(query)
        totalrow=cursor.fetchall()
        for data in totalrow:
            self.comboBoxcode.addItems(data)

    def populatecollegecode(self):
        cn = db.createconnection()
        self.clgcode=self.comboBoxcode.currentText()
        query="select college_name from passratio where college_code=%s"
        cursor = cn.cursor()
        cursor.execute(query,(self.clgcode))
        totalrow=cursor.fetchone()
        for data in totalrow:
            self.clgname.setText(data)
        self.clgname.setReadOnly(True)

        self.populateyear()

    def populateyear(self):
        #code = self.comboBoxcode.currentText()
        cn = db.createconnection()
        query = "select distinct year from passratio where college_code=%s"
        cursor = cn.cursor()
        cursor.execute(query,(self.clgcode))
        totalrow = cursor.fetchall()
        for data in totalrow:
            self.comboBoxyear.addItems(data)

    def populatebranch(self):
        self.comboBoxbranch.clear()
        # self.cmbbranch.addItem("Select")
        #code=self.comboBoxcode.currentText()
        cn=db.createconnection()
        query="select distinct branch from passratio where college_code=%s && year=%s"
        cursor=cn.cursor()
        cursor.execute(query,(self.clgcode,self.comboBoxyear.currentText()))
        totalrow=cursor.fetchall()
        for data in totalrow:
            self.comboBoxbranch.addItems(data)
    def populatepassing(self):
            if self.comboBoxyear.currentText()!="Select":
                cn=db.createconnection()
                query="select passed from passratio where college_code=%s && branch=%s && year=%s"
                cursor=cn.cursor()
                cursor.execute(query,(self.clgcode,self.comboBoxbranch.currentText(),self.comboBoxyear.currentText()))
                totalrow=cursor.fetchone()
                if totalrow!=None:

                    for data in totalrow:
                        self.placed.setMaximum(int(data))
            else:
                msg.messagebox("Select year")
    def senddata(self):
        cn = db.createconnection()
        #code = self.comboBoxcode.currentText()
        if self.clgcode=="Select":
            msg.messagebox("Please select college code")
        else:
            branch=self.comboBoxbranch.currentText()
            if branch!="Select":
                clgname=self.clgname.text()
                year=self.comboBoxyear.currentText()
                place=self.placed.value()
                querycheck = "select college_code from passratio where branch=%s && year=%s"
                cursor=cn.cursor()
                a=cursor.execute(querycheck,(branch,year))

                query="update passratio set placed=%s where college_code=%s && branch=%s && year=%s "
                cursor=cn.cursor()
                cursor.execute(query,(place,self.clgcode,branch,year))
                cn.commit()
                msg.messagebox("{0} Students Placed in {1} {2}".format(place,branch,year))
            else:
                msg.messagebox("Select any branch")


    def __init__(self):
        super(placement,self).__init__()
        loadUi("placement.ui",self)

        self.populatecode()

        self.comboBoxcode.currentIndexChanged.connect(self.populatecollegecode)



        self.comboBoxyear.currentIndexChanged.connect(self.populatebranch)
        # self.cmbyear.currentIndexChanged.connect(self.cmbbranch.clear)

        self.comboBoxbranch.currentIndexChanged.connect(self.populatepassing)
        self.btnsubmit.clicked.connect(self.senddata)

import managerlogin_rc
if __name__=="__main__":
    import sys
    app=QApplication(sys.argv)
    objpass=placement()
    objpass.show()
    sys.exit(app.exec())