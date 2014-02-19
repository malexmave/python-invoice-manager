import os
import random
import string
import unittest

import data.initialize
import data.connect


class DBSpecifications(unittest.TestCase):
    def testDBSpec_options(self):
        data.initialize.testDBSpec_options()

    def testDBSpec_fkeys(self):
        data.initialize.testDBSpec_fkeys()

    def testDBSpec_types(self):
        data.initialize.testDBSpec_types()


class DBGeneration(unittest.TestCase):
    # TODO: Negative-tests
    def setUp(self):
        self.testfilename = "test." + ''.join(random.choice(
            string.ascii_lowercase + string.digits) for x in range(8)) + ".db"

    def testDBGeneration(self):
        if not os.path.isfile(self.testfilename):
            rv = 0
            assert data.connect.isSQLite3(self.testfilename) == 1, \
                "isSQLite3: Nonexistant file not detected"
            try:
                data.initialize.setup(self.testfilename)
            except Exception, e:
                try:
                    os.remove(self.testfilename)
                except OSError:
                    pass
                self.fail('An exception occured: ' + str(e))
            assert data.connect.isSQLite3(self.testfilename) == 0, \
                "isSQLite3: Valid SSQLite3 not detected"
            try:
                data.initialize.checkConformity(self.testfilename)
            except Exception, e:
                try:
                    os.remove(self.testfilename)
                except OSError:
                    pass
                self.fail('An exception occured: ' + str(e))
            with open(self.testfilename, "w") as fo:
                fo.write(''.join(random.choice(string.ascii_lowercase + 
                    string.digits) for x in range(200)))
            assert data.connect.isSQLite3(self.testfilename) == 2, \
                "isSQLite3: Invalid SQLite3 not detected."
            try:
                data.initialize.setup(self.testfilename)
                rv = 1
            except AssertionError:
                rv = 0
            if rv == 1:
                self.fail("Setup: No fail on invalid db file")
            try:
                os.remove(self.testfilename)
            except OSError:
                pass
