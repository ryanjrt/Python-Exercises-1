import tkinter as tk

window = tk.Tk()
window.title("Fire into the window!")
window.geometry("600x300")

def button_press():
    button.config(text="Ta ta, fool!", 
                  fg = "#0000ff",
                  bg = "#000000")

def submit_name():
    entry_name = entry.get()
    button2.config(text = f"Hello, {entry_name}!")

label = tk.Label(text="Hello, Tkinter!",
                 font = ("Arial", 12),
                 pady=10)
label.pack()

button = tk.Button(fg="#ff0000", 
                   bg = "#00ff00",
                   width=30,
                   height=10,
                   compound= "center",
                   text="Click me!",
                   command = button_press)
button.pack()

entry = tk.Entry()
entry.pack()

button2 = tk.Button(fg="#ff0000", 
                   bg = "#00ff00",
                   width=15,
                   height=5,
                   compound= "center",
                   text="Submit!",
                   command = submit_name)
button2.pack()


tk.mainloop()