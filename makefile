test : 
	nosetests --with-coverage --cover-branches --cover-html

clean :
	find . -iname '*.pyc' -exec rm {} \;
