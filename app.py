# This is app.py, this is the main file called.
from myproject import app
from flask import render_template

"""
export FLASK_APP=~/Desktop/KPI/Semester_5/Python/BankApplication_v1/app.py
flask db init
flask db migrate -m "initial migration"
flask db upgrade
"""


@app.route('/')
def index():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
