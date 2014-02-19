from data import structure

# TODO: Auto-generate this stuff
# Universal functions:
# - {0}({0})

s = structure.STRUCT
cd = "from data import connect, datatype\n\n"

for tbl in s:
    cTbl = structure.CamelCase(tbl)
    cd += "def {0}({0}):\n".format(cTbl)
    cd += " "*4 + "assert isinstance({0}, datatype.{0})\n".format(cTbl)
    cd += " "*4 + "{0}.checkRep()\n".format(cTbl)
    cd += " "*4 + "cur, conn = connect.getConnection()\n"
    cd += " "*4 + "qfields = {}\n"
    for field in s[tbl]:
        if field != "ID":
            fd = s[tbl][field]
            cField = structure.CamelCase(field)
            cd += " "*4 + "if {0}.get{1}() != None:\n".format(cTbl, cField)
            cd += " "*8 + "qfields[{0}] = {1}.get{2}()\n".format(field, cTbl, 
                cField)
    cd += " "*4 + "stmt = 'INSERT INTO {0} ('\n".format(tbl)
    cd += " "*4 + "vals = ''\n"
    cd += " "*4 + "for field in qfields:\n"
    cd += " "*8 + "stmt += field + ', '\n"
    cd += " "*8 + "vals += ':' + field + ', '\n"
    cd += " "*4 + "stmt = stmt[:-2] + ') VALUES (' + vals[:-2] + ');'\n"
    cd += " "*4 + "cur.execute(stmt, qfields)\n"
    cd += " "*4 + "conn.commit()\n\n"

exec cd