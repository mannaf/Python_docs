from tkinter import *

root = Tk()


def myClick():
    new_root = Tk()
    mylabel = Label(new_root, text="Look, I clicked Button")
    mylabel.pack()
    new_root.mainloop()


myButton = Button(root, text="click me", command=myClick).pack()
root.mainloop()