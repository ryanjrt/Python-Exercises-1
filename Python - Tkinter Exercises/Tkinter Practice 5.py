# Create a Resizable Window
# Objective: Create a window where all widgets (labels, buttons, etc.) resize dynamically when the window size changes.

import tkinter as tk
from tkinter import messagebox

#Define functions
def resize_screen():
    new_width = width_entry.get()
    new_height = height_entry.get()
   
    try:
        new_width = int(new_width)
        new_height = int(new_height)
        
        root.geometry(f"{new_width}x{new_height}")
    except ValueError:
        tk.messagebox.showerror("Invalid input", "Please enter an integer for width and height!")
        
#Initialize window
root = tk.Tk()
title = root.title("shat")
root.geometry("500x500")

#Add labels, entry and buttons
#Resize entry
width_label = tk.Label(root, text = "Please enter your desired resize width:")
width_entry = tk.Entry(root, width = 20, font = ("Arial", 10))

height_label = tk.Label(root, text = "Please enter your desired resize height:")
height_entry = tk.Entry(root, width = 20, font = ("Arial", 10))

#Pack objects
width_label.pack(padx = 10, pady = 15)
width_entry.pack()

height_label.pack(padx = 10, pady = 15)
height_entry.pack()

submit_button = tk.Button(root, text = "submit", command = resize_screen)
submit_button.pack(pady = 15)

tk.mainloop()
