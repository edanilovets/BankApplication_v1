# myproject/deposits/views.py
from flask import Blueprint, render_template, redirect, url_for, request
from myproject import db
from myproject.models import Deposit, Currency
from myproject.deposits.forms import RadioForm

deposits_blueprint = Blueprint('deposits', __name__, template_folder='templates/deposits')

@deposits_blueprint.route('/list')
def deposits_list():
    deposits = Deposit.query.all()
    return render_template('deposits_list.html', deposits=deposits)

@deposits_blueprint.route('/currencies', methods=['GET', 'POST'])
def currencies():

    form = RadioForm()

    deposits = Deposit.query.all()
    if form.validate_on_submit():
        # show only selected options
        if form.currency_filter.data != '0':
            deposits = Deposit.query.join(Currency).filter_by(name=f'{form.currency_filter.data}').all()
    return render_template('currencies.html', deposits=deposits, form=form)