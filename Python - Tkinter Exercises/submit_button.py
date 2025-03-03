from tkinter import *

def submit():
    username = entry.get()
    print("Hello " + username)
    
def delete():
    entry.delete(0, END)
    
def backspace():
    entry.delete(len(entry.get())-1, END) #delete last character

window = Tk()

#Entry Widget
entry = Entry()
entry.config(font = ('Times New Roman', 20))
entry.config(bg = '#fcba03')
entry.config(bg = '#00FF00')
entry.insert(0, 'Type shit') #Default text
#entry.config(state = DISABLED) ACTIVE / DISABLED
entry.config(width = 10) #Size of the entry display (# characters shown)
#entry.config(show = '*') #Replaces typed string to '*', great for passwords

submit = Button(window, text = "submit", command = submit)
delete = Button(window, text = "delete", command = delete)
backspace = Button(window, text = "backspace", command = backspace)

entry.pack()
submit.pack(side = RIGHT)
delete.pack(side = RIGHT)
backspace.pack(side = BOTTOM)
window.mainloop()