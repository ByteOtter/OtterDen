import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from logblog import mail

#save image file the user updates. randomize the name to avoid cloissions with files the same name, split the extension off the filename and user "_" to throw away the unused filename
def save_picture(form_picture):
    random_name = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_name + f_ext
    #join together the package directory with the custom images location and the picture file name
    picture_path = os.path.join(current_app.root_path, 'static/profile_pictures', picture_fn)
    #resize picture to improve performance and save space
    output_size = (300, 300)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    #save image to filesystem
    i.save(picture_path)
    
    #TODO: clean up old pps after successfull change
    
    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender = 'info.logblog@gmail.com', recipients = [user.email])
    msg.body = f'''Hey, we have recieved a request to reset your password!
Just follow this link:

    {url_for('users.reset_password', token = token, _external = True)}

If you did not request a password reset, simply ignore this email.        
'''
    mail.send(msg)
