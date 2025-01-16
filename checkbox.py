from tkinter import *

def display():
    print("I like Python")


window = Tk()

x = IntVar()

checkbox = Checkbutton(window, text = 'Python', variable = x, onvalue = 1, offvalue = 0, command = display)

checkbox.pack()
window.mainloop()