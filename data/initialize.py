from data import connect, structure


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


def checkConformity(dbfile):
	"""Check the conformity of a SQLite database.

	This function will check if a provided SQLite database conforms to a the
	Database structure generated by structure.STRUCT.

	Raises:
	InvalidDatabaseStructureException -- If the database structure is incorrect
	"""
	# TODO: Modify to conform to new DB structure definition
	# Check database tables
	cursor, conn = connect.getConnection(dbfile)
	for tbl in structure.STRUCT:
		cursor.execute("PRAGMA table_info(%s);" % tbl)
		res = cursor.fetchall()
		if res != []:
			# Table exists
			cursor.execute("PRAGMA foreign_key_list(%s);" % tbl)
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
			for field in structure.STRUCT[tbl]:
				try:
					if resdict[field]["type"] == \
					  structure.STRUCT[tbl][field]["type"]:
						# Field exists and has the correct type
						# Check for foreign keys
						if structure.STRUCT[tbl][field]["foreignKey"] \
							!= None:
							fk = structure.STRUCT[tbl][field]["foreignKey"]
							assert resdict[field]["is_fkey"], \
								"%s.%s: Should not be a foreign key" % \
								(tbl, field)
							assert resdict[field]["fkey_table"] == \
							    	fk["table"], "%s.%s: incorrect table" \
							    	% (tbl, field)
							assert resdict[field]["fkey_field"] == \
									fk["field"], "%s.%s: incorrect field" \
									% (tbl, field)
							assert resdict[field]["UPDATE"] == \
									fk["onUpd"], "%s.%s: incorrect ON UPDATE" \
									% (tbl, field)
							assert resdict[field]["DELETE"] == \
									fk["onDel"], "%s.%s: incorrect ON DELETE" \
									% (tbl, field)
					else:
						raise InvalidDatabaseStructureException(
							"Field %s in table %s has type %s (should be %s)"
							% (field, tbl, resdict[field]["type"],
							   structure.STRUCT[tbl][field][0]))
				except KeyError:
					raise InvalidDatabaseStructureException(
						"Field %s does not exist in table %s." \
						% (field, tbl))
				except AssertionError, e:
					raise InvalidDatabaseStructureException(
						"Incorrect foreign key on %s: %s."
						% (field, str(e)))
		else:
			raise InvalidDatabaseStructureException("Table '%s' does not exist." % tbl)


def testDBSpec_options():
	s = structure.STRUCT
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
				# TODO: Verify datatypes of fkey and target
				if s[tbl][field]["autoIncrement"]:
					assert s[tbl][field]["primaryKey"], \
					"%s.%s: AutoIncrement on non-PK" % (tbl, field)
			except KeyError, e:
				raise AssertionError("KeyError on %s.%s: %s" % (tbl, field, str(e)))

def testDBSpec_fkeys():
	VALID_CONSTRAINTS = ["UPDATE", "DELETE", "CASCADE", "RESTRICT"]
	s = structure.STRUCT
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
				raise AssertionError("KeyError on %s.%s: %s" % (tbl, field, str(e)))


def testDBSpec_types():
	types = ["INTEGER", "TEXT", "DECIMAL(16,2)", "BOOLEAN", "BLOB" \
			 "INT", "REAL", "FLOAT", "DOUBLE", "NONE"]
	s = structure.STRUCT
	for tbl in s:
		for field in s[tbl]:
			assert s[tbl][field]["type"].upper() in types, \
				"Invalid type for %s.%s" % (tbl,field)

def validateDBDefinition():
	try:
		testDBSpec_options()
		testDBSpec_fkeys()
		testDBSpec_types()
	except AssertionError, e:
		raise InvalidDatabaseStructureException(
			"Self-test indicates broken DB definition: " + str(e))

def setup(dbfile):
	"""Set up the sqlite database on first run.

	This function will set up the SQLite database during first run.
	It should not be run afterwards.

	Raises:
	sqlite3.OperationalError -- If the database already exists or syntax of
	    a SQL statement was incorrect.
	"""
	validateDBDefinition()
	cursor, conn = connect.getConnection(dbfile)
	for tbl in structure.STRUCT:
		stmt = "CREATE TABLE %s(" % tbl
		for field in structure.STRUCT[tbl]:
			cf = structure.STRUCT[tbl][field]
			stmt += "\n%s %s " % (field, cf["type"])
			if cf["primaryKey"]:
				stmt += "PRIMARY KEY "
			if cf["autoIncrement"]:
				stmt += "AUTOINCREMENT "
			if cf["notNull"]:
				stmt += "NOT NULL "
			if cf["default"] != None:
				stmt += "DEFAULT %s " % str(cf["default"])
			if cf["foreignKey"] != None:
				fk = cf["foreignKey"]
				stmt += "REFERENCES %s(%s) ON DELETE %s ON UPDATE %s " % \
					(fk["table"], fk["field"], fk["onDel"], fk["onUpd"])
			stmt = stmt[:-1] + ","
		stmt = stmt[:-1] + "\n);"
		cursor.execute(stmt)
	conn.commit()
