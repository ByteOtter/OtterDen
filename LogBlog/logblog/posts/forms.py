from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed

class PostForm(FlaskForm):
    title = StringField('Title', validators = [DataRequired()])
    content = TextAreaField('Content', validators = [DataRequired()])
    picture = FileField('Add media', validators = [FileAllowed(['jpg', 'jpeg', 'png', 'svg', 'webp', 'gif', 'bmp'])])
    submit = SubmitField('Post')
