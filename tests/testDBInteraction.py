import os
import random
import re
import string
import unittest

import data.initialize

"""
class ArticleDataInteractions(unittest.TestCase):
	def testAddArticle(self):
		self.failUnless(True)

	def testGetArticle(self):
		self.failUnless(True)

	def testEditArticle(self):
		self.failUnless(True)

	def testDiscontinueArticle(self):
		self.failUnless(True)

	def testRelaunchArticle(self):
		self.failUnless(True)


class CompanyDataInteractions(unittest.TestCase):
	def testEditCompanyData(self):
		self.failUnless(True)

	def testGetCompanyData(self):
		self.failUnless(True)


class CustomerDataInteractions(unittest.TestCase):
	def testAddCustomer(self):
		self.failUnless(True)

	def testGetCustomer(self):
		self.failUnless(True)

	def testEditCustomer(self):
		self.failUnless(True)

	def testRetireCustomer(self):
		self.failUnless(True)

	def testReanimateCustomer(self):
		self.failUnless(True)


class InvoiceDataInteractions(unittest.TestCase):
	def testNewInvoice(self):
		self.failUnless(True)

	def testGetInvoice(self):
		self.failUnless(True)

	def testEditInvoice(self):
		self.failUnless(True)

	def testFinalizeInvoice(self):
		self.failUnless(True)

	def testFinalizedInvoiceNotMutable(self):
		self.failUnless(True)
"""
class DBSpecifications(unittest.TestCase):
	def testDBSpec_options(self):
		s = data.structure.STRUCT
		for tbl in s:
			for field in s[tbl]:
				try:
					assert type(s[tbl][field]["notNull"]) == bool, \
					    "%s.%s: notNull not a boolean" % (tbl, field)
					assert type(s[tbl][field]["primaryKey"]) == bool, \
						"%s.%s: primaryKey not a boolean" % (tbl, field)
					assert type(s[tbl][field]["autoIncrement"])  == bool, \
						"%s.%s: autoIncrement not a boolean" % (tbl, field)
					if s[tbl][field]["default"] != None:
						pass  # TODO: Use the class generators mapping of datatypes
					if s[tbl][field]["autoIncrement"]:
						assert s[tbl][field]["primaryKey"], "AIncrement on non-PK."
				except KeyError, e:
					self.fail("KeyError on %s.%s: %s" % (tbl, field, str(e)))

	def testDBSpec_fkeys(self):
		fkeypat = re.compile('REFERENCES (.*)\((.*)\) ON (UPDATE|DELETE) ' +
			'(RESTRICT|DELETE|CASCADE) ON (UPDATE|DELETE) ' + 
			'(RESTRICT|DELETE|CASCADE)')
		s = data.structure.STRUCT
		for tbl in s:
			for field in s[tbl]:
				if s[tbl][field][2] != "":
					mo = re.match(fkeypat, s[tbl][field][2])
					assert mo != None, "Incorrect fkey statement for %s.%s" \
						% (tbl, field)
					assert mo.group(1) in s.keys(), \
						"Reference to undefined table in %s.%s" % (tbl, field)
					assert mo.group(2) in s[mo.group(1)].keys(), \
						"Reference to undefined field in %s.%s" % (tbl, field)

	def testDBSpec_types(self):
		types = ["INTEGER", "TEXT", "DECIMAL(16,2)", "BOOLEAN", "BLOB"]
		s = data.structure.STRUCT
		for tbl in s:
			for field in s[tbl]:
				assert s[tbl][field][0] in types, \
					"Invalid type for %s.%s" % (tbl,field)

"""
class DBGeneration(unittest.TestCase):
	def setUp(self):
		self.testfilename = "test." + ''.join(random.choice(
			string.ascii_lowercase + string.digits) for x in range(8)) + ".db"

	def testDBGeneration(self):
		if not os.path.isfile(self.testfilename):
			try:
				data.initialize.setup(self.testfilename)
			except Exception, e:
				os.remove(self.testfilename)
				self.fail('An exception occured: ' + str(e))
			try:
				data.initialize.checkConformity(self.testfilename)
			except Exception, e:
				os.remove(self.testfilename)
				self.fail('An exception occured: ' + str(e))
			os.remove(self.testfilename)
"""