import re
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
class DBGeneration(unittest.TestCase):
	def testDBSpec_options(self):
		optionspat = re.compile('((NOT NULL)|(PRIMARY KEY)|(AUTOINCREMENT)|' +
			'(DEFAULT (TRUE|FALSE)))+')
		s = data.initialize.SQL_STRUCT
		for tbl in s:
			for field in s[tbl]:
				if s[tbl][field][1] != "":
					mo = re.match(optionspat, s[tbl][field][1])
					assert mo != None, "Incorrect SQL options for %s.%s" \
						% (tbl, field)

	def testDBSpec_fkeys(self):
		fkeypat = re.compile('REFERENCES (.*)\((.*)\) ON (UPDATE|DELETE) ' +
			'(RESTRICT|DELETE|CASCADE) ON (UPDATE|DELETE) ' + 
			'(RESTRICT|DELETE|CASCADE)')
		s = data.initialize.SQL_STRUCT
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
		types = ["INTEGER", "TEXT", "DECIMAL(16,2)", "BOOLEAN"]
		s = data.initialize.SQL_STRUCT
		for tbl in s:
			for field in s[tbl]:
				assert s[tbl][field][0] in types, \
					"Invalid type for %s.%s" % (tbl,field)

	def testDBGeneration(self):
		pass

	def testGeneratedDBCorrectness(self):
		pass