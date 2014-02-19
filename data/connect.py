from cache import db
import sqlite3


def isSQLite3(filename):
    from os.path import isfile, getsize

    if not isfile(filename):
        return 1
    if getsize(filename) < 100: # SQLite database file header is 100 bytes
        return 2
    else:
        fd = open(filename, 'rb')
        Header = fd.read(100)
        fd.close()

        if Header[0:16] == 'SQLite format 3\000':
            return 0
        else:
            return 2

def getConnection():
    if db._cur and db._con:
        return (db._cur, db._con)
    else:
        raise AssertionError("No open connection found.")

def openConnection(dbfile, create=False):
    fs = isSQLite3(dbfile)
    if fs == 0 or (fs == 1 and create):
        db._con = sqlite3.connect(dbfile)
        db._cur = db._con.cursor()
        db._cur.execute("PRAGMA foreign_keys = ON;")
        db._con.commit()  # Not sure if this is needed
        return True
    else:
        raise AssertionError("File exists and is invalid SQLite file.")