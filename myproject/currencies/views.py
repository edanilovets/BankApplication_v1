# myproject/currencies/views.py
from flask import Blueprint, render_template, redirect, url_for, request
from myproject import db
from myproject.models import Currency

currencies_blueprint = Blueprint('currencies', __name__, template_folder='templates/currencies')

@currencies_blueprint.route('/list')
def currencies_list():
    currencies = Currency.query.all()
    return render_template('currencies_list.html', currencies=currencies)