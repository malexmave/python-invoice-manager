# -*- coding: utf-8 -*-
from data import structure
from random import randint, choice
import string

def randomString():
    return ''.join(choice(string.ascii_lowercase + string.digits) \
        for x in range(randint(3,100)))

# cd = "classdef", the definition of the classes we are building
cd =  "import copy\n"
cd += "import unittest\n"
cd += "import data.datatype\n\n"

exec cd
for tbl in structure.STRUCT:
    camelTbl = structure.CamelCase(tbl)
    cd += "class %s(unittest.TestCase):\n" % camelTbl
    cd += " "*4 + "def setUp(self):\n"
    cd += " "*8 + "self.template = {\n"
    dictdef = " "*8 + "self.getters = {\n"
    allowedNone = []
    for field in structure.STRUCT[tbl]:
        fd = structure.STRUCT[tbl][field]
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
        dictdef += " "*12 + "'%s': data.datatype.%s.%s,\n" % \
            (field, camelTbl, "get" + structure.CamelCase(field))
        if not fd["notNull"]:
            allowedNone.append(field)
    cd += " "*8 + "}\n"
    cd += dictdef + " "*8 + "}\n"

    ### Generate test functions
    # Generate Generation tests
    cd += """
    def test{0}Generation(self):
        allowedNone = {1}
        for field in self.template:
            rv = 0
            try:
                oldvar = copy.deepcopy(self.template[field])
                self.template[field] = None
                data.datatype.{0}(self.template)
                if field not in allowedNone:
                    rv = 1
            except AssertionError:
                if field in allowedNone:
                    rv = 2
            finally:
                self.template[field] = oldvar
                if rv == 1:
                    self.fail("%s = None accepted." % field)
                if rv == 2:
                    self.fail("%s = None not accepted." % field)

""".format(camelTbl, str(allowedNone))

    # Generate getter tests
    cd += """
    def test{0}Getters(self):
        try:
            {0} = data.datatype.{0}(self.template)
        except AssertionError:
            self.fail("Generation of {0} Object failed.")
        for key in self.getters:
            self.assertEqual(self.template[key], self.getters[key]({0}), \\
                "%s getter failed: Expected %s, but got %s" % \\
                (key, str(self.template[key]), str(self.getters[key]({0}))))

""".format(camelTbl)

    # Generate reference break tests
    cd += """
    def test{0}ReferenceBreak(self):
        try:
            {0} = data.datatype.{0}(self.template)
        except AssertionError:
            self.fail("Generation of {0} Object failed.")
        for key in self.getters:
            oldvar = copy.deepcopy(self.template[key])
            self.template[key] = None
            self.assertEqual(oldvar, self.getters[key]({0}), "%s: unbroken reference.")

""".format(camelTbl)
    
    # Test equality and inequality
    cd += """
    def test{0}Equality(self):
        {0}_1 = data.datatype.{0}(self.template)
        {0}_2 = data.datatype.{0}(self.template)
        self.template["ID"] += 1
        {0}_3 = data.datatype.{0}(self.template)
        assert {0}_1 == {0}_2, "{0} equality failed"
        assert {0}_1 != {0}_3, "{0} equality failed"
        assert {0}_2 != {0}_3, "{0} equality failed"

""".format(camelTbl)
    # Test checkRep function
    cd += """
    def test{0}CheckRep(self):
        {0} = data.datatype.{0}(self.template)
        {0}.checkRep()
        rv = 0
""".format(camelTbl)
    for field in structure.STRUCT[tbl]:
        fd = structure.STRUCT[tbl][field]
        S2P = structure.SQL_TO_PY_TYPE
        if S2P[fd["type"]] != "str":
            val = '"' + randomString() + '"' 
        else: 
            val = randint(1,1000)
        cd += """
        try:
            bu = {0}._{1} 
            {0}._{1} = {2}
            {0}.checkRep()
            rv = 1
        except AssertionError:
            {0}._{1} = bu
        finally:
            if rv == 1:
                self.fail('{0} checkRep did not detect error on {1}')
""".format(camelTbl, field, val) 

# Evaluate resulting string to generate tests for datatypes
exec cd