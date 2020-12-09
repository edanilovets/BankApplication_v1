from myproject import db
from myproject.models import Deposit, Currency, Client
from myproject import app
from datetime import datetime

# database from app must exist
def create_tables():
    with app.test_request_context():
        db.init_app(app)
        db.create_all()


def populate_tables():
    # Create 5 deposits
    deposits = [
        Deposit("Deposit on 5 months", 5, 10000, 1),
        Deposit("Deposit on 6 months", 6, 15000, 2),
        Deposit("Deposit on 12 months", 12, 10000, 2),
        Deposit("Deposit on 24 months", 24, 20000, 3),
        Deposit("Deposit on 36 months", 36, 40000, 3)
    ]
    # Create 3 currencies
    currencies = [
        Currency("USD", 27.8),
        Currency("RUB", 57.0),
        Currency("EUR", 30.3)
    ]
    # Create 10 clients
    clients = [
        Client("Eugene Poplavskiy", "Kyiv, Lomonosova st. 52", "380970359901",
               "MP-453222", datetime(2015, 10, 15, 12, 0, 0), datetime(2016, 10, 15, 14, 0, 15),
               1, 30000, 50000, True, 2),
        Client("Yakov Ivankiv", "Kyiv, Banderu st. 111", "380973453901",
               "MP-345678", datetime(2019, 11, 10, 11, 0, 10), None,
               2, 440000, None, False, 4),
        Client("Klara Mart", "Lviv, Agness st. 33", "380980354901",
               "DA-343355", datetime(2020, 10, 15, 12, 0, 0), None,
               3, 1000000, None, False, 3),
        Client("Denys Ladkov", "Kharkov, Olesya Kurbasa st. 2", "380730119901",
               "MP-342211", datetime(2014, 12, 14, 15, 40, 1), datetime(2016, 10, 18, 14, 12, 0),
               4, 34000, 78000, True, 10),
        Client("Eugene Danilovets", "Kyiv, Lomonosova st. 52", "380970359901",
               "MP-453222", datetime(2018, 10, 15, 12, 0, 0), datetime(2020, 12, 12, 13, 0, 0),
               4, 200000, 550000, True, 9),
        Client("Egor Molyavko", "Kyiv, Leontovicha av. 11", "380730354401",
               "KD-908710", datetime(2019, 10, 15, 12, 0, 0), None,
               5, 44550, None, False, 9),
        Client("Nataliya Komarova", "Kyiv, Ivana Mazepu st. 1", "0443569087",
               "ER-463789", datetime(2014, 3, 3, 12, 33, 0), datetime(2018, 3, 5, 9, 26, 30),
               5, 890000, 1430000, True, 4),
        Client("Gilbert Lord", "London, Bruce Loyd st. 88", "40554435544",
               "D-43222", datetime(2020, 4, 4, 12, 0, 0), None,
               3, 440000, None, False, 7),
        Client("Eugene Poplavskiy", "Kyiv, Lomonosova st. 52", "380970359901",
               "MP-453222", datetime(2015, 1, 13, 18, 4, 5), None,
               3, 340000, None, False, 5),
        Client("Egor Molyavko", "Kyiv, Leontovicha av. 11", "380730354401",
               "KD-908710", datetime(2020, 10, 15, 16, 33, 0), None,
               5, 89725, None, False, 1)
    ]

    db.session.add_all(deposits)
    db.session.add_all(currencies)
    db.session.add_all(clients)
    db.session.commit()


if __name__ == '__main__':
    create_tables()
    populate_tables()
