#Copyright ByteOtter (c) 2021-2022

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
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


class UpdateAccountInfoForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired(), Length(min = 5, max = 20)])
    email = StringField('Email', validators = [DataRequired(), Email()])
    picture = FileField('Update Avatar', validators = [FileAllowed(['jpg', 'jpeg', 'png', 'webp', 'gif'])])
    biography = StringField('About you (max 250 characters)', validators = [Length(max = 250)])
    submit = SubmitField('Update your info!')

    # check if username already in use
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username = username.data).first()
            if user:
                raise ValidationError('A user with this username already exists!')

    # check if email already in use
    def validate_email(self, email):
        if email.data != current_user.email:
            email = User.query.filter_by(email = email.data).first()
            if email:
                raise ValidationError('An account is already registered with this email!')


class RequestPasswordResetForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    submit = SubmitField('Request password reset')

    # check if email does not exsists
    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user is None:
            raise ValidationError('There is no account with this email!')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators = [DataRequired(), Length(min = 5)])
    confirm_password = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password', message = "Your passwords do not match!")])
    submit = SubmitField('Confirm password reset')
