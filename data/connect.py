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

def getConnection(dbfile, create=False):
    fs = isSQLite3(dbfile)
    if fs == 0 or (fs == 1 and create):
        conn = sqlite3.connect(dbfile)
        cursor = conn.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")
        conn.commit()  # Not sure if this is needed
        return (cursor, conn)
    else:
        raise AssertionError("File exists and is invalid SQLite file.")
