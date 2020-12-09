# forms.py underneath deposits folder
from flask_wtf import FlaskForm
from wtforms import RadioField


class RadioForm(FlaskForm):
    currency_filter = RadioField('Currency filter',
        choices=[('0','all'),('USD','USD'),('EUR', 'EUR'),('RUB', 'RUB')], default='0')