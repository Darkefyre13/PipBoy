import sys
import tkinter
import time
from tkinter import constants
from tkinter import Tk, Label


root = Tk()
root.title('PipBoy3k')
root.geometry("800x480+50+50")


text_loading = Label(root, text='Loading, Please Wait')
text_loading.config(font=('times', 48))
text_loading.pack()
time.sleep(5)
text_loading.pack_forget()


root.mainloop()
