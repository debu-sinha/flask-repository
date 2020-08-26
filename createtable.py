import sqlite3
import os

def reset_database():
    filepath = "data.db"
    if os.path.exists(filepath):
        print("found file")
        os.remove(filepath)

    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    create_table = "create table if not exists users(id INTEGER PRIMARY KEY, username text, password text)"
    cursor.execute(create_table)

    create_table = "create table if not exists items( id INTEGER PRIMARY KEY, name varchar(60), price real)"
    cursor.execute(create_table)

    insert_dummy_item = "insert into items(name, price) values('table', 100.00)"
    cursor.execute(insert_dummy_item)

    connection.commit()
    connection.close()
