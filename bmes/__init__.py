from flask import Flask, request, session
from bmes.sharedbp import db
import os
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from bmes.cataloguebp.views import catalogue

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret-key"

app.register_blueprint(catalogue)

#Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'bmeswebapp.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

import bmes.views

@app.context_processor
def inject_context():
    """
    Contains object that is available to whole application
    :return:
    """
    return {}