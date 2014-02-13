# -*- coding: utf-8 -*-
import copy
import unittest

import data.datatype
import manage.article
import manage.company
import manage.customer
import manage.invoice

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

class ArticleType(unittest.TestCase):
	def setUp(self):
		self.template = {"ID": 1, 
			"article_no": 1, 
			"name": "Hurpdurp", 
			"description": "Herp and Derp", 
			"article_type": "Service", 
			"tax_rate": 19, 
			"gross": 20, 
			"comment": "This is a comment", 
			"last_modified": 3,
			"active": True
		}
		self.getters = {
			"ID": data.datatype.Article.getPersistentID,
			"article_no": data.datatype.Article.getArticleNumber,
			"name": data.datatype.Article.getName,
			"description": data.datatype.Article.getDescription,
			"article_type": data.datatype.Article.getArticleType,
			"tax_rate": data.datatype.Article.getTaxRate,
			"gross": data.datatype.Article.getGrossPrice,
			"comment": data.datatype.Article.getComment,
			"active": data.datatype.Article.isActive
		}

	def testArticleGeneration(self):
		try:
			data.datatype.Article(self.template)
			self.template["article_type"] = None
			self.template["comment"] = None
			data.datatype.Article(self.template)
		except AssertionError, e:
			self.fail(str(e))
		try:
			self.template["ID"] = None
			data.datatype.Article(self.template)
			self.fail("ID == None, assertion failed.")
		except AssertionError, e:
			pass


	def testArticleGetters(self):
		article = data.datatype.Article(self.template)
		for key in self.getters:
			self.assertEqual(self.template[key], self.getters[key](article), \
				"%s getter failed: Expected %s, but got %s" % \
				(key, str(self.template[key]), str(self.getters[key](article))))

	def testReferenceBreak(self):
		article = data.datatype.Article(self.template)
		for key in self.getters:
			oldvar = copy.deepcopy(self.template[key])
			self.template[key] = None
			self.assertEqual(oldvar, self.getters[key](article), "%s: unbroken reference.")


class CompanyType(unittest.TestCase):
	def setUp(self):
		self.template = {"ID": 2, 
			"company_name": "Herpderp",
			"street": "Wonderstreet 1337",
			"zip": "31337",
			"city": "L33thaven",
			"phone": "+1 292992 666 42",
			"mobile": "+1 424242424242",
			"website": "31337company.com",
			"email": "42@31337company.com",
			"bank_iban": "LOL3313374242666",
			"bank_bic": "TROLLFACEXX",
			"bank_name": "Gotham City Bank",
			"tax_no": "31 337 424242",
			"currency": "€",
			"last_modified": 31337,
			"active": True
		}
		self.getters = {
			"ID": data.datatype.Company.getPersistentID,
			"company_name":data.datatype.Company.getName,
			"street":data.datatype.Company.getStreet,
			"zip":data.datatype.Company.getZIP,
			"city":data.datatype.Company.getCity,
			"phone":data.datatype.Company.getPhone,
			"mobile":data.datatype.Company.getMobile,
			"website":data.datatype.Company.getWebsite,
			"email":data.datatype.Company.getEmail,
			"bank_iban":data.datatype.Company.getIBAN,
			"bank_bic":data.datatype.Company.getBIC,
			"bank_name":data.datatype.Company.getBankName,
			"tax_no":data.datatype.Company.getTaxNo,
			"currency":data.datatype.Company.getCurrency,
			"active":data.datatype.Company.isActive
		}

	def testCompanyGeneration(self):
		try:
			data.datatype.Company(self.template)
			self.template["mobile"] = None
			self.template["website"] = None
			self.template["email"] = None
			data.datatype.Company(self.template)
		except AssertionError, e:
			self.fail(str(e))
		try:
			self.template["company_name"] = None
			data.datatype.Company(self.template)
			self.fail("Company Name = None accepted, assertions failed.")
		except AssertionError, e:
			pass

	def testCompanyGetters(self):
		company = data.datatype.Company(self.template)
		for key in self.getters:
			self.assertEqual(self.template[key], self.getters[key](company), \
				"%s getter failed: Expected %s, but got %s" % \
				(key, str(self.template[key]), str(self.getters[key](company))))

	def testReferenceBreak(self):
		company = data.datatype.Company(self.template)
		for key in self.getters:
			oldvar = copy.deepcopy(self.template[key])
			self.template[key] = None
			self.assertEqual(oldvar, self.getters[key](company), "%s: unbroken reference.")


def suite():
	suite = unittest.TestSuite()
	suite.addTest(unittest.makeSuite(ArticleDataInteractions, 'test'))
	suite.addTest(unittest.makeSuite(CompanyDataInteractions, 'test'))
	suite.addTest(unittest.makeSuite(CustomerDataInteractions, 'test'))
	suite.addTest(unittest.makeSuite(InvoiceDataInteractions, 'test'))
	suite.addTest(unittest.makeSuite(ArticleType, 'test'))
	suite.addTest(unittest.makeSuite(CompanyType, 'test'))
	return suite
