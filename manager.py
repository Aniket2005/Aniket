from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi
from managerlogin import *
from addCollege import *
from yearchart import yearchart
from placementchart import placementchart
from futureplacement import placementpredict
from collegedetails import *
from managerprofile import Managerprofile
from Connection import dbconnection as db
import pymysql
from testfut import resultpredict
from surveyform import surveyform
from chartbranchwisepassratio import chartbranch
from yearwisechart import yearwiseplot
from surveychart import surveychart

from passing import passing
from placement import placement
from admission import admission

class manager(QMainWindow):
    def rr(self):
        self.bcd=passing()
        self.bcd.show()

    def add(self,o):
        self.o=addCollege()
        self.o.show()

    def clgdetail(self,objjj):
        self.objjj=collegedetails()
        self.objjj.show()

    def updatedata(self,obj):
        self.user=self.lbluser.text()
        self.obj = Managerprofile()
        self.obj.show()
        self.obj.txtuserid.setText(self.user)


    def signout(self,objj):
        import managerlogin
        self.objj = managerlogin.managerlogin()
        self.objj.show()
        self.close()
    def admm(self):
        self.abc=admission()
        self.abc.show()
    def pll(self):
        self.asc=placement()
        self.asc.show()
    def m(self):
        self.n=surveyform()
        self.n.show()
    def ma(self):
        self.na=yearwiseplot()
        self.na.show()
    def co(self):
        self.naa=placementchart()
        self.naa.show()
    def predictb(self):
        self.naaa=placementpredict()
        self.naaa.show()
    def maa(self):
        self.kl=chartbranch()
        self.kl.show()
    def pre(self):
        self.lki=resultpredict()
        self.lki.show()

    def maaa(self):
        self.kll =yearchart()
        self.kll.show()
    def maaaa(self):
        self.kl=surveychart()
        self.kl.show()

    def __init__(self):
        super(manager, self).__init__()
        loadUi("manager.ui", self)
        #self.adminbtn.clicked.connect(self.displayy)
        # self.update.triggered.connect(self.update)
        # self.logout.triggered.connect(self.logout)

        self.update.triggered.connect(lambda: self.updatedata(self.update))
        self.logout.triggered.connect(lambda: self.signout(self.logout))
        self.actionclgdetail.triggered.connect(lambda: self.clgdetail(self.actionclgdetail))
        self.btnadd.clicked.connect(self.add)
        self.actionAdmissions.triggered.connect(self.admm)
        self.actionPlacement.triggered.connect(self.pll)
        self.actionResult.triggered.connect(self.rr)
        self.actionFillForm.triggered.connect(self.m)
        self.actionResultYearwise.triggered.connect(self.ma)
        self.actionResult_Course_wise.triggered.connect(self.maa)
        self.actionPlacement_year_wise.triggered.connect(self.maaa)
        self.actionRatings.triggered.connect(self.maaaa)
        self.actionPlacement_Course_wise.triggered.connect(self.co)
        self.actionpredict_by_placement.triggered.connect(self.predictb)
        self.actionPredict_by_result.triggered.connect(self.pre)


import managerlogin_rc

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    ob = manager()
    ob.show()
    sys.exit(app.exec())