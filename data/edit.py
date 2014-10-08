from data import connect, structure

# TODO: Auto-generate this stuff
# Universal functions:
# - deactivate{0}ByID({0})
# - activate{0}ByID({0})
# - {0}({0})

# Editing does not, in fact, edit existing entries, but creates new entries
# with the same article_no, customer_no, etc, but with a new ID.
# This is used in order to preserve a history of edits, and to preserve old
# invoices in case addresses change later.
# 
# Old versions of the same article, customer, etc, will be set to inactive
# and hidden from the default view (it will probably be possible to take a
# look at the history of individual entries).
# This means that existing entries _need_ to be edited (to set them to
# inactive), but the "active"-Flag should be the only field that is changed.
#
# The base edit function takes as a parameter an instance of an object of the
# correct type, with the data fields changed, but unchanged metadata fields
# (ID, last_modified, ...). It will then deactivate the old version (using the
# ID of the passed object), update the last_modified date, and save the new
# revision (using data.add.{0}).

s = structure.STRUCT
cd = "import time\n"
cd += "from data import add, connect, datatype\n\n"

for tbl in s:
    cTbl = structure.CamelCase(tbl)
    cd += """def {0}({0}):
    assert isinstance({0}, datatype.{0})
    {0}.checkRep()
    cur, conn = connect.getConnection()
    oID = {0}.getId()
    {0}._last_modified = int(time.time())
    add.{0}({0})
    stmt = 'UPDATE {1} SET active = 0 '
    stmt += "WHERE ID = %s" % oID
    cur.execute(stmt)
    conn.commit()

""".format(cTbl, tbl)

# TODO: Add revision handling according to the onRev-Flag in FK definition
# This requires use of the data.get.*-Functions, which are not implemented yet
exec cd