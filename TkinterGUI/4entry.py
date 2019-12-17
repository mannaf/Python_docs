from tkinter import *

root = Tk()
e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter Your Name")


def myclick():
    hello = e.get()
    mylabel = Label(root, text=hello)
    mylabel.pack()


myButton = Button(root, text="click me", command=myclick).pack()
root.mainloop()
