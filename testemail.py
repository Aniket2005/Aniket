
import smtplib
class mail:

    @staticmethod
    def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):



            server = smtplib.SMTP(smtpserver)
            server.starttls()
            server.login(login, password)
            problems = server.sendmail(from_addr, to_addr_list, message)
            server.quit()

# sendemail(from_addr    = '1104anshuman@gmail.com',
#           to_addr_list = ['mishrapriya1402@gmail.com'],
#           cc_addr_list = ['anshumansrivastava007@gmail.com'],
#           subject      = 'OTP',
#           message      = 'chudail kahin ki from python :))',
#           login        = '1104anshuman@gmail.com',
#           password     = 'ansh1104')