import pymongo
from flask import current_app as app


def mongo(data):
    # MongoDB function implementation
    client = pymongo.MongoClient(app.config['MONGODB_URI'])  # server URL
    db = client(app.config['MONGODB_NAME'])  # database
    collection = db(app.config['MONGODB_COLLECTION'])  # collection
    collection.insert_many(data)  # insert data
