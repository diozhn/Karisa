run:
	python3 src/main.py

install:
	pip install -r requirements/common.txt

replit_install:
	pip install -r requirements/replit.txt

replit:
	make replit_install
	make run
