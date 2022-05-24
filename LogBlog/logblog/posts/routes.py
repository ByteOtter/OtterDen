from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flask_login import current_user, login_required
from logblog import db
from logblog.models import Post
from logblog.posts.forms import PostForm
from logblog.posts.utils import save_posted_picture

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


@posts.route("/post/<int:post_id>/pin")
def pin_post(post_id):
    is_pinned = request.args.get('is_pinned', type = bool)
    print(is_pinned)
    post = Post.query.get_or_404(post_id)
    post.is_pinned = is_pinned
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
    post = Post.query.get_or_404(post_id)
    #only user who wrote that post should be able to delete
    if post.author != current_user:
        abort(403) #forbidden
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))
