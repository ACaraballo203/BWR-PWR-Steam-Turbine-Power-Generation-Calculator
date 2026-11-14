#This will be the base code for the app/GUI.

#Packages
from tkinter import *
from tkinter import ttk
import tkinter as tk

#Create Roor Window
window = Tk()

# root window title and dimension
window.title("Nuclear Steam Power Generator Calculator")
# Set geometry(widthxheight)
window.geometry('450x200')

# adding menu bar in root window
# new item in menu bar labelled as 'New'
# adding more items in the menu bar 
menu = Menu(window)
item = Menu(menu)
item.add_command(label='New')
menu.add_cascade(label='File', menu=item)
window.config(menu=menu)

#Adds a text in the GUI
greeting = tk.Label(text="Hello, Tkinter")
entry = tk.Entry()

# adding a label to the root window
lbl = Label(window, text = "Are you a Geek?")
lbl.grid()

# adding Entry Field
txt = Entry(window, width=10)
txt.grid(column =1, row =0)

# function to display text when
# button is clicked
def clicked():

    res = "You wrote " + txt.get()
    lbl.configure(text = res)

# button widget with red color text
# inside
btn = Button(window, text = "Click me" ,
             fg = "red", command=clicked)
# set Button grid
btn.grid(column=0, row=1)


# all widgets will be here
# Execute Tkinter
window.mainloop()
