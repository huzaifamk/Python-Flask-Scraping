from flask import Flask
from scraper.scraper import scrape
from config.config import Config

# Initialize Flask app
app = Flask(__name__)

# Load config
app.config.from_object(Config)

# Register routes
app.route('/api/v1/scrape', methods=['POST'])(scrape)

if __name__ == '__main__':
    app.run()
