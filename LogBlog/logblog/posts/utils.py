#Copyright ByteOtter (c) 2021-2022

import os
import secrets
from PIL import Image
from flask import url_for, current_app, abort, flash
from flask_login import current_user
from logblog import db
from logblog.models import Post


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

def delete_from_db(post_id, send_flash):
    post = Post.query.get_or_404(post_id)
    #only user who wrote that post should be able to delete
    if post.author != current_user:
        abort(403) #forbidden
    #remove the picture included in the post if there is any
    if post.picture != None:
        os.remove('logblog/static/posted_pictures/' + post.picture)
    db.session.delete(post)
    db.session.commit()
    if send_flash:
        flash('Your post has been deleted!', 'success')
        
