
from tkinter import *
from sys import *
import os
top = Tkinter.Tk()

def helloCallBack():
    os.system('kmeans.py')

B = Tkinter.Button(top, text = "hello", command = helloCallBack)
B.pack()
top.mainloop()