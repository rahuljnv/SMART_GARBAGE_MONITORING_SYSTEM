from tkinter import *

# create a function for button
def butt_graph():
    print("plz connect the module")
def butt_ID():
    print("none ID is available")

# create gui interface of smart bins management system
root = Tk()
root.title("SGMS")
root.geometry('600x500')
root.config(background = 'black')
lbl_1 = Label(root, text = "SMART GARBAGE MONITORING SYSTEM", activebackground = 'blue', activeforeground = 'red', bg = 'red')
lbl_1.config(width = 300, height = 4)
lbl_1.pack(side = TOP)

lbl_2 = Label(root, text = "IMAGE", activebackground = 'blue', activeforeground = 'red', bg = 'blue')
lbl_2.config(width = 200, height = 10)
lbl_2.pack(side = TOP)

but_1 = Button(root, text = "Graph visual", command = butt_graph)
but_1.config(width = 20, height = 3, bg = 'blue')
but_1.pack(side = LEFT)

but_2 = Button(root, text = "Check ID", command = butt_ID)
but_2.config(width = 20, height = 3, bg = 'blue')
but_2.pack(side = RIGHT)
root.mainloop()



#__________________________SMART GARBAGE MONITORING SYTSEM___________________________
frame = Frame(master)
frame.pack()
self.lbl_1 = Label(frame, text = "SMART GARBAGE MONITORING SYSTEM", activebackground = 'blue', activeforeground = 'red',
                   bg = 'red')
self.lbl_1.config(width = 300, height = 4)
self.lbl_1.pack(side = TOP)

self.lbl_2 = Label(frame, text = "IMAGE", activebackground = 'blue', activeforeground = 'red', bg = 'blue')
self.lbl_2.config(width = 200, height = 10)
self.lbl_2.pack(side = TOP)

self.but_1 = Button(frame, text = "Graph visual", command = self.PtGraph)
self.but_1.config(width = 20, height = 3, bg = 'blue')
self.but_1.pack(side = LEFT)

self.but_2 = Button(frame, text = "Check ID", command = self.PtCluster)
self.but_2.config(width = 20, height = 3, bg = 'blue')
self.but_2.pack(side = RIGHT)

self.but_3 = Button(frame, text = "Quit", command = frame.quit)
self.but_3.config(width = 20, height = 3, bg = 'blue')
self.but_3.pack(side = BOTTOM)