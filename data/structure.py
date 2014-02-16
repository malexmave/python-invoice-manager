import re

# SQL-Statements to generate the Database are represented like this.
# STRUCT = {
#     TABLENAME: {
#         FIELDNAME: {
#             "type": [INTEGER|TEXT|DECIMAL(16,2)|BOOLEAN|BLOB],
#             "notNull": [True|False],
#             "primaryKey": [True|False],
#             "autoIncrement": [True|False],
#             "default": [VALUE|None],
#             "foreignKey": [ForeignKeyStatement|None]
#         },
#         FIELDNAME: ...
#         ...
#     },
#     TABLENAME: {
#         ...
#     },
#     ...
# }
# 
# With:
# ForeignKeyStatement = {
#     "table": TABLENAME,
#     "field": FIELDNAME,
#     "onDel": [UPDATE|DELETE|CASCADE|RESTRICT],
#     "onUpd": [UPDATE|DELETE|CASCADE|RESTRICT]
# }
STRUCT = {
	"article": {
		"ID": {
		    "type": "INTEGER",
		    "notNull": False,
		    "primaryKey": True,
		    "autoIncrement": True,
		    "default": None,
		    "foreignKey": None
		},
		"article_no": {
		    "type": "INTEGER",
		    "notNull": True,
		    "primaryKey": False,
		    "autoIncrement": False,
		    "default": None,
		    "foreignKey": None
		},
		"name": {
		    "type": "TEXT",
		    "notNull": True,
		    "primaryKey": False,
		    "autoIncrement": False,
		    "default": None,
		    "foreignKey": None
		},
		"description": {
		    "type": "TEXT",
		    "notNull": True,
		    "primaryKey": False,
		    "autoIncrement": False,
		    "default": None,
		    "foreignKey": None
		},
		"article_type": {
		    "type": "TEXT",
		    "notNull": True,
		    "primaryKey": False,
		    "autoIncrement": False,
		    "default": None,
		    "foreignKey": None
		},
		"tax_rate": {
		    "type": "INTEGER",
		    "notNull": True,
		    "primaryKey": False,
		    "autoIncrement": False,
		    "default": None,
		    "foreignKey": None
		},
		"gross": {
		    "type": "DECIMAL(16,2)",
		    "notNull": True,
		    "primaryKey": False,
		    "autoIncrement": False,
		    "default": None,
		    "foreignKey": None
		 },
		"comment": {
		    "type": "TEXT",
		    "notNull": False,
		    "primaryKey": False,
		    "autoIncrement": False,
		    "default": None,
		    "foreignKey": None
		},
		"last_modified": {
		    "type": "INTEGER",
		    "notNull": True,
		    "primaryKey": False,
		    "autoIncrement": False,
		    "default": None,
		    "foreignKey": None
		},
		"active": {
		    "type": "BOOLEAN",
		    "notNull": True,
		    "primaryKey": False,
		    "autoIncrement": False,
		    "default": True,
		    "foreignKey": None
		}
	},
	"customer": {
		"ID":            {
		    "type": "INTEGER",
		    "notNull": False,
		    "primaryKey": True,
		    "autoIncrement": True,
		    "default": None,
		    "foreignKey": None
		},
        "customer_no":   {
            "type": "INTEGER",
            "notNull": True,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "company":       {
            "type": "TEXT",
            "notNull": False,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "honorific":     {
            "type": "TEXT",
            "notNull": False,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "last_name":     {
            "type": "TEXT",
            "notNull": False,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "first_name":    {
            "type": "TEXT",
            "notNull": False,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "street":        {
            "type": "TEXT",
            "notNull": True,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "zip":           {
            "type": "TEXT",
            "notNull": True,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "city":          {
            "type": "TEXT",
            "notNull": True,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "country":       {
            "type": "TEXT",
            "notNull": False,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "phone":         {
            "type": "TEXT",
            "notNull": False,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "email":         {
            "type": "TEXT",
            "notNull": False,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "tax_no":        {
            "type": "TEXT",
            "notNull": False,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "comment":       {
            "type": "TEXT",
            "notNull": False,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "last_modified": {
            "type": "INTEGER",
            "notNull": True,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "active":        {
            "type": "BOOLEAN",
            "notNull": True,
            "primaryKey": False,
            "autoIncrement": False,
            "default": True,
            "foreignKey": None
        }
	},
	"shipping_address": {
	    "ID":            {
	        "type": "INTEGER",
	        "notNull": False,
	        "primaryKey": True,
	        "autoIncrement": True,
	        "default": None,
	        "foreignKey": None
	    },
        "customer_id":   {
            "type": "INTEGER",
            "notNull": True,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": {
            	"table": "customer",
            	"field": "ID",
            	"onDel": "RESTRICT",
            	"onUpd": "RESTRICT"
            }
        },
        "company":       {
            "type": "TEXT",
            "notNull": False,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "honorific":     {
            "type": "TEXT",
            "notNull": False,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "last_name":     {
            "type": "TEXT",
            "notNull": False,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "first_name":    {
            "type": "TEXT",
            "notNull": False,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "street":        {
            "type": "TEXT",
            "notNull": True,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "zip":           {
            "type": "TEXT",
            "notNull": True,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "city":          {
            "type": "TEXT",
            "notNull": True,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "country":       {
            "type": "TEXT",
            "notNull": False,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "comment":       {
            "type": "TEXT",
            "notNull": False,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "last_modified": {
            "type": "INTEGER",
            "notNull": True,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "active":        {
            "type": "BOOLEAN",
            "notNull": True,
            "primaryKey": False,
            "autoIncrement": False,
            "default": True,
            "foreignKey": None
        }
	},
	"company_data": {
	    "ID":            {
	        "type": "INTEGER",
	        "notNull": False,
	        "primaryKey": True,
	        "autoIncrement": True,
	        "default": None,
	        "foreignKey": None
	    },
        "company_name":  {
            "type": "TEXT",
            "notNull": True,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "street":        {
            "type": "TEXT",
            "notNull": True,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "zip":           {
            "type": "TEXT",
            "notNull": True,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "city":          {
            "type": "TEXT",
            "notNull": True,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "phone":         {
            "type": "TEXT",
            "notNull": True,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "mobile":        {
            "type": "TEXT",
            "notNull": False,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "website":       {
            "type": "TEXT",
            "notNull": False,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "email":         {
            "type": "TEXT",
            "notNull": False,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "bank_iban":     {
            "type": "TEXT",
            "notNull": True,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "bank_bic":      {
            "type": "TEXT",
            "notNull": True,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "bank_name":     {
            "type": "TEXT",
            "notNull": True,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "tax_no":        {
            "type": "TEXT",
            "notNull": True,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "currency":      {
            "type": "TEXT",
            "notNull": True,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "last_modified": {
            "type": "INTEGER",
            "notNull": True,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "active":        {
            "type": "BOOLEAN",
            "notNull": True,
            "primaryKey": False,
            "autoIncrement": False,
            "default": True,
            "foreignKey": None
        }
	},
	"invoice": {
        "ID":            {
            "type": "INTEGER",
            "notNull": False,
            "primaryKey": True,
            "autoIncrement": True,
            "default": None,
            "foreignKey": None
        },
        "invoice_no":    {
            "type": "INTEGER",
            "notNull": True,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "invoice_date":  {
            "type": "INTEGER",
            "notNull": True,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "customer_id":   {
            "type": "INTEGER",
            "notNull": True,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": {
                "table": "customer",
                "field": "ID",
                "onDel": "RESTRICT",
                "onUpd": "RESTRICT"
            }
        },
        "company_id":    {
            "type": "INTEGER",
            "notNull": True,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": {
                "table": "company_data",
                "field": "ID",
                "onDel": "RESTRICT",
                "onUpd": "RESTRICT"
            }
        },
        "payment_due":   {
            "type": "INTEGER",
            "notNull": True,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "comment":       {
            "type": "TEXT",
            "notNull": False,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "finalized":     {
            "type": "BOOLEAN",
            "notNull": True,
            "primaryKey": False,
            "autoIncrement": False,
            "default": True,
            "foreignKey": None
        },
        "paid":          {
            "type": "BOOLEAN",
            "notNull": True,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "last_modified": {
            "type": "INTEGER",
            "notNull": True,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "active":        {
            "type": "BOOLEAN",
            "notNull": True,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
	},
	"invoice_element": {
        "ID":              {
            "type": "INTEGER",
            "notNull": False,
            "primaryKey": True,
            "autoIncrement": True,
            "default": None,
            "foreignKey": None
        },
        "invoice_no":      {
            "type": "INTEGER",
            "notNull": True,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": {
                "table": "invoice",
                "field": "ID",
                "onDel": "RESTRICT",
                "onUpd": "RESTRICT"
            }
        },
        "invoice_element": {
            "type": "INTEGER",
            "notNull": True,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "article_id":      {
            "type": "INTEGER",
            "notNull": True,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": {
                "table": "article",
                "field": "ID",
                "onDel": "RESTRICT",
                "onUpd": "RESTRICT"
            }
        },
        "amount":          {
            "type": "INTEGER",
            "notNull": True,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "comment":         {
            "type": "TEXT",
            "notNull": False,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "last_modified":   {
            "type": "INTEGER",
            "notNull": True,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "active":          {
            "type": "BOOLEAN",
            "notNull": True,
            "primaryKey": False,
            "autoIncrement": False,
            "default": True,
            "foreignKey": None
        },
	},
	"invoice_payments": {
        "ID":             {
            "type": "INTEGER",
            "notNull": False,
            "primaryKey": True,
            "autoIncrement": True,
            "default": None,
            "foreignKey": None
        },
        "invoice_no":     {
            "type": "INTEGER",
            "notNull": True,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": {
                "table": "invoice",
                "field": "ID",
                "onDel": "RESTRICT",
                "onUpd": "RESTRICT"
            }
        },
        "payment_amount": {
            "type": "DECIMAL(16,2)",
            "notNull": True,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "payment_date":   {
            "type": "INTEGER",
            "notNull": True,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "comment":        {
            "type": "TEXT",
            "notNull": False,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "last_modified":  {
            "type": "INTEGER",
            "notNull": True,
            "primaryKey": False,
            "autoIncrement": False,
            "default": None,
            "foreignKey": None
        },
        "active":         {
            "type": "BOOLEAN",
            "notNull": True,
            "primaryKey": False,
            "autoIncrement": False,
            "default": True,
            "foreignKey": None
        }
	}
}

SQL_TO_PY_TYPE = {
    "INTEGER"      : "int",
    "TEXT"         : "str",
    "BOOLEAN"      : "bool",
    "DECIMAL(16,2)": "float"
}

def CamelCase(strng):
    def _cc(mobj):
        rv = mobj.group(0)[1:]
        return rv.upper()
    return re.sub('_.', _cc, strng.capitalize())
