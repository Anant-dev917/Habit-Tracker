import os
from flask import Flask
from routes import pages
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__,static_folder="pretty_stuff")
    app.register_blueprint(pages)
    Client = MongoClient(os.environ.get("MONGODB_URI"))

    #Creates a MongoDB database of the name as specified at the end of the MONGODB_URI in .env file
    app.db = Client.get_default_database()

    return app




