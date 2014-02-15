# -*- coding: utf-8 -*-
import copy
import unittest

import data.datatype

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
		allowedNone = ["article_type", "comment"]
		for field in self.template:
			rv = 0
			try:
				oldvar = copy.copy(self.template[field])
				self.template[field] = None
				data.datatype.Article(self.template)
				if field not in allowedNone:
					rv = 1
			except AssertionError:
				if field in allowedNone:
					rv = 2
			finally:
				self.template[field] = oldvar
				if rv == 1:
					self.fail("%s = None accepted.")
				if rv == 2:
					self.fail("%s = None not accepted.")


	def testArticleGetters(self):
		try:
			article = data.datatype.Article(self.template)
		except AssertionError:
			self.fail("Generation of Article Object failed.")
		for key in self.getters:
			self.assertEqual(self.template[key], self.getters[key](article), \
				"%s getter failed: Expected %s, but got %s" % \
				(key, str(self.template[key]), str(self.getters[key](article))))

	def testReferenceBreak(self):
		try:
			article = data.datatype.Article(self.template)
		except AssertionError:
			self.fail("Generation of Article Object failed.")
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
			"company_name": data.datatype.Company.getName,
			"street": data.datatype.Company.getStreet,
			"zip": data.datatype.Company.getZIP,
			"city": data.datatype.Company.getCity,
			"phone": data.datatype.Company.getPhone,
			"mobile": data.datatype.Company.getMobile,
			"website": data.datatype.Company.getWebsite,
			"email": data.datatype.Company.getEmail,
			"bank_iban": data.datatype.Company.getIBAN,
			"bank_bic": data.datatype.Company.getBIC,
			"bank_name": data.datatype.Company.getBankName,
			"tax_no": data.datatype.Company.getTaxNo,
			"currency": data.datatype.Company.getCurrency,
			"active": data.datatype.Company.isActive
		}

	def testCompanyGeneration(self):
		allowedNone = ["mobile", "website", "email"]
		for field in self.template:
			rv = 0
			try:
				oldvar = copy.copy(self.template[field])
				self.template[field] = None
				data.datatype.Company(self.template)
				if field not in allowedNone:
					rv = 1
			except AssertionError:
				if field in allowedNone:
					rv = 2
			finally:
				self.template[field] = oldvar
				if rv == 1:
					self.fail("%s = None accepted.")
				if rv == 2:
					self.fail("%s = None not accepted.")


	def testCompanyGetters(self):
		try:
			company = data.datatype.Company(self.template)
		except AssertionError:
			self.fail("Generation of company object failed")
		for key in self.getters:
			self.assertEqual(self.template[key], self.getters[key](company), \
				"%s getter failed: Expected %s, but got %s" % \
				(key, str(self.template[key]), str(self.getters[key](company))))

	def testReferenceBreak(self):
		try:
			company = data.datatype.Company(self.template)
		except AssertionError:
			self.fail("Generation of company object failed")
		for key in self.getters:
			oldvar = copy.deepcopy(self.template[key])
			self.template[key] = None
			self.assertEqual(oldvar, self.getters[key](company), "%s: unbroken reference.")
