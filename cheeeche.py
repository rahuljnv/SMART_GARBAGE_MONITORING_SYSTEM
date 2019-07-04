from tkinter import *



class check:
    def __init__(self, master):
        Tframe = Frame(master)
        Tframe.pack()
        #self.toolbar = Frame(Tframe, bg='aquamarine ')
        #self.insertB1 = Button(self.toolbar, text="Graph Visual", fg='brown')
        #self.insertB1.pack(side=LEFT, padx=2, pady=2)
        #self.insertB2 = Button(self.toolbar, text="Check ID", fg="brown")
        #self.insertB2.pack(side=LEFT, padx=2, pady=2)
        #self.insertB3 = Button(self.toolbar, text="Exit", fg='brown',command=quit)
        #self.insertB3.pack(side=RIGHT, padx=2, pady=2)



root = Tk()
root.geometry('1000x768')
b = check(root)
root.config(bg = 'aqua')
root.mainloop()

