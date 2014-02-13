# -*- coding: utf-8 -*-

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
		self.template = {"ID": 1, \
		    "article_no": 1, \
		    "name": "Hurpdurp", \
		    "description": "Herp and Derp", \
		    "article_type": "Service", \
		    "tax_rate": 19, \
		    "gross": 20, \
		    "comment": "This is a comment", \
		    "last_modified": 3,\
		    "active": True}

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
		self.assertEqual(self.template["ID"], article.getPersistentID(), "ID getter failed")
		self.assertEqual(self.template["article_no"], article.getArticleNumber(), "article_no getter failed")
		self.assertEqual(self.template["name"], article.getName(), "name getter failed")
		self.assertEqual(self.template["description"], article.getDescription(), "description getter failed")
		self.assertEqual(self.template["article_type"], article.getArticleType(), "article_type getter failed")
		self.assertEqual(self.template["tax_rate"], article.getTaxRate(), "tax_rate getter failed")
		self.assertEqual(self.template["gross"], article.getGrossPrice(), "gross getter failed")
		self.assertEqual(self.template["comment"], article.getComment(), "comment getter failed")
		self.assertEqual(self.template["active"], article.isActive(), "active getter failed")

	def testReferenceBreak(self):
		article = data.datatype.Article(self.template)
		self.template["article_type"] = None
		self.assertEqual("Service", article.getArticleType(), "Error: State not disjointed")

	def testMutabilityByGetter(self):
		article = data.datatype.Article(self.template)
		temp = article.getPersistentID()
		temp = 3
		self.assertEqual(self.template["ID"], article.getPersistentID(), "Error: State mutable")


class CompanyType(unittest.TestCase):
	def setUp(self):
		self.template = {"ID": 2, \
			"company_name": "Herpderp",\
			"street": "Wonderstreet 1337",\
			"zip": "31337",\
			"city": "L33thaven",\
			"phone": "+1 292992 666 42",\
			"mobile": "+1 424242424242",\
			"website": "31337company.com",\
			"email": "42@31337company.com",\
			"bank_iban": "LOL3313374242666",\
			"bank_bic": "TROLLFACEXX",\
			"bank_name": "Gotham City Bank",\
			"tax_no": "31 337 424242",\
			"currency": "€",\
			"last_modified": 31337,\
			"active": True}

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
		self.assertEqual(self.template["ID"], company.getPersistentID(), "ID getter failed")
		self.assertEqual(self.template["company_name"], company.getName(), "company_name getter failed")
		self.assertEqual(self.template["street"], company.getStreet(), "street getter failed")
		self.assertEqual(self.template["zip"], company.getZIP(), "zip getter failed")
		self.assertEqual(self.template["city"], company.getCity(), "city getter failed")
		self.assertEqual(self.template["phone"], company.getPhone(), "phone getter failed")
		self.assertEqual(self.template["mobile"], company.getMobile(), "mobile getter failed")
		self.assertEqual(self.template["website"], company.getWebsite(), "website getter failed")
		self.assertEqual(self.template["email"], company.getEmail(), "email getter failed")
		self.assertEqual(self.template["bank_iban"], company.getIBAN(), "bank_iban getter failed")
		self.assertEqual(self.template["bank_bic"], company.getBIC(), "bank_bic getter failed")
		self.assertEqual(self.template["bank_name"], company.getBankName(), "bank_name getter failed")
		self.assertEqual(self.template["currency"], company.getCurrency(), "currency getter failed")
		self.assertEqual(self.template["active"], company.isActive(), "active getter failed")

	def testReferenceBreak(self):
		company = data.datatype.Company(self.template)
		self.template["mobile"] = None
		self.assertEqual("+1 424242424242", company.getMobile(), "Error: State not disjointed")

	def testMutabilityByGetter(self):
		company = data.datatype.Company(self.template)
		temp = company.getPersistentID()
		temp = 3
		self.assertEqual(self.template["ID"], company.getPersistentID(), "Error: State mutable")


def suite():
	suite = unittest.TestSuite()
	suite.addTest(unittest.makeSuite(ArticleDataInteractions, 'test'))
	suite.addTest(unittest.makeSuite(CompanyDataInteractions, 'test'))
	suite.addTest(unittest.makeSuite(CustomerDataInteractions, 'test'))
	suite.addTest(unittest.makeSuite(InvoiceDataInteractions, 'test'))
	suite.addTest(unittest.makeSuite(ArticleType, 'test'))
	suite.addTest(unittest.makeSuite(CompanyType, 'test'))
	return suite
