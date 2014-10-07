# Commented out the code for now, as the Code does not play well with
# foreign key constraints, and I don't have the motivation to fix this,
# as the fix is either ugly or non-trivial.
# TODO: Fix this stuff up.

from data import structure
from random import randint, choice
import string


def randomString():
    return ''.join(choice(string.ascii_lowercase + string.digits)
                   for x in range(randint(3, 50)))

s = structure.STRUCT

FKLib  = {} # Holds foreign key constraint information
FKData = {} # Holds actual foreign key sample data

for tbl in s:
    FKLib[tbl] = {}
    FKLib[tbl]["depended"] = False
    FKLib[tbl]["depends"] = []

def addFKC(tbl, field, targettbl, targetfield):
    try:
        FKLib[tbl][field]["out"]
    except KeyError:
        FKLib[tbl][field] = {}
    FKLib[tbl]["depends"] += [targettbl]
    FKLib[tbl][field]["out"] = True
    FKLib[tbl][field]["targettbl"] = targettbl
    FKLib[tbl][field]["targetfield"] = targetfield
    try:
        FKLib[targettbl][targetfield]["in"]
    except KeyError:
        FKLib[targettbl][targetfield] = {}
    FKLib[targettbl]["depended"] = True
    FKLib[targettbl][targetfield]["in"] = True


def isFKCTarget(tbl, field):
    try:
        return FKLib[tbl][field]["in"]
    except KeyError:
        return False


def isFKCSource(tbl, field):
    try:
        return FKLib[tbl][field]["out"]
    except KeyError:
        return False


def addFKData(tbl, field, data):
    try:
        FKData[tbl][field] = data
    except KeyError:
        FKData[tbl] = {}
        FKData[tbl][field] = data


def getFKtbl(tbl, field):
    return FKLib[tbl][field]["targettbl"]


def getFKfield(tbl, field):
    return FKLib[tbl][field]["targetfield"]


def getFKData(tbl, field):
    try:
        return FKData[getFKtbl(tbl, field)][getFKfield(tbl, field)]
    except KeyError, e:
        raise Exception(str(FKData) + "\n" + str(e))
    # This will throw a KeyError in case the data is not present yet.
    # This should not happen, as the tests should be generated in an order
    # that prevents this from happening.


def getDependencylessTables():
    res = []
    for tbl in FKLib:
        if FKLib[tbl]["depends"] == []:
            res += [tbl]
    return res

for tbl in s:
    for field in s[tbl]:
        if s[tbl][field]["foreignKey"] != None:
            targettbl = s[tbl][field]["foreignKey"]["table"]
            targetfield = s[tbl][field]["foreignKey"]["field"]
            addFKC(tbl, field, targettbl, targetfield)
            assert isFKCSource(tbl, field), "Source error"
            assert isFKCTarget(targettbl, targetfield), "Target error"

# Resolve dependencies
order = getDependencylessTables()
unprocessed = set(s.keys()) - set(order)
while set(s.keys()) - set(order) != set([]):
    toRemove = []
    for element in unprocessed:
        if set(FKLib[element]["depends"]) - set(order) == set([]):
            order += [element]
            toRemove += [element]
        else:
            print "Not Removing: %s. Depends: %s" % (element, str(FKLib[element]["depends"]))
    if toRemove == []:
        raise Exception(str(set(s.keys()) - set(order)) + ", " + str(order))
    else:
        for element in toRemove:
            unprocessed.remove(element)

cd = """from data import add, datatype
import unittest
"""

for tbl in order:
    cTbl = structure.CamelCase(tbl)
    cd += """class test%s(unittest.TestCase):
    def setUp(self):
        self.template = {
""" % cTbl
    allowedNone = []
    for field in s[tbl]:
        if field == "ID":
            cd += " "*12 + "'ID': -1,\n"
            if isFKCTarget(tbl, field):
                addFKData(tbl, field, 1)
                # This is quite an evil trick I am using to make this work
                # (predicting the auto_increment-Value on a new database),
                # but it is the only way to make this work with the current
                # implementation. As soon as the impl. is improved, this
                # could be changed
                # TODO: Keep this in mind for newer implementations
            continue
        fd = s[tbl][field]
        if isFKCSource(tbl, field):
            val = getFKData(tbl, field)
            if type(val) == int:
                cd += " "*12 + "'%s': %i,\n" % (field, val)
            elif type(val) == str:
                cd += " "*12 + "'%s': '%s',\n" % (field, val)
            elif type(val) == bool:
                cd += " "*12 + "'%s': %s,\n" % (field, str(val))
            elif type(val) == float:
                cd += " "*12 + "'%s': %f,\n" % (field, val)
            else:
                assert False, "Unknown type detected."
        elif structure.SQL_TO_PY_TYPE[fd["type"]] == "int":
            rv = randint(1, 10000)
            cd += " "*12 + "'%s': %i,\n" % (field, rv)
        elif structure.SQL_TO_PY_TYPE[fd["type"]] == "str":
            rv = randomString()
            cd += " "*12 + "'%s': '%s',\n" % (field, rv)
        elif structure.SQL_TO_PY_TYPE[fd["type"]] == "bool":
            rv = choice([True, False])
            cd += " "*12 + "'%s': %s,\n" % (field, str(rv))
        elif structure.SQL_TO_PY_TYPE[fd["type"]] == "float":
            rv = float(randint(1, 1000) + randint(1, 99)*0.01)
            cd += " "*12 + "'%s': %f,\n" % (field, rv)
        else:
            assert False, "Unknown type detected."
        if isFKCTarget(tbl, field):
            addFKData(tbl, field, rv)
    cd += " "*8 + "}\n\n"

    cd += """
    def testAdd{0}(self):
        self.{0} = datatype.{0}(self.template)
        add.{0}(self.{0})

""".format(cTbl)

exec cd
