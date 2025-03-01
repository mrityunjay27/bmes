from flask import (Blueprint, request, render_template, url_for, redirect)
from datetime import datetime
from bmes.cartbp import cart_service

cart = Blueprint('cart', __name__, template_folder='templates/cartbp')
