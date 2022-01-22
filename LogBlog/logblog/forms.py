from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from logblog.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired(), Length(min = 5, max = 20)])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired(), Length(min = 5)])
    confirm_password = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password', message = "Your passwords do not match!")])
    submit = SubmitField('Sign Up')
    
    #check if username already in use
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('A user with this username already exists!')
    
    #check if email already in use
    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('An account is already registered with this email!')

class LoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired(), Length(min = 5)])
    remember = BooleanField('Remember me?')
    submit = SubmitField('Sign In')