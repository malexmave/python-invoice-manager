import unittest
import tests.datatest

def suite():
	suite = unittest.TestSuite()
	suite.addTest(tests.datatest.suite())
	return suite

def main():
	unittest.main(defaultTest='suite')

if __name__ == '__main__':
	main()