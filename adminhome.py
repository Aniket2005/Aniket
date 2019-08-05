from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi
from Connection import dbconnection as db
from addmanager import Addmanager
from admin_result import admin_result
from chartbranchwisepassratio import chartbranch
from yearwisechart import yearwiseplot
from surveychart import surveychart
from seeplacement import seeplacement

from updatemanager import*
import pymysql
from admin_collegedetail import admin_collegedetail
from deleteaccount import Deleteaccount
from branchdetails import branchDetails
from placement import placement
class Adminhome(QMainWindow):
    def out(self):
        import admin
        self.objad=admin.admin()
        self.objad.show()
        self.close()

    def updatemanager(self):
        self.obj=Updatemanager()
        self.obj.show()
    def addacc(self):
       self.objj=Addmanager()
       self.objj.show()


    def populatetable(self):
        cn=db.createconnection()
        query="select * from manager"
        cursor=cn.cursor()
        a=cursor.execute(query)
        self.tblmanager.setRowCount(a)
        totalrow=cursor.fetchall()
        for rowno,rowdata in enumerate(totalrow):
            for colno,coldata in enumerate(rowdata):
                self.tblmanager.setItem(rowno,colno,QTableWidgetItem(str(coldata)))
    def branchde(self):
        self.op=branchDetails()
        self.op.show()
    def clgbasic(self):
        self.ojcoll=admin_collegedetail()
        self.ojcoll.show()
    def res(self):
        self.aaa=admin_result()
        self.aaa.show()
    def brplot(self):
        self.objpl=chartbranch()
        self.objpl.show()
    def dell(self):
        self.delll=Deleteaccount()
        self.delll.show()
    def pl(self):
        self.ol=seeplacement()
        self.ol.show()
    def plo(self):
        self.olo=yearwiseplot()
        self.olo.show()
    def lon(self):
        self.sh=surveychart()
        self.sh.show()
    def __init__(self):
        super(Adminhome,self).__init__()
        loadUi("adminhome.ui",self)
        self.tblmanager.setHorizontalHeaderLabels(("Name","Email","UserId","Password"))
        self.populatetable()
        self.actionaddaccount.triggered.connect(self.addacc)
        self.btnrefresh.clicked.connect(self.populatetable)
        self.actionupdateaccount.triggered.connect(self.updatemanager)
        self.actionlogout.triggered.connect(self.out)
        self.actionCollegeBasicDetail.triggered.connect(self.clgbasic)
        self.actionResult.triggered.connect(self.res)
        self.actionBranch_Wise.triggered.connect(self.brplot)
        self.actiondeleteaccount.triggered.connect(self.dell)
        self.actionCollegeBranchDetails.triggered.connect(self.branchde)
        self.actionPlacements.triggered.connect(self.pl)
        self.actionYearwise.triggered.connect(self.plo)
        self.actionRating.triggered.connect(self.lon)
import adminhomeresource_rc
if __name__=="__main__":
    import sys
    app=QApplication(sys.argv)
    objadminhome=Adminhome()
    objadminhome.show()
    sys.exit(app.exec())