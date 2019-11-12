from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, RadioField
from wtforms.validators import DataRequired, Length, EqualTo
from booking import IATA


class AirportsForm(FlaskForm):
    from_airport = StringField('fromIATA', validators=[DataRequired()])
    to_airport = StringField('toIATA', validators=[DataRequired()])
    when = DateField('dates')
    seat_class = RadioField('seats')
    submit = SubmitField('Search')