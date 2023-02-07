#Copyright ByteOtter (c) 2021-2022

from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flask_login import current_user, login_required
from otter_den import db
from otter_den.models import Post
from otter_den.posts.forms import PostForm
from otter_den.posts.utils import save_posted_picture, delete_from_db, delete_post_picture

posts = Blueprint('posts', __name__)


@posts.route("/posts/new", methods = ['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    post = Post()
    posted_picture = None
    if form.validate_on_submit():
        if form.picture.data:
            posted_picture = save_posted_picture(form.picture.data)
        post = Post(title = form.title.data, content = form.content.data, author = current_user, picture = posted_picture)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been shared!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_new_post.html', title = 'New Post', form=form, legend = 'Create new post')


@posts.route("/post/<int:post_id>")
def post(post_id):
    #get post with post_id or throw 404
    post = Post.query.get_or_404(post_id)
    if post.picture != None:
        image_file = url_for('static', filename = 'posted_pictures/' + post.picture)
        return render_template('post.html', title = post.title, post = post, picture = post.picture)
    else: return render_template('post.html', title = post.title, post = post, is_pinned = post.is_pinned)


@posts.route("/post/<int:post_id>/pin", methods = ['POST', 'GET'])
@login_required
def pin_post(post_id):
    post = Post.query.get_or_404(post_id)
    post.is_pinned = not post.is_pinned
    print(post.is_pinned)
    db.session.commit()
    return render_template('post.html', title = post.title, post = post, is_pinned = post.is_pinned)


@posts.route("/post/<int:post_id>/edit", methods = ['GET', 'POST'])
@login_required
def edit_post(post_id):
    form = PostForm()
    post = Post.query.get_or_404(post_id)
    #only user who wrote that post should be able to update
    if post.author != current_user:
        abort(403) #forbidden
    posted_picture = post.picture
    if form.validate_on_submit():
        if form.picture.data:
            if post.picture:
                delete_post_picture(post.picture)
            posted_picture = save_posted_picture(form.picture.data)
        post.title = form.title.data
        post.content = form.content.data
        post.picture = posted_picture
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id = post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_new_post.html', title = 'Edit Post', form = form, picture = post.picture, legend = 'Edit post')


@posts.route("/post/<int:post_id>/delete", methods = ['POST'])
@login_required
def delete_post(post_id):
    delete_from_db(post_id, send_flash = True)
    return redirect(url_for('main.home'))
