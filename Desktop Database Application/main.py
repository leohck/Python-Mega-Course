#  Copyright (c)  13/8/2019
#  Developed by: Leonardo Black | 21 years old | Computer Engineer

"""
A program that stores this book informations
-> Title
-> Author
-> Year
-> ISBN

User can:
View all records
Search an entry
Add entry
Update entry
Delete
Close
"""

from tkinter import *
import backend


def get_selected_row(event):
    try:
        global selected_tuple
        index = listbox.curselection()[0]
        selected_tuple = listbox.get(index)
        et_title.delete(0, END)
        et_author.delete(0, END)
        et_year.delete(0, END)
        et_isbn.delete(0, END)
        et_title.insert(END, selected_tuple[1])
        et_author.insert(END, selected_tuple[2])
        et_year.insert(END, selected_tuple[3])
        et_isbn.insert(END, selected_tuple[4])
    except IndexError:
        pass


def place_widgets():
    # ROW 0
    lb_title.grid(row=0, column=0)
    et_title.grid(row=0, column=1)
    lb_author.grid(row=0, column=2)
    et_author.grid(row=0, column=3)
    # ROW 1
    lb_year.grid(row=1, column=0)
    et_year.grid(row=1, column=1)
    lb_isbn.grid(row=1, column=2)
    et_isbn.grid(row=1, column=3)

    # ROW 2
    bt_view_all.grid(row=2, column=3)
    listbox.grid(row=2, column=0, rowspan=6, columnspan=2)
    scroll.grid(row=2, column=2, rowspan=6)

    listbox.configure(yscrollcommand=scroll.set)
    scroll.configure(command=listbox.yview)

    listbox.bind('<<ListboxSelect>>', get_selected_row)
    # ROW 3
    bt_searh_entry.grid(row=3, column=3)
    # ROW 4
    bt_add_entry.grid(row=4, column=3)
    # ROW 5
    bt_update.grid(row=5, column=3)
    # ROW 6
    bt_delete.grid(row=6, column=3)
    # ROW 7
    bt_close.grid(row=7, column=3)


def view_command():
    listbox.delete(0, END)
    for row in backend.view():
        listbox.insert(END, row)


def search_command():
    listbox.delete(0, END)
    for row in backend.search(et_title_text.get(), et_author_text.get(), et_year_text.get(), et_isbn_text.get()):
        listbox.insert(END, row)


def add_command():
    listbox.delete(0, END)
    backend.insert(et_title_text.get(), et_author_text.get(), et_year_text.get(), et_isbn_text.get())
    et_author.delete(0, END)
    et_year.delete(0, END)
    et_isbn.delete(0, END)
    listbox.insert(END, (et_title_text.get() + "\n successfully registered"))
    et_title.delete(0, END)


def update_command():
    backend.update(selected_tuple[0], et_title_text.get(), et_author_text.get(), et_year_text.get(), et_isbn_text.get())


def delete_command():
    backend.delete(selected_tuple[0])


def close_command():
    window.destroy()


window = Tk()
backend.connect()
# SETUP WIDGETS VARS
et_title_text = StringVar()
et_author_text = StringVar()
et_year_text = StringVar()
et_isbn_text = StringVar()

# SETUP WIDGETS
lb_title = Label(window, text="Title")
lb_author = Label(window, text="Author")
lb_year = Label(window, text="Year")
lb_isbn = Label(window, text="ISBN")

et_title = Entry(window, textvariable=et_title_text)
et_author = Entry(window, textvariable=et_author_text)
et_year = Entry(window, textvariable=et_year_text)
et_isbn = Entry(window, textvariable=et_isbn_text)

listbox = Listbox(window, width=35, height=10)
scroll = Scrollbar(window)

bt_searh_entry = Button(window, text="Search entry", width=15, command=search_command)
bt_view_all = Button(window, text="View all", width=15, command=view_command)
bt_add_entry = Button(window, text="Add entry", width=15, command=add_command)
bt_update = Button(window, text="Update selected", width=15, command=update_command)
bt_delete = Button(window, text="Delete selected", width=15, command=delete_command)
bt_close = Button(window, text="Close", width=15, command=close_command)

place_widgets()
window.mainloop()
