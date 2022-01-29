import os
import secrets
from PIL import Image
from logblog import db
from flask import url_for, current_app

def save_posted_picture(form_picture):
    random_name = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_name + f_ext
    #join together the package directory with the custom images location and the picture file name
    picture_path = os.path.join(current_app.root_path, 'static/posted_pictures', picture_fn)
    #resize picture to improve performance and save space
    output_size = (800, 600)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    #save image to filesystem
    i.save(picture_path)
    return picture_fn
