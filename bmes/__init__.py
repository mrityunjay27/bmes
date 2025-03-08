from flask import Flask, request, session

from bmes.cartbp import cart_service
from bmes.sharedbp import db
import os
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from bmes.cataloguebp.models import Brand, Category, Product, ProductAdmin
from bmes.cataloguebp.views import catalogue
from bmes.cartbp.views import cart
from bmes.locationbp.views import location

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# App Secret key
app.config["SECRET_KEY"] = "secret-key"

# Blueprint registration
app.register_blueprint(catalogue)
app.register_blueprint(cart)
app.register_blueprint(location)

#Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'bmeswebapp.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Registering The Product Catalogue Models to the Admin Module
# This allows to perform CRUD on following tables from Admin module.
admin = Admin(app)
admin.add_view(ProductAdmin(Product, db.session))
admin.add_view(ModelView(Category, db.session))
admin.add_view(ModelView(Brand, db.session))

db.init_app(app)
migrate = Migrate(app, db)

import bmes.views

@app.context_processor
def inject_context():
    """
    Contains object that is available to whole application
    :return:
    """
    return {
              'cart_item_count': cart_service.cart_items_count(request,session),
              'cart_total': cart_service.get_cart_total(request, session),
              'cart_items': cart_service.get_cart_items(request,session),
           }