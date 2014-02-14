import sqlite3


def getCursor():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    conn.commit()  # Not sure if this is needed
    return cursor
