from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
print __name__
app.config.from_object('app.config')
db = MongoEngine(app)

from app import views