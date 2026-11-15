#This will be the base code for the app/GUI.

##############Packages
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import font
import re

#Create Root Window
window = tk.Tk()

###############Functions
def raise_frame(frame):
    frame.tkraise()

def check_num(newval):
    return re.match('^[0-9]*$', newval) is not None and len(newval) <= 5



# root window title and dimension
window.title("Nuclear Steam Power Generator Calculator")
# Set geometry(widthxheight)
window.geometry('500x375')

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

###Formatting BWR's Frame###
Label(f2, text='Boiling Water Reactor', font=("Verdana", 20)).grid()
Button(f2, text='Start Menu', command=lambda:raise_frame(f1)).grid()

#Temperature Section Customization
B_L_temp = ttk.Label(f2, text='Temperatures', font=("Verdana", 15)).grid(sticky='w')
B_L_in_temp = ttk.Label(f2, text='Inlet:', font=("Verdana", 15)).grid(sticky='w')
B_check_num_wrapper = (f2.register(check_num), '%P')
B_num1 = StringVar()
B_e1 = ttk.Entry(f2, textvariable=B_num1, validate='key', validatecommand=B_check_num_wrapper, width=10).place(x=60 ,y=100)
B_Temp_Units = ttk.Label(f2, text='\u00b0 C').place(x=125 ,y=100)

B_L_out_temp = ttk.Label(f2, text='Outlet:', font=("Verdana", 15)).grid(sticky='w')
B_num2 = StringVar()
B_e2 = ttk.Entry(f2, textvariable=B_num2, validate='key', validatecommand=B_check_num_wrapper, width=10).place(x=80 ,y=130)
B_Temp_Units = ttk.Label(f2, text='\u00b0 C').place(x=145 ,y=130)

#Pressure Section Customization
B_L_Press = ttk.Label(f2, text='Pressure', font=("Verdana", 15)).grid(sticky='w',pady= (15,0))
B_L_in_Press = ttk.Label(f2, text='Inlet:', font=("Verdana", 15)).grid(sticky='w')
B_num3 = StringVar()
B_e3 = ttk.Entry(f2, textvariable=B_num3, validate='key', validatecommand=B_check_num_wrapper, width=10).place(x=60 ,y=200)
B_Pres_Units = ttk.Label(f2, text='kPa').place(x=125 ,y=200)

B_L_out_Press = ttk.Label(f2, text='Outlet:', font=("Verdana", 15)).grid(sticky='w')
B_num4 = StringVar()
B_e4 = ttk.Entry(f2, textvariable=B_num4, validate='key', validatecommand=B_check_num_wrapper, width=10).place(x=75 ,y=230)
B_Pres_Units = ttk.Label(f2, text='kPa').place(x=145 ,y=230)

#Enthalpy Section Customization
B_L_Enth = ttk.Label(f2, text='Enthalpy', font=("Verdana", 15)).grid(sticky='w',pady= (15,0))
B_L_in_Enth = ttk.Label(f2, text='Inlet:', font=("Verdana", 15)).grid(sticky='w')
B_num5 = StringVar()
B_e5 = ttk.Entry(f2, textvariable=B_num5, validate='key', validatecommand=B_check_num_wrapper, width=10).place(x=60 ,y=305)
B_Enth_Units = ttk.Label(f2, text='J').place(x=130 ,y=305)

B_L_out_Enth = ttk.Label(f2, text='Outlet:', font=("Verdana", 15)).grid(sticky='w')
B_num6 = StringVar()
B_e6 = ttk.Entry(f2, textvariable=B_num6, validate='key', validatecommand=B_check_num_wrapper, width=10).place(x=75 ,y=335)
B_Enth_Units = ttk.Label(f2, text='J').place(x=145 ,y=335)

#Efficiency Section
B_L_Eff = ttk.Label(f2, text='Turbine Efficiency:', font=("Verdana", 15)).place(x=200,y=95)
B_num7 = StringVar()
B_e7 = ttk.Entry(f2, textvariable=B_num7, validate='key', validatecommand=B_check_num_wrapper, width=5).place(x=390 ,y=100)
B_Eff_Units = ttk.Label(f2, text='%').place(x=425 ,y=100)

#Mass Flow Section
B_L_MasFlo = ttk.Label(f2, text='Mass Flow:', font=("Verdana", 15)).place(x=200,y=155)
B_num8 = StringVar()
B_e8 = ttk.Entry(f2, textvariable=B_num8, validate='key', validatecommand=B_check_num_wrapper, width=10).place(x=315 ,y=160)
B_MF_Units = ttk.Label(f2, text='kg/s').place(x=380 ,y=160)

#Result Section
B_L_Result = ttk.Label(f2, text='Results', font=("Verdana", 15)).place(x=200,y=225)

#Power Section
B_L_Power = ttk.Label(f2, text='Power:', font=("Verdana", 15)).place(x=200,y=250)
B_num9 = StringVar()
B_e9 = ttk.Entry(f2, textvariable=B_num9, validate='key', validatecommand=B_check_num_wrapper, width=10).place(x=270 ,y=255)
B_P_Units = ttk.Label(f2, text='kW').place(x=335 ,y=255)

###Formating's PWR Section###
Label(f3, text='Pressurized Water Reactor', font=("Verdana", 20)).grid()
Button(f3, text='Start Menu', command=lambda:raise_frame(f1)).grid()

#Temperature Section Customization
P_L_temp = ttk.Label(f3, text='Temperatures', font=("Verdana", 15)).grid(sticky='w')
P_L_in_temp = ttk.Label(f3, text='Inlet:', font=("Verdana", 15)).grid(sticky='w')
P_check_num_wrapper = (f3.register(check_num), '%P')
P_num1 = StringVar()
P_e1 = ttk.Entry(f3, textvariable=B_num1, validate='key', validatecommand=P_check_num_wrapper, width=10).place(x=60 ,y=100)
P_Temp_Units = ttk.Label(f3, text='\u00b0 C').place(x=125 ,y=100)

P_L_out_temp = ttk.Label(f3, text='Outlet:', font=("Verdana", 15)).grid(sticky='w')
P_num2 = StringVar()
P_e2 = ttk.Entry(f3, textvariable=P_num2, validate='key', validatecommand=P_check_num_wrapper, width=10).place(x=80 ,y=130)
P_Temp_Units = ttk.Label(f3, text='\u00b0 C').place(x=145 ,y=130)

#Pressure Section Customization
P_L_Press = ttk.Label(f3, text='Pressure', font=("Verdana", 15)).grid(sticky='w',pady= (15,0))
P_L_in_Press = ttk.Label(f3, text='Inlet:', font=("Verdana", 15)).grid(sticky='w')
P_num3 = StringVar()
P_e3 = ttk.Entry(f3, textvariable=P_num3, validate='key', validatecommand=P_check_num_wrapper, width=10).place(x=60 ,y=200)
P_Pres_Units = ttk.Label(f3, text='kPa').place(x=125 ,y=200)

P_L_out_Press = ttk.Label(f3, text='Outlet:', font=("Verdana", 15)).grid(sticky='w')
P_num4 = StringVar()
P_e4 = ttk.Entry(f3, textvariable=P_num4, validate='key', validatecommand=P_check_num_wrapper, width=10).place(x=75 ,y=230)
P_Pres_Units = ttk.Label(f3, text='kPa').place(x=145 ,y=230)

#Enthalpy Section Customization
P_L_Enth = ttk.Label(f3, text='Enthalpy', font=("Verdana", 15)).grid(sticky='w',pady= (15,0))
P_L_in_Enth = ttk.Label(f3, text='Inlet:', font=("Verdana", 15)).grid(sticky='w')
P_num5 = StringVar()
P_e5 = ttk.Entry(f3, textvariable=P_num5, validate='key', validatecommand=P_check_num_wrapper, width=10).place(x=60 ,y=305)
P_Enth_Units = ttk.Label(f3, text='J').place(x=130 ,y=305)

P_L_out_Enth = ttk.Label(f3, text='Outlet:', font=("Verdana", 15)).grid(sticky='w')
P_num6 = StringVar()
P_e6 = ttk.Entry(f3, textvariable=P_num6, validate='key', validatecommand=P_check_num_wrapper, width=10).place(x=75 ,y=335)
P_Enth_Units = ttk.Label(f3, text='J').place(x=145 ,y=335)

#Efficiency Section
P_L_Eff = ttk.Label(f3, text='Turbine Efficiency:', font=("Verdana", 15)).place(x=200,y=95)
P_num7 = StringVar()
P_e7 = ttk.Entry(f3, textvariable=P_num7, validate='key', validatecommand=P_check_num_wrapper, width=5).place(x=390 ,y=100)
P_Eff_Units = ttk.Label(f3, text='%').place(x=425 ,y=100)

#Mass Flow Section
P_L_MasFlo = ttk.Label(f3, text='Mass Flow:', font=("Verdana", 15)).place(x=200,y=155)
P_num8 = StringVar()
P_e8 = ttk.Entry(f3, textvariable=P_num8, validate='key', validatecommand=P_check_num_wrapper, width=10).place(x=315 ,y=160)
P_MF_Units = ttk.Label(f3, text='kg/s').place(x=380 ,y=160)

#Result Section
P_L_Result = ttk.Label(f3, text='Results', font=("Verdana", 15)).place(x=200,y=225)

#Power Section
P_L_Power = ttk.Label(f3, text='Power:', font=("Verdana", 15)).place(x=200,y=250)
P_num9 = StringVar()
P_e9 = ttk.Entry(f3, textvariable=P_num9, validate='key', validatecommand=P_check_num_wrapper, width=10).place(x=270 ,y=255)
P_P_Units = ttk.Label(f3, text='kW').place(x=335 ,y=255)

###Formating's Comparison Section###
Label(f4, text='Comparing Both Reactors', font=("Verdana", 20)).pack()
Button(f4, text='Start Menu', command=lambda:raise_frame(f1)).pack()

raise_frame(f1)

# all widgets will be here
# Execute Tkinter
window.mainloop()
