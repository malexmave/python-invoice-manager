import nose
# import data.initialize
# import os
# import tests.testDatatypes

dbfile = "data.db"

def main():
	nose.main(defaultTest='tests')

if __name__ == '__main__':
	# if not os.path.isfile(dbfile):
	#	try:
	#		data.initialize.setup(dbfile)
	#	except Exception, e:
	#		print "Error while initiating Database:", str(e)
	# else:
		# print "Database exists."
		# try:
		# data.initialize.checkConformity(dbfile)
		# except Exception, e:
		#	print "Error while checking Database validity:", str(e)
		#	raise e
	main()
	pass