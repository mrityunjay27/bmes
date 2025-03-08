from flask import (Blueprint, request,session, render_template, url_for, redirect)

checkout = Blueprint('checkout', __name__, template_folder='templates/checkoutbp')