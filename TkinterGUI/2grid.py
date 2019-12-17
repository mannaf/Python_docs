from tkinter import *

root = Tk()
# Creating a Label Wiget
mylabel1 = Label(root, text="hello World")
mylabel2 = Label(root, text="My name is mannaf")

# Showing it onto screen
mylabel1.grid(row=0, column=0)
mylabel2.grid(row=1, column=0)

root.mainloop()
