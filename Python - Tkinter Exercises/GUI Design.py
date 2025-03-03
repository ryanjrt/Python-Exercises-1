import tkinter
from tkinter import *

count = 0

def clickme():
    global count
    count += 1
    label.config(text = count)
    print("You are that which experiences. Nothing more, nothing less.")

window = Tk()
window.title("My first GUI")
window.config(background = "#011638")

label2 = Label(text = "I have achieved insane success!",
              fg = "#ffffff",
              bg = "#000000",
              compound = "center",
              padx = 40,
              pady = 10
              )



button = Button(window,
                text = "Click me to achieve unassailable self esteem",
                )
button.config(command = clickme)

#Button styling
button.config(font = ("Times New Roman", 10, "italic"))
button.config(bg = "#63637d", fg = "#292959")
button.config(activebackground = "#0ebcc2", activeforeground = "#ffffff")

#Button state
#button.config(state = DISABLED)

#Counter Label
label = Label(window, text = count)

#Entry Widget
entry = Entry()
entry.config(font = ('Times New Roman', 20))
entry.config(bg = '#fcba03')
entry.config(bg = '#00FF00')
entry.insert(0, 'Type shit') #Default text
#entry.config(state = DISABLED) ACTIVE / DISABLED
entry.config(width = 10) #Size of the entry display (# characters shown)
entry.config(show = '*') #Replaces typed string to '*', great for passwords

entry.pack()
label.pack()
label2.pack()
button.pack()
window.mainloop()
