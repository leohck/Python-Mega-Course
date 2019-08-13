#  Copyright (c)  13/8/2019
#  Developed by: Leonardo Black | 21 years old | Computer Engineer

from tkinter import *


def convert_kg():
    kg = float(et_kg_value.get())
    grams = kg*1000
    pounds = kg*2.20462
    ounces = kg*35.274
    tx_grams.delete('1.0', END)
    tx_pounds.delete('1.0', END)
    tx_ounces.delete('1.0', END)
    tx_grams.insert(INSERT, grams)
    tx_ounces.insert(INSERT, ounces)
    tx_pounds.insert(INSERT, pounds)


# SET WINDOW
window = Tk()

# VARS
et_kg_value = StringVar()

# WIDGETS
lb_intro = Label(window, height=1, width=20, text="KG")
et_kg = Entry(window, textvariable=et_kg_value)
bt_convert = Button(window, text="Execute", command=convert_kg)
tx_grams = Text(window, height=1, width=20)
tx_pounds = Text(window, height=1, width=20)
tx_ounces = Text(window, height=1, width=20)
lb_grams = Label(window, height=1, width=20, text="grams")
lb_pounds = Label(window, height=1, width=20, text="pounds")
lb_ounces = Label(window, height=1, width=20, text="ounces")

# POSITIONS
# row 1
lb_intro.grid(row=0, column=0)
et_kg.grid(row=0, column=1)
bt_convert.grid(row=0, column=3)

# row 2
tx_grams.grid(row=1, column=0)
tx_pounds.grid(row=1, column=1)
tx_ounces.grid(row=1, column=3)

# row 3
lb_grams.grid(row=2, column=0)
lb_pounds.grid(row=2, column=1)
lb_ounces.grid(row=2, column=3)

# INIT PROGRAM
window.mainloop()
