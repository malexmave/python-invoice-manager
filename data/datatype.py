class Article():
	def __init__(self, dat):
		# Check input values for proper types
		assert type(dat["ID"])            == int, "ID is not an integer"
		assert type(dat["article_no"])    == int, "article_no is not an integer"
		assert type(dat["name"])          == str, "name is not a string"
		assert type(dat["description"])   == str, "description is not a string"
		assert type(dat["article_type"])  in (str, type(None)), "article_type is neither String nor None"
		assert type(dat["tax_rate"])      == int, "tax_rate is not an integer"
		assert type(dat["gross"])         == int, "gross is not an integer"
		assert type(dat["comment"])       in (str, type(None)), "comment is neither String nor None"
		assert type(dat["last_modified"]) == int, "last_modified is not an integer"
		assert type(dat["active"])        == bool, "active is not a boolean"
		# Copy state info
		for key in dat:
			self.__dict__["_" + key] = dat[key]

	def getPersistentID(self):
		return self._ID

	def getArticleNumber(self):
		return self._article_no

	def getName(self):
		return self._name

	def getDescription(self):
		return self._description

	def getArticleType(self):
		return self._article_type

	def getTaxRate(self):
		return self._tax_rate

	def getGrossPrice(self):
		return self._gross

	def getComment(self):
		return self._comment

	def isActive(self):
		return self._active


class Company():
	def __init__(self, dat):
		# Check data
		assert type(dat["ID"])            == int, "ID is not an integer"
		assert type(dat["company_name"])  == str, "company_name is not a string"
		assert type(dat["street"])        == str, "street is not a string"
		assert type(dat["zip"])           == str, "zip is not a string"
		assert type(dat["city"])          == str, "city is not a string"
		assert type(dat["phone"])         == str, "phone is not a string"
		assert type(dat["mobile"])        in (str, type(None)), "mobile is not a string or None"
		assert type(dat["website"])       in (str, type(None)), "website is not a string or None"
		assert type(dat["email"])         in (str, type(None)), "email is not a string or None"
		assert type(dat["bank_iban"])     == str, "bank_iban is not a string"
		assert type(dat["bank_bic"])      == str, "bank_bic is not a string"
		assert type(dat["bank_name"])     == str, "bank_name is not a string"
		assert type(dat["tax_no"])        == str, "tax_no is not a string"
		assert type(dat["currency"])      == str, "currency is not a string"
		assert type(dat["last_modified"]) == int, "last_modified is not an integer"
		assert type(dat["active"])        == bool, "active is not a boolean"
		# copy state info
		for key in dat:
			self.__dict__["_" + key] = dat[key]

	def getPersistentID(self):
		return self._ID

	def getName(self):
		return self._company_name

	def getStreet(self):
		return self._street

	def getZIP(self):
		return self._zip

	def getCity(self):
		return self._city

	def getPhone(self):
		return self._phone

	def getMobile(self):
		return self._mobile

	def getWebsite(self):
		return self._website

	def getEmail(self):
		return self._email

	def getIBAN(self):
		return self._bank_iban

	def getBIC(self):
		return self._bank_bic

	def getBankName(self):
		return self._bank_name

	def getTaxNo(self):
		return self._tax_no

	def getCurrency(self):
		return self._currency

	def isActive(self):
		return self._active