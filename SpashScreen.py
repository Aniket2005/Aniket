"""
Python Tkinter Splash Screen

This script holds the class SplashScreen, which is simply a window without
the top bar/borders of a normal window.

The window width/height can be a factor based on the total screen dimensions
or it can be actual dimensions in pixels. (Just edit the useFactor property)

Very simple to set up, just create an instance of SplashScreen, and use it as
the parent to other widgets inside it.

"""

from tkinter import *
from threading import Thread, Event
import time

from SplashScreen2 import stop_event, do_actions


class SplashScreen(Frame):
    def __init__(self, master=None, width=0.8, height=0.6, useFactor=True):
        Frame.__init__(self, master)
        self.pack(side=TOP, fill=BOTH, expand=YES)

        # get screen width and height
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        w = (useFactor and ws * width) or width
        h = (useFactor and ws * height) or height
        # calculate position x, y
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.master.overrideredirect(True)
        self.lift()

    stop_event = Event()

    # def do_actions(self):
    #     """
    #     Function that should timeout after 5 seconds. It simply prints a number and waits 1 second.
    #     :return:
    #     """
    #     i = 0
    #     while True:
    #         i += 1
    #         print(i)
    #         time.sleep(1)
    #
    #         # Here we make the check if the other thread sent a signal to stop execution.
    #         if stop_event.is_set():
    #             break


# if __name__ == '__main__':
#     root = Tk()
#
#
#     sp = SplashScreen(root)
#     sp.config(bg="#228B22")
#
#     m = Label(sp, text="Welcome to College Rating App")
#     m.pack(side=TOP, expand=YES)
#     m.config(bg="#228B22", justify=CENTER, font=("monotype corsiva", 29))
#
#     Button(sp, text="Press this button to kill the program", bg='red', command=root.destroy).pack(side=BOTTOM, fill=X)
#
#     # We create another Thread
#     action_thread = Thread(target=do_actions)
#
#     # Here we start the thread and we wait 5 seconds before the code continues to execute.
#     action_thread.start()
#
#     stop_event.set()
#
#     action_thread.join(timeout=5)
#     root.after(5000, root.destroy)
#     root.mainloop()
#
#
#     # We send a signal that the other thread should stop.
#
#
#     print("Hey there! I timed out! You can do things after me!")
#
