from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi
from manager import *
from managerprofile import *
from Connection import dbconnection as db
from PyQt5.QtWidgets import QMessageBox
from addmanager import Addmanager
from home import homepy


class managerlogin(QMainWindow):

    def forgot(self):

        self.showMessage2("Consult to admin")

    def homebutton(self):
        self.o =homepy()
        self.o.show()
        self.close()

    def displayy(self):

        self.userid = self.txtusername.text()
        self.userpass = self.txtpass.text()
        con = db.createconnection()
        query = "select UserId,Password from manager where UserId=%s && Password=%s"
        cursor = con.cursor()
        a = cursor.execute(query,(self.userid,self.userpass))

        rows=cursor.fetchone()

        if(a):
            self.o=manager()
            self.o.show()
            self.o.lbluser.setText(self.userid)
            self.close()
            # self.showMessage("Congratulations !!!  You are successfully logged in\n\nClick ok to continue       ")
        elif self.userid.__eq__("") | self.userpass.__eq__(""):
            self.showMessage1("User Id or password can not be blank")
        else:
            self.showMessage1("Invalid User Id and password")
        # print(rows[1][0])
        # print(len(rows))
        # for i in range(len(rows)):
        #     if userid.__eq__(rows[i][2])& userpass.__eq__(rows[i][3]):
        #         self.showMessage("Congratulations !!!  You are successfully logged in\n\nClick ok to continue       ")
        # if userid.__eq__("") | userpass.__eq__(""):
        #     self.showMessage1("User Id or password can not be blank")
        # if userid!=(rows[i][2])| userpass!=(rows[i][3]):
        #     self.showMessage1("Invalid User Id or password")


    def showMessage(self,message):
            msg = QMessageBox()
            msg.setWindowTitle("Welcome")
            #msg.setIcon(QMessageBox.Information)
            msg.setText(message)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.buttonClicked.connect(self.dlgbutton)
            msg.exec()

    def showMessage1(self,message):
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setIcon(QMessageBox.Information)
            msg.setText(message)
            #msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()

    def showMessage2(self, message):
        msg = QMessageBox()
        msg.setWindowTitle("Recover")
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        # msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()

    # def dlgbutton(self, buttonvalue):
    #     caption = buttonvalue.text()
        # if caption == "OK":
        #     #self.appp=QApplication(sys.argv)
        #     self.objjj = Managerprofile()
        #     self.objjj.show()
        #     #self.objjj.set
        #     #obj.close()



    def __init__(self):
        super(managerlogin,self).__init__()
        loadUi("managerlogin.ui",self)
        self.btnlogin.clicked.connect(self.displayy)
        self.btnforgotpass.clicked.connect(self.forgot)
        self.btnhome.clicked.connect(self.homebutton)


import managerlogin_rc
if __name__=="__main__":
    import sys
    app=QApplication(sys.argv)
    obj=managerlogin()
    obj.show()
    sys.exit(app.exec())
