from data import connect
import re


class InvalidDatabaseStructureException(Exception):
	"""InvalidDatabaseStructureException

	Thrown if the structure of the database is invalid.
	"""
	def __init__(self, msg=""):
		self.msg=msg

	def __repr__(self):
		return repr(self.msg)

	def __str__(self):
		return str(self.msg)


# SQL-Statements to generate the Database are represented like this.
# SQL_STRUCT = {
#     TABLENAME = {
#         FIELDNAME : [DATATYPE, OPTIONS, FOREIGN KEY OPTIONS],
#         FIELDNAME : ...
#         ...
#     },
#     TABLENAME = {
#         ...
#     },
#     ...
# }
SQL_STRUCT = {
	"article": {
		"ID":            ["INTEGER", "PRIMARY KEY AUTOINCREMENT", ""],
		"article_no":    ["INTEGER", "NOT NULL", ""],
		"name":          ["TEXT", "NOT NULL", ""],
		"description":   ["TEXT", "NOT NULL", ""],
		"article_type":  ["TEXT", "", ""],
		"tax_rate":      ["INTEGER", "NOT NULL", ""],
		"gross":         ["DECIMAL(16,2)", "NOT NULL", ""],
		"comment":       ["TEXT", "", ""],
		"last_modified": ["INTEGER", "NOT NULL", ""],
		"active":        ["BOOLEAN", "DEFAULT TRUE", ""]
	},
	"customer": {
		"ID":            ["INTEGER", "PRIMARY KEY AUTOINCREMENT", ""],
        "customer_no":   ["INTEGER", "NOT NULL", ""],
        "company":       ["TEXT", "", ""],
        "honorific":     ["TEXT", "", ""],
        "last_name":     ["TEXT", "", ""],
        "first_name":    ["TEXT", "", ""],
        "street":        ["TEXT", "NOT NULL", ""],
        "zip":           ["TEXT", "NOT NULL", ""],
        "city":          ["TEXT", "NOT NULL", ""],
        "country":       ["TEXT", "", ""],
        "phone":         ["TEXT", "", ""],
        "email":         ["TEXT", "", ""],
        "tax_no":        ["TEXT", "", ""],
        "comment":       ["TEXT", "", ""],
        "last_modified": ["INTEGER", "NOT NULL", ""],
        "active":        ["BOOLEAN", "DEFAULT TRUE NOT NULL", ""]
	},
	"shipping_address": {
	    "ID":            ["INTEGER", "PRIMARY KEY AUTOINCREMENT", ""],
        "customer_id":   ["INTEGER", "NOT NULL", "REFERENCES customer(ID) ON" +
                          " DELETE RESTRICT ON UPDATE RESTRICT"],
        "company":       ["TEXT", "", ""],
        "honorific":     ["TEXT", "", ""],
        "last_name":     ["TEXT", "", ""],
        "first_name":    ["TEXT", "", ""],
        "street":        ["TEXT", "NOT NULL", ""],
        "zip":           ["TEXT", "NOT NULL", ""],
        "city":          ["TEXT", "NOT NULL", ""],
        "country":       ["TEXT", "", ""],
        "comment":       ["TEXT", "", ""],
        "last_modified": ["INTEGER", "NOT NULL", ""],
        "active":        ["BOOLEAN", "DEFAULT TRUE NOT NULL", ""]
	},
	"company_data": {
	    "ID":            ["INTEGER", "PRIMARY KEY AUTOINCREMENT", ""],
        "company_name":  ["TEXT", "NOT NULL", ""],
        "street":        ["TEXT", "NOT NULL", ""],
        "zip":           ["TEXT", "NOT NULL", ""],
        "city":          ["TEXT", "NOT NULL", ""],
        "phone":         ["TEXT", "NOT NULL", ""],
        "mobile":        ["TEXT", "", ""],
        "website":       ["TEXT", "", ""],
        "email":         ["TEXT", "", ""],
        "bank_iban":     ["TEXT", "NOT NULL", ""],
        "bank_bic":      ["TEXT", "NOT NULL", ""],
        "bank_name":     ["TEXT", "NOT NULL", ""],
        "tax_no":        ["TEXT", "NOT NULL", ""],
        "currency":      ["TEXT", "NOT NULL", ""],
        "last_modified": ["INTEGER", "NOT NULL", ""],
        "active":        ["BOOLEAN", "DEFAULT TRUE NOT NULL", ""]
	},
	"invoice": {
        "ID":            ["INTEGER", "PRIMARY KEY AUTOINCREMENT", ""],
        "invoice_no":    ["INTEGER", "NOT NULL", ""],
        "invoice_date":  ["INTEGER", "NOT NULL", ""],
        "customer_id":   ["INTEGER", "NOT NULL", "REFERENCES customer(ID) ON" +
                           " DELETE RESTRICT ON UPDATE RESTRICT"],
        "company_id":    ["INTEGER", "NOT NULL", "REFERENCES company_data(ID)"+
                           " ON DELETE RESTRICT ON UPDATE RESTRICT"],
        "payment_due":   ["INTEGER", "NOT NULL", ""],
        "comment":       ["TEXT", "", ""],
        "finalized":     ["BOOLEAN", "NOT NULL", ""],
        "paid":          ["BOOLEAN", "NOT NULL", ""],
        "last_modified": ["INTEGER", "NOT NULL", ""],
        "active":        ["BOOLEAN", "DEFAULT TRUE NOT NULL", ""]
	},
	"invoice_element": {
        "ID":              ["INTEGER", "PRIMARY KEY AUTOINCREMENT", ""],
        "invoice_no":      ["INTEGER", "NOT NULL", "REFERENCES invoice(ID) ON"+
                             " DELETE RESTRICT ON UPDATE RESTRICT"],
        "invoice_element": ["INTEGER", "NOT NULL", ""],
        "article_id":      ["INTEGER", "NOT NULL", "REFERENCES article(ID) ON"+
                             " DELETE RESTRICT ON UPDATE RESTRICT"],
        "amount":          ["INTEGER", "NOT NULL", ""],
        "comment":         ["TEXT", "", ""],
        "last_modified":   ["INTEGER", "NOT NULL", ""],
        "active":          ["BOOLEAN", "DEFAULT TRUE NOT NULL", ""]
	},
	"invoice_payments": {
        "ID":             ["INTEGER", "PRIMARY KEY AUTOINCREMENT", ""],
        "invoice_no":     ["INTEGER", "NOT NULL", "REFERENCES invoice(ID) ON" +
                            " DELETE RESTRICT ON UPDATE RESTRICT"],
        "payment_amount": ["DECIMAL(16,2)", "NOT NULL", ""],
        "payment_date":   ["INTEGER", "NOT NULL", ""],
        "comment":        ["TEXT", "", ""],
        "last_modified":  ["INTEGER", "NOT NULL", ""],
        "active":         ["BOOLEAN", "DEFAULT TRUE NOT NULL", ""]
	}
}

def checkConformity(dbfile):
	"""Check the conformity of a SQLite database.

	This function will check if a provided SQLite database conforms to a the
	Database structure generated by SQL_STRUCT.

	Raises:
	InvalidDatabaseStructureException -- If the database structure is incorrect
	"""
	# Check database tables
	cursor, conn = connect.getConnection(dbfile)
	fkeypat = re.compile('REFERENCES (.*)\((.*)\) ON (UPDATE|DELETE) (.*) ' +
						 'ON (UPDATE|DELETE) (.*)')
	for tbl_name in SQL_STRUCT:
		cursor.execute("PRAGMA table_info(%s);" % tbl_name)
		res = cursor.fetchall()
		if res != []:
			# Table exists
			cursor.execute("PRAGMA foreign_key_list(%s);" % tbl_name)
			fkeys = cursor.fetchall()
			resdict = {}
			for element in res:
				resdict[element[1]] = {
					"type": element[2],
					"nullAllowed": True if element[3] == 0 else False
				}
			for element in fkeys:
				resdict[element[3]]["is_fkey"] = True
				resdict[element[3]]["UPDATE"] = element[5]
				resdict[element[3]]["DELETE"] = element[6]
				resdict[element[3]]["fkey_table"] = element[2]
				resdict[element[3]]["fkey_field"] = element[4]
			for field in SQL_STRUCT[tbl_name]:
				try:
					if resdict[field]["type"] == \
					  SQL_STRUCT[tbl_name][field][0]:
						# Field exists and has the correct type
						# Check for foreign keys
						if SQL_STRUCT[tbl_name][field][2] != "":
							mobj = re.search(fkeypat, 
								             SQL_STRUCT[tbl_name][field][2])
							assert resdict[field]["is_fkey"], "no foreign key"
							assert resdict[field]["fkey_table"] == \
							    	mobj.group(1), "incorrect table"
							assert resdict[field]["fkey_field"] == \
									mobj.group(2), "incorrect field"
							assert resdict[field][mobj.group(3)] == \
									mobj.group(4), "incorrect ON %s" % \
									mobj.group(3)
							assert resdict[field][mobj.group(5)] == \
									mobj.group(6), "incorrect ON %s" % \
									mobj.group(5)
					else:
						raise InvalidDatabaseStructureException(
							"Field %s in table %s has type %s (should be %s)"
							% (field, tbl_name, resdict[field]["type"],
							   SQL_STRUCT[tbl_name][field][0]))
				except KeyError:
					raise InvalidDatabaseStructureException(
						"Field %s does not exist in table %s." \
						% (field, tbl_name))
				except AssertionError, e:
					raise InvalidDatabaseStructureException(
						"Incorrect foreign key on %s: %s."
						% (field, str(e)))
					
		else:
			raise InvalidDatabaseStructureException("Table '%s' does not exist." % tbl_name)


def setup(dbfile):
	"""Set up the sqlite database on first run.

	This function will set up the SQLite database during first run.
	It should not be run afterwards.

	Raises:
	sqlite3.OperationalError -- If the database already exists or syntax of
	    a SQL statement was incorrect.
	"""
	cursor, conn = connect.getConnection(dbfile)
	for key in SQL_STRUCT:
		stmt = "CREATE TABLE %s(" % key
		for field in SQL_STRUCT[key]:
			stmt += "%s %s %s %s, " % (field, SQL_STRUCT[key][field][0],
				                       SQL_STRUCT[key][field][1],
				                       SQL_STRUCT[key][field][2])
		stmt = stmt[:-2] + ");"
		cursor.execute(stmt)
	conn.commit()

