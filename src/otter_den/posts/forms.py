#Copyright ByteOtter (c) 2022

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FileField, SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed

class PostForm(FlaskForm):
    title = StringField('Title', validators = [DataRequired()])
    content = TextAreaField('Content', validators = [DataRequired()])
    picture = FileField('Add media', validators = [FileAllowed(['jpg', 'jpeg', 'png', 'svg', 'webp', 'gif', 'bmp'])])
    topic = SelectField('Select Topic', choices=[('', '----'), ('Art & Photography', 'Art & Photography'), ('Technology', 'Technology'), ('Programming', 'Programming'), ('Gaming', 'Gaming'), ('Movies', 'Movies'), ('Literature', 'Literature'), ('Food', 'Food'), ('Animals', 'Animals')])
    submit = SubmitField('Post')
