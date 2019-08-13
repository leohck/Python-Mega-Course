#  Copyright (c)  13/8/2019
#  Developed by: Leonardo Black | 21 years old | Computer Engineer


import sqlite3


def connect():
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS book ("
                   "id INTEGER PRIMARY KEY,"
                   " title TEXT,"
                   " author TEXT,"
                   " year INTEGER,"
                   " isbn INTEGER)"
                   "")
    conn.commit()
    conn.close()


def insert(title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title, author, year, isbn))
    conn.commit()
    conn.close()


def update(_id, title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, _id))
    conn.commit()
    conn.close()


def delete(_id):
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM book WHERE id=?", (_id,))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM book")
    rows = cursor.fetchall()
    conn.close()
    return rows


def search(title='', author='', year=0, isbn=0):
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    rows = cursor.fetchall()
    conn.close()
    return rows
