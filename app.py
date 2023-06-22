from flask import Flask, request
from utils.scraping import scrape, process
from config.config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Register routes
app.route('/api/v1/scrape', methods=['POST'])(scrape)
app.route('/api/v1/process', methods=['POST'])(process)

if __name__ == '__main__':
    app.run()
