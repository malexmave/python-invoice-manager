from data import structure


cd = "from copy import deepcopy\n\n"
for tbl in structure.STRUCT:
    # Class header
    S2P = structure.SQL_TO_PY_TYPE
    camelTbl = structure.CamelCase(tbl)
    cd +=  "class %s():\n" % camelTbl
    cd += " "*4 + "def __init__(self,dat):\n"

    # Add data type checks
    for field in structure.STRUCT[tbl]:
        fd = structure.STRUCT[tbl][field]
        if fd["notNull"]:
            cd += " "*8 +"assert type(dat['{0}']) == {1}, '{0} is no {1}'\n" \
                .format(field, str(S2P[fd["type"].upper()]))
        else:
            cd += " "*8 +"assert type(dat['{0}']) in ".format(field) + \
                "[{1}, type(None)], '{0} is neither {1} nor None'\n" \
                .format(field, str(S2P[fd["type"].upper()]))
    
    # Copy data
    cd += " "*8 + "for key in dat:\n"
    cd += " "*12 + "self.__dict__['_' + key] = deepcopy(dat[key])\n\n"

    # Create getters
    for field in structure.STRUCT[tbl]:
        camelField = structure.CamelCase(field)
        cd += " "*4 + "def get{0}(self):\n".format(camelField)
        cd += " "*8 + "return self._{0}\n\n".format(field)
    cd += "\n"

# Evaluate String to generate actual datatypes
exec cd