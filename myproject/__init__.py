import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import flask_migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = 'myscretkey'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir)
app.config['SQLALCHEMY_TRACK_MODIFCATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)