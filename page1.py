import sys
#import tkinter
import tkinter as tk
import time
from tkinter import constants
from tkinter import Tk, Label, Message, font, Menu, Button, Toplevel
from tkinter.ttk import Progressbar


root = Tk()
root.configure(background='black')
root.title('PipBoy3k')
#root.geometry("800x480+50+50")
root.attributes('-fullscreen', True)

menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Quit", command=root.destroy)

exit_button = Button(root, command=root.destroy)
exit_button.pack(side="bottom")

class Loading(tk.Frame):
    """docstring for loading."""
    def __init__(self, arg):
        super(Loading, self).__init__()
        self.arg = arg
        progress=Progressbar(tk,length=100,mode='determinate')

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


Loading.pack()
root.mainloop()
