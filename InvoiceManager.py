import unittest
import tests.data

def suite():
	suite = unittest.TestSuite()
	suite.addTest(tests.data.suite())
	return suite

def main():
	unittest.main(defaultTest='suite')

if __name__ == '__main__':
	main()