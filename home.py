from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import pyttsx3
from tkinter import *
from threading import Thread, Event
import time

from SpashScreen import SplashScreen
from SplashScreen2 import stop_event, do_actions


class homepy(QMainWindow):
    def dispmanager(self):
        import managerlogin
        self.manlogin = managerlogin.managerlogin()
        self.manlogin.show()
        self.close()

    def displayy(self):
        import admin

        self.objadmin = admin.admin()
        self.objadmin.show()

        self.close()

    def __init__(self):
        super(homepy, self).__init__()
        loadUi("home.ui", self)
        self.adminbtn.clicked.connect(self.displayy)
        self.managerbtn.clicked.connect(self.dispmanager)


import homeresource_rc

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    engine = pyttsx3.init()

    root = Tk()

    sp = SplashScreen(root)
    sp.config(bg="#228B22")

    m = Label(sp, text="Welcome to College Rating App")
    m.pack(side=TOP, expand=YES)
    m.config(bg="#228B22", justify=CENTER, font=("monotype corsiva", 29))

    Button(sp, text="Press this button to kill the program", bg='red', command=root.destroy).pack(side=BOTTOM, fill=X)

    # We create another Thread
    action_thread = Thread(target=do_actions)

    # Here we start the thread and we wait 5 seconds before the code continues to execute.
    action_thread.start()

    stop_event.set()

    action_thread.join(timeout=5)
    root.after(5000, root.destroy)
    root.mainloop()

    engine.say("welcome to college rating app")
    engine.setProperty('rate', 10)
    engine.setProperty('volume', 0.9)
    engine.runAndWait()

    objhome = homepy()
    objhome.show()

    print("Hey there! I timed out! You can do things after me!")
    sys.exit(app.exec())

    # We send a signal that the other thread should stop.
