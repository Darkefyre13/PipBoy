import sys
#import tkinter
import tkinter as tk
import time
from tkinter import constants
from tkinter import *
from tkinter.ttk import Progressbar


root = Tk()
root.title('PipBoy3k')

def bar():
    import time
    progress['value']=20
    tk.update_idletasks()
    time.sleep(1)
    progress['value']=50
    tk.update_idletasks()
    time.sleep(1)
    progress['value']=80
    tk.update_idletasks()
    time.sleep(1)
    progress['value']=100
    Loading.pack_forget()

root.mainloop()
