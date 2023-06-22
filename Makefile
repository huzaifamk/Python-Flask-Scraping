.PHONY: app

install:
	@echo "Installing dependencies..."
	@pip install -r requirements.txt
	@pip install flask beautifulsoup4 selenium pymongo webdriver_manager
	@echo "Done"

run:
	@echo "Running app..."
	@python app.py

run3:
	@echo "Running app..."
	@python3 app.py

clean:
	@echo "Cleaning up..."
	@rm -rf __pycache__/
	@rm -rf .pytest_cache/