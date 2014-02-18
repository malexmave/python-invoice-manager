import sqlite3


def getConnection(dbfile):
	# TODO: Check if file exists and is valid before opening
    conn = sqlite3.connect(dbfile)
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    conn.commit()  # Not sure if this is needed
    return (cursor, conn)
