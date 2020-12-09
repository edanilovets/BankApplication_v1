import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# FLASK APP
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# FLASK APP CONFIG
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# KEY FOR FORMS
app.config['SECRET_KEY'] = 'my_secret_key'

# SET UP SQLALCHEMY
db = SQLAlchemy(app)
Migrate(app, db)

# SET UP BLUEPRINTS
from myproject.clients.views import clients_blueprint
from myproject.currencies.views import currencies_blueprint
from myproject.deposits.views import deposits_blueprint

app.register_blueprint(clients_blueprint, url_prefix='/clients')
app.register_blueprint(currencies_blueprint, url_prefix='/currencies')
app.register_blueprint(deposits_blueprint, url_prefix='/deposits')
