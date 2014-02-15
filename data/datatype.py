from data import structure
import re

def _CamelCase(mobj):
	rv = mobj.group(0)[1:]
	return rv.upper()


classdef = "from copy import deepcopy\n\n"
for tbl in structure.STRUCT:
	# Class header
	camelTbl = re.sub('_.', _CamelCase, tbl.capitalize())
	classdef +=  "class %s():\n" % camelTbl
	classdef += " "*4 + "def __init__(self,dat):\n"

	# Add data type checks
	for field in structure.STRUCT[tbl]:
		fd = structure.STRUCT[tbl][field]
		if fd["notNull"]:
			classdef += " "*8 +"assert type(dat['%s']) == %s, '%s is no %s'\n"\
			    % (field, str(structure.SQL_TO_PY_TYPE[fd["type"].upper()]), \
			    	field, str(structure.SQL_TO_PY_TYPE[fd["type"].upper()]))
		else:
			classdef += " "*8 +"assert type(dat['%s']) in " % field + \
				"[%s, type(None)], '%s is neither %s nor None'\n" \
				% (str(structure.SQL_TO_PY_TYPE[fd["type"].upper()]), \
					field, str(structure.SQL_TO_PY_TYPE[fd["type"].upper()]))
	
	# Copy data
	classdef += " "*8 + "for key in dat:\n"
	classdef += " "*12 + "self.__dict__['_' + key] = deepcopy(dat[key])\n\n"

	# Create getters
	for field in structure.STRUCT[tbl]:
		camelField = re.sub('_.', _CamelCase, field.capitalize())
		classdef += " "*4 + "def get%s(self):\n" % camelField
		classdef += " "*8 + "return self._%s\n\n" % field
	classdef += "\n"
exec classdef