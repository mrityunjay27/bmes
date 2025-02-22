from flask import  Blueprint, request, session, render_template, url_for, redirect

catalogue = Blueprint('catalogue', __name__, template_folder='templates/cataloguebp')
