
from tkinter import *
from PIL import ImageTk, Image
#import os

root = Tk()
root.geometry('1000x768')

Tframe = Frame(root)
Tframe.pack(side = TOP)




frame1 = Frame(Tframe)
frame2 = Frame(Tframe)
root.config(background = 'blue')


frame1.pack(side = LEFT)
frame2.pack(side = RIGHT)


# separator = Frame(height = 10, bd = 100, relief = GROOVE)
# separator.pack(fill = 0X, padx = 5, pady = 5)

Bframe=Frame(root)
# Bframe.geometry('300x250')
Bframe.pack(side = BOTTOM)

#path = "img3.png"
#imagv = ImageTk.PhotoImage(Image.open(path))
#l1 = Label(frame1,image = imagv)
#l1.pack()



# creating a toolbara
toolbar = Frame(Tframe,bg = 'aquamarine ')
insertB1 = Button(toolbar, text = "Graph Visual",fg = 'brown')
insertB1.pack(side = LEFT, padx = 2, pady = 2)
insertB2 = Button(toolbar, text = "Check ID",fg = "brown")
insertB2.pack(side = LEFT, padx=2, pady = 2)
insertB3 = Button(toolbar, text = "Exit", fg = 'brown')
insertB3.pack(side = RIGHT, padx = 2, pady = 2)


#l2 = Label(frame2,image = imagv)
#l2.pack(side = RIGHT)
#img = ImageTk.PhotoImage(Image.open("img3.png"))
#panel = Label(frame, image = img)

#panel.config(heght = 20,width = 30)
#panel.pack(side = "bottom", fill = "both", expand = "yes")
root.mainloop()