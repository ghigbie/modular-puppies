import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = 'myscretkey'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

<<<<<<< HEAD
# Blueprints must be resgistered after db
from myproject.puppies.views import puppies_blueprint
from myproject.owners.views import owners_blueprint

app.register_blueprint(owners_blueprint, url_prefix='/owners')
app.register_blueprint(puppies_blueprint, url_prefix='/puppies')
=======
from myproject.puppies.views import puppies_blueprint
from myproject.owners.views import owners_bluprint

app.register_blueprint(puppies_blueprint, url_prefix='/puppies')
app.register_blueprint(owners_bluprint, url_prefix='/owners')
>>>>>>> 7065eb3a8961dbc10b821b79b8f36ade66f13785
