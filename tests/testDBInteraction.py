import os
import random
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
					assert type(s[tbl][field]["foreignKey"]) in \
						[type(None), dict], "%s.%s: Invalid foreignKey." % \
						(tbl, field)
					if s[tbl][field]["default"] != None:
						pass  # TODO: Use the datatype mapping
					if s[tbl][field]["autoIncrement"]:
						assert s[tbl][field]["primaryKey"], \
						"%s.%s: AutoIncrement on non-PK" % (tbl, field)
				except KeyError, e:
					self.fail("KeyError on %s.%s: %s" % (tbl, field, str(e)))

	def testDBSpec_fkeys(self):
		VALID_CONSTRAINTS = ["UPDATE", "DELETE", "CASCADE", "RESTRICT"]
		s = data.structure.STRUCT
		for tbl in s:
			for field in s[tbl]:
				try:
					if s[tbl][field]["foreignKey"] != None:
						# Typing checks
						assert type(s[tbl][field]["foreignKey"]["table"]) \
							== str, "%s.%s: Table choice should be string" % \
							(tbl, field)
						assert type(s[tbl][field]["foreignKey"]["field"]) \
							== str, "%s.%s: Field choice should be string" % \
							(tbl, field)
						assert type(s[tbl][field]["foreignKey"]["onDel"]) \
							== str, "%s.%s: onDel choice should be string" % \
							(tbl, field)
						assert type(s[tbl][field]["foreignKey"]["onUpd"]) \
							== str, "%s.%s: onUpd choice should be string" % \
							(tbl, field)
						assert s[tbl][field]["foreignKey"]["onDel"].upper() \
							in VALID_CONSTRAINTS, "%s.%s: Invalid constraints"\
							% (tbl, field)
						assert s[tbl][field]["foreignKey"]["onUpd"].upper() \
							in VALID_CONSTRAINTS, "%s.%s: Invalid constraints"\
							% (tbl, field)
						
						# Semantic Checks
						assert s[tbl][field]["foreignKey"]["table"] in s, \
							"%s.%s: Reference to non-existent table" % \
							(tbl, field)
						assert s[tbl][field]["foreignKey"]["field"] \
							in s[s[tbl][field]["foreignKey"]["table"]],\
							"%s.%s: Reference to non-existent field" % \
							(tbl, field)
				except KeyError, e:
					self.fail("KeyError on %s.%s: %s" % (tbl, field, str(e)))


	def testDBSpec_types(self):
		types = ["INTEGER", "TEXT", "DECIMAL(16,2)", "BOOLEAN", "BLOB" \
				 "INT", "REAL", "FLOAT", "DOUBLE", "NONE"]
		s = data.structure.STRUCT
		for tbl in s:
			for field in s[tbl]:
				assert s[tbl][field]["type"].upper() in types, \
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