.PHONY: app

install:
	@echo "Installing dependencies..."
	@pip install -r requirements.txt
	@pip install flask beautifulsoup4 selenium pymongo webdriver_manager
	@echo "Done"

run:
	@echo "Running app..."
	@python Blogster.py

run3:
	@echo "Running app..."
	@python3 Blogster.py