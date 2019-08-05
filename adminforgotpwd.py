from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from Connection import dbconnection as db
from msg import msg
from random import randint
from testemail import mail
from adminresetpwd import adminreset
class adminforgotpwd(QMainWindow):
    def sendotp(self):
        email=self.txtemail.text()
        if email=="":
            msg.messagebox("Email Id cannot be Empty")
        else:
            if email=="1104anshuman@gmail.com":
                self.otp=randint(1001,9999)
                mail.sendemail(from_addr='1104anshuman@gmail.com',
                to_addr_list = ['1104anshuman@gmail.com'],
                cc_addr_list = ['anshumansrivastava007@gmail.com'],
                subject      = 'OTP',
                message      = str(self.otp),
                login        = '1104anshuman@gmail.com',
                password     = 'ansh4011')
                self.lblmsg.setText("OTP has been sent to your mail")
                self.txtotp.setReadOnly(False)
            else:
                msg.messagebox("Email Id not matched")
    def check(self):
        otpp = self.txtotp.text()
        if self.txtemail.text()=="":
            msg.messagebox("Please enter email")
        else:
            if otpp=="":
                msg.messagebox("Please enter OTP")
            else:
                if int(otpp)==self.otp:
                    self.aaa=adminreset()
                    self.aaa.show()
                    self.close()
                else:
                    msg.messagebox("OTP doesnot match")


    def __init__(self):
        super(adminforgotpwd,self).__init__()
        loadUi("adminforgotpwd.ui",self)
        self.btnsubmit.clicked.connect(self.check)
        self.btnotp.clicked.connect(self.sendotp)
        self.txtotp.setReadOnly(True)
import forgotpwd_rc
if __name__=="__main__":
    import sys
    app=QApplication(sys.argv)
    obj=adminforgotpwd()
    obj.show()
    sys.exit(app.exec())