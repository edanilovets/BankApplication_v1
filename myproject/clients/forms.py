# forms.py underneath clients folder
from flask_wtf import FlaskForm
from wtforms import RadioField


class RadioForm(FlaskForm):
    deposit_filter = RadioField('Deposit type',
           choices=[('0','all'),('5','5 months'),('6','6 months'),('12','12 months'),
                    ('24','24 months'),('36','36 months')], default='0')
    deposit_mark_filter = RadioField('Deposit mark',
        choices=[('0','all'),('True','Returned'),('False', 'Not Returned')], default='0')