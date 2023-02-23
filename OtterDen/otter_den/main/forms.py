#Copyright ByteOtter (c) 2023

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Regexp

class SearchForm(FlaskForm):
    query = StringField('Search', validators = [DataRequired(), Regexp('[^\s]{5,20}', message="Username cannot contain whitespaces!")])
    submit = SubmitField('GET')
