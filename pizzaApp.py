from tkinter import *
from tkinter.font import *
from tkinter.ttk import *

window = Tk()
window.geometry("800x300")
window.configure(background = "Red", bd = 10, highlightbackground = "white")


title = Label(window, text = "Pizza App", font = ("Arial", 15))
title.pack(padx = 15, pady = 10)

f1 = Frame(window)
f1.pack(padx = 70, pady = 70,)

l1 = Label(f1, text = "Welcome to Pizza Hut", font = ("Arial", 15), bg = "White")
l1.grid(row = 1, column = 1)

l2 = Label(f1, text = "Select Your Fav Pizza:", font = ("Arial", 15), bg = "White")
l2.grid(row = 1, column = 0)

l3 = Label(f1, text = "Enter Quality:", font = ("Arial", 15), bg = "White")
l3.grid(row = 2, column = 0)

pizza_type = StringVar()
pizza_options = Combobox(f1, textvariable = pizza_type, width = 25)
pizza_options["value"]= ("Onion", "Corn", "Veg Delux")
pizza_options.set("Veg Delux")
pizza_options.grid(row = 1, column = 3)

pizza_quantity = IntVar()
num = Combobox(f1,textvariable = pizza_quantity, width = 25)
num["value"] = tuple(range(1, 7))
num.grid(row = 2, column = 2)

r1 = Radiobutton(f1, variable = pizza_type, text = "S",)
r2 = Radiobutton(f1, variable = pizza_type, text = "M",)
r3 = Radiobutton(f1, variable = pizza_type, text = "L",)

e1 = Entry(f1, text = "Veg Extravaganza")
e1.grid(row = 1, column = 2, columnspan = 2)

r1.grid(row = 3, column = 2)
r2.grid(row = 4, column = 2)
r3.grid(row = 5, column = 2)


b1 = Button(f1, text = "Order")
b1.grid(row = 5, column = 0)

window.mainloop()