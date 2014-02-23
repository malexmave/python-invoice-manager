test : 
	nosetests --with-coverage --cover-branches --cover-html
	rm test.*.db

clean :
	find . -iname '*.pyc' -exec rm {} \;
