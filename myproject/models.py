# db initialized in __init__.py under myproject
from myproject import db

class Deposit(db.Model):
    __tablename__ = 'deposits'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    deposit_min_term = db.Column(db.Integer)
    deposit_min_sum = db.Column(db.Numeric)

    # Connect the deposit to the currency
    currency_id = db.Column(db.Integer, db.ForeignKey('currencies.id'))
    currency = db.relationship('Currency', backref='deposit', uselist=False)

    def __init__(self, name, deposit_min_term, deposit_min_sum, currency_id):
        self.name = name
        self.deposit_min_term = deposit_min_term
        self.deposit_min_sum = deposit_min_sum
        self.currency_id = currency_id

    def __repr__(self):
        return f"Deposit name is {self.name}"


class Currency(db.Model):
    __tablename__ = 'currencies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    exchange_rate = db.Column(db.Numeric)

    def __init__(self, name, exchange_rate):
        self.name = name
        self.exchange_rate = exchange_rate

    def __repr__(self):
        return f"Currency name is {self.name}"


class Client(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    address = db.Column(db.Text)
    phone_number = db.Column(db.Text)
    passport = db.Column(db.Text)
    deposit_date = db.Column(db.DateTime)
    deposit_return_date = db.Column(db.DateTime)

    # Connect the client to the deposit
    deposit_id = db.Column(db.Integer, db.ForeignKey('deposits.id'))
    deposit = db.relationship('Deposit', backref='client', uselist=False)

    deposit_sum = db.Column(db.Numeric)
    deposit_return_sum = db.Column(db.Numeric)
    deposit_return_mark = db.Column(db.Boolean)

    def __init__(self, name, address, phone_number, passport, deposit_date,
                 deposit_return_date, deposit_id, deposit_sum,
                 deposit_return_sum, deposit_return_mark, employee_id):

        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.passport = passport
        self.deposit_date = deposit_date
        self.deposit_return_date = deposit_return_date
        self.deposit_id = deposit_id
        self.deposit_sum = deposit_sum
        self.deposit_return_sum = deposit_return_sum
        self.deposit_return_mark = deposit_return_mark

    def __repr__(self):
        return f"Client name is {self.name}"
