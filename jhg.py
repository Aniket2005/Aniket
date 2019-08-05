from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from managerlogin import *
from addCollege import *
from collegedetails import *
from managerprofile import Managerprofile
from Connection import dbconnection as db
import pymysql


class manager(QMainWindow):

    def add(self, o):
        self.o = addCollege()
        self.o.show()

    def clgdetail(self, objjj):
        self.objjj = collegedetails()
        self.objjj.show()

    def updatedata(self, obj):
        self.user = self.lbluser.text()
        self.obj = Managerprofile()
        self.obj.show()
        self.obj.txtuserid.setText(self.user)

    def signout(self, objj):
        import managerlogin
        self.objj = managerlogin.managerlogin()
        self.objj.show()
        self.close()

    def __init__(self):
        super(manager, self).__init__()
        loadUi("manager.ui", self)
        # self.adminbtn.clicked.connect(self.displayy)
        # self.update.triggered.connect(self.update)
        # self.logout.triggered.connect(self.logout)

        self.update.triggered.connect(lambda: self.updatedata(self.update))
        self.logout.triggered.connect(lambda: self.signout(self.logout))
        self.actionclgdetail.triggered.connect(lambda: self.clgdetail(self.actionclgdetail))
        self.btnadd.clicked.connect(self.add)


import managerlogin_rc
#
# if __name__ == "__main__":
#     import sys
#
#     app = QApplication(sys.argv)
#
#     ob = manager()
#     ob.show()
#     sys.exit(app.exec())