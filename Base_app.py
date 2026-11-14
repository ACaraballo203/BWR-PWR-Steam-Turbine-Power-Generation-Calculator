#This will be the base code for the app/GUI.

##############Packages
from tkinter import *
from tkinter import ttk
import tkinter as tk

#Create Root Window
window = tk.Tk()

###############Functions
def raise_frame(frame):
    frame.tkraise()


# root window title and dimension
window.title("Nuclear Steam Power Generator Calculator")
# Set geometry(widthxheight)
window.geometry('450x350')

#Creating Different frames, these are the window for each individual model
f1 = Frame(window)
f2 = Frame(window)
f3 = Frame(window)
f4 = Frame(window)

#Setting up each Frame
for frame in (f1, f2, f3, f4):
    frame.grid(row=0, column=0, sticky='news')

#This is the Start Menu
Tlable = tk.Label(f1, text='Start Menu', font=("Verdana", 25), padx=130, pady=40).pack()

#Creating our main menu
menu = Menu(f1)

#Category Items for the menu
BWR_item = Menu(menu, tearoff=0)
menu.add_cascade(label='BWR', menu=BWR_item)

PWR_item = Menu(menu, tearoff=0)
menu.add_cascade(label='PWR', menu=PWR_item)

Comparison_item = Menu(menu, tearoff=0)
menu.add_cascade(label='Comparison', menu=Comparison_item)

#Creating our subcategory in the menu
BWR_item.add_command(label='Switch', command=lambda:raise_frame(f2))
#BWR_item.add_command(label='Open Window', command=lambda:Toplevel(f2))

PWR_item.add_command(label='Switch', command=lambda:raise_frame(f3))
#PWR_item.add_command(label='Open Window', command=lambda:Toplevel(f3))

Comparison_item.add_command(label='Switch', command=lambda:raise_frame(f4))
#Comparison_item.add_command(label='Open Window', command=lambda:Toplevel(f4))

#Adds a menu separator
menu.add_separator()
menu.add_cascade(label='Quit', command=window.quit)

window.config(menu=menu)

#Menu Selection
Button(f1, text='Boiling Water Reactor', command=lambda:raise_frame(f2)).pack()
Button(f1, text='Pressurized Water Reator', command=lambda:raise_frame(f3)).pack()
Button(f1, text='Comparison', command=lambda:raise_frame(f4)).pack()

Label(f2, text='Boiling water Reactor', font=("Verdana", 20)).pack()
Button(f2, text='Start Menu', command=lambda:raise_frame(f1)).pack()

Label(f3, text='Pressurized Water Reactor', font=("Verdana", 20)).pack()
Button(f3, text='Start Menu', command=lambda:raise_frame(f1)).pack()

Label(f4, text='Comparing Both Reactors', font=("Verdana", 20)).pack()
Button(f4, text='Start Menu', command=lambda:raise_frame(f1)).pack()

raise_frame(f1)

# all widgets will be here
# Execute Tkinter
window.mainloop()
