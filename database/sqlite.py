import sqlite3


def connect_to_db():
    conn = sqlite3.connect('aemotor.db')
    return conn
