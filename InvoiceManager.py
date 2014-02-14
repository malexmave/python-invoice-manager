import nose
import data.initialize
import os


def main():
	nose.main(defaultTest='tests')

if __name__ == '__main__':
	if not os.path.isfile("data.db"):
		try:
			data.initialize.setup("data.db")
		except Exception, e:
			print "Error while initiating Database:", str(e)
	else:
		print "Database exists."
	main()