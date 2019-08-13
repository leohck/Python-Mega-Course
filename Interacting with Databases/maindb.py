#  Copyright (c)  13/8/2019
#  Developed by: Leonardo Black | 21 years old | Computer Engineer

# import sqlite3
import psycopg2

# steps
# connect to database  -> create a cursor object -> apply a SQL Query -> commit changes to database -> close conection

connection = "dbname='database1' user='postgres' password='toor' host='localhost' port='5432'"


def create_table():
    # connection to database OPEN
    # conn = sqlite3.connect("lite.db") sqlite3
    global connection
    conn = psycopg2.connect(connection)
    # create cursor
    cur = conn.cursor()
    # apply sql query
    createdbquery = "CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)"
    cur.execute(createdbquery)
    # commit changes to database
    conn.commit()
    # connection to database OPEN
    conn.close()


def insert(item, quantity, price):
    # conn = sqlite3.connect("lite.db") sqlite3
    global connection
    conn = psycopg2.connect(connection)
    cur = conn.cursor()
    # cur.execute("INSERT INTO store VALUES (?, ?, ?)", (item, quantity, price)) sqlite3
    cur.execute("INSERT INTO store VALUES ('{}', {}, {})".format(item, quantity, price))
    conn.commit()
    conn.close()


def view():
    # conn = sqlite3.connect("lite.db") sqlite3
    global connection
    conn = psycopg2.connect(connection)
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(item):
    # conn = sqlite3.connect("lite.db") sqlite3
    global connection
    conn = psycopg2.connect(connection)
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item='%s'" % item)
    conn.commit()
    conn.close()


def update(item, quantity, price):
    # conn = sqlite3.connect("lite.db")
    global connection
    conn = psycopg2.connect(connection)
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity={0}, price={1} WHERE item='{2}'".format(quantity, price, item))
    conn.commit()
    conn.close()


# create_table()
# insert("Lois", 2, 5240)
delete("Louis")
# update("Lois", 1, 5000)
print(view())
