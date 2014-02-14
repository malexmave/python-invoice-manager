from data import connect
import sqlite3

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
        "customer_id":   ["INTEGER", "NOT NULL", "REFERENCES customer(ID) ON \
                           DELETE RESTRICT ON UPDATE RESTRICT"],
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
        "customer_id":   ["INTEGER", "NOT NULL", "REFERENCES customer(ID) ON \
                           DELETE RESTRICT ON UPDATE RESTRICT"],
        "company_id":    ["INTEGER", "NOT NULL", "REFERENCES company_data(ID) \
                           ON DELETE RESTRICT ON UPDATE RESTRICT"],
        "payment_due":   ["INTEGER", "NOT NULL", ""],
        "comment":       ["TEXT", "", ""],
        "finalized":     ["BOOLEAN", "NOT NULL", ""],
        "paid":          ["BOOLEAN", "NOT NULL", ""],
        "last_modified": ["INTEGER", "NOT NULL", ""],
        "active":        ["BOOLEAN", "DEFAULT TRUE NOT NULL", ""]
	},
	"invoice_element": {
        "ID":              ["INTEGER", "PRIMARY KEY AUTOINCREMENT", ""],
        "invoice_no":      ["INTEGER", "NOT NULL", "REFERENCES invoice(ID) ON \
                             DELETE RESTRICT ON UPDATE RESTRICT"],
        "invoice_element": ["INTEGER", "NOT NULL", ""],
        "article_id":      ["INTEGER", "NOT NULL", "REFERENCES article(ID) ON \
                             DELETE RESTRICT ON UPDATE RESTRICT"],
        "amount":          ["INTEGER", "NOT NULL", ""],
        "comment":         ["TEXT", "", ""],
        "last_modified":   ["INTEGER", "NOT NULL", ""],
        "active":          ["BOOLEAN", "DEFAULT TRUE NOT NULL", ""]
	},
	"invoice_payments": {
        "ID":             ["INTEGER", "PRIMARY KEY AUTOINCREMENT", ""],
        "invoice_no":     ["INTEGER", "NOT NULL", "REFERENCES invoice(ID) ON \
                            DELETE RESTRICT ON UPDATE RESTRICT"],
        "payment_amount": ["DECIMAL(16,2)", "NOT NULL", ""],
        "payment_date":   ["INTEGER", "NOT NULL", ""],
        "comment":        ["COMMENT", "", ""],
        "last_modified":  ["INTEGER", "NOT NULL", ""],
        "active":         ["BOOLEAN", "DEFAULT TRUE NOT NULL", ""]
	}
}

def checkConformity():
	"""Check the conformity of a SQLite database.

	This function will check if a provided SQLite database conforms to a the
	Database structure generated by SQL_STRUCT.

	Returns:
	True -- If the database format is correct
	False -- Otherwise
	"""
	pass

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
			stmt += "%s %s %s %s, " % (field, SQL_STRUCT[key][field][0], \
				                       SQL_STRUCT[key][field][1], \
				                       SQL_STRUCT[key][field][2])
		stmt = stmt[:-2] + ");"
		cursor.execute(stmt)
	conn.commit()

