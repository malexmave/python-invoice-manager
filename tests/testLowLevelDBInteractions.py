from data import structure
from random import randint, choice
import string

def randomString():
    return ''.join(choice(string.ascii_lowercase + string.digits) \
        for x in range(randint(3,50)))

s = structure.STRUCT

cd = """from data import add, datatype
import unittest
"""

for tbl in s:
    cTbl = structure.CamelCase(tbl)
    cd += """class test%s(unittest.TestCase):
    def setUp(self):
        self.template = {
""" % cTbl
    allowedNone = []
    for field in s[tbl]:
        if field == "ID":
            cd += " "*12 + "'ID': -1,\n"
            continue
        fd = s[tbl][field]
        if structure.SQL_TO_PY_TYPE[fd["type"]] == "int":
            cd += " "*12 + "'%s': %i,\n" % (field, randint(1, 10000))
        elif structure.SQL_TO_PY_TYPE[fd["type"]] == "str":
            cd += " "*12 + "'%s': '%s',\n" % (field, randomString())
        elif structure.SQL_TO_PY_TYPE[fd["type"]] == "bool":
            cd += " "*12 + "'%s': %s,\n" % (field, \
                choice(['True', 'False']))
        elif structure.SQL_TO_PY_TYPE[fd["type"]] == "float":
            cd += " "*12 + "'%s': %f,\n" % (field, 
                float(randint(1,1000) + randint(1,99)*0.01))
        else:
            assert False, "Unknown type detected."
    cd += " "*8 + "}\n\n"

    cd += """
    def testAdd{0}(self):
        self.{0} = datatype.{0}(self.template)
        add.{0}(self.{0})

""".format(cTbl)

exec cd