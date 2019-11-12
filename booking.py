from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
# from forms import AirportsForm
# from pyairports import airports

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db.SQLAlchemy(app)

class IATA(db.Model):
    code = db.Column(db.String(3))
    airport = db.Column(db.String(50))

db.create_all()

@app.route("/")
@app.route("/booking")
def bookingweb():
    form = AirportsForm()
    return render_template('bookingweb.html', title='Booking', form=form)

if __name__ == '__main__':
    app.run(debug=True)