from data import connect

def setup():
	"""Set up the sqlite database on first run.

	This function will set up the SQLite database during first run.
	It should not be run afterwards.
	"""
	cursor = connect.getCursor()
	