# myproject/clients/views.py
from flask import Blueprint, render_template, redirect, url_for, request
from myproject import db
from myproject.models import Client, Deposit
from myproject.clients.forms import RadioForm

clients_blueprint = Blueprint('clients', __name__, template_folder='templates/clients')

@clients_blueprint.route('/list')
def clients_list():
    clients = Client.query.all()
    return render_template('clients_list.html', clients=clients)

@clients_blueprint.route('/deposit_clients', methods=['GET', 'POST'])
def deposit_clients():

    form = RadioForm()

    clients = Client.query.all()
    if form.validate_on_submit():
        # show only selected options
        if form.deposit_mark_filter.data == '0' and form.deposit_filter.data == '0':
            clients = Client.query.all()
        elif form.deposit_filter.data == '0':
            clients = Client.query.filter_by(deposit_return_mark=f'{form.deposit_mark_filter.data}').all()
        elif form.deposit_mark_filter.data == '0':
            clients = Client.query.join(Deposit).filter_by(name=f'Deposit on {form.deposit_filter.data} months').all()
        else:
            clients = Client.query.filter_by(deposit_return_mark=f'{form.deposit_mark_filter.data}').join(Deposit).filter_by(name=f'Deposit on {form.deposit_filter.data} months').all()
    return render_template('deposit_clients.html', clients=clients, form=form)
