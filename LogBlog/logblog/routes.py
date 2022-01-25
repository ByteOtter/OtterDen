import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from logblog import app, db, bcrypt
from logblog.forms import RegistrationForm, LoginForm, UpdateAccountInfoForm, PostForm
from logblog.models import User, Post
from flask_login import login_user, logout_user, current_user, login_required


@app.route("/")
@app.route("/home")
def home():
    page = request.args.get('page', 1, type = int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts = posts)


@app.route("/about")
def about():
    return render_template('about.html', title = 'About LogBlog')


@app.route("/register", methods = ['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegistrationForm()
    #displays flash message when form validates successfully & redirects user to home page
    if form.validate_on_submit():
        #hash user pw and decode it into a string to be saved in the database
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash(f'Your Account has been created! Welcome, {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title = 'Register', form = form)


@app.route("/login", methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash(f'Welcome, {user.username}!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home')) #redirect to the next page if it exists, else redirect to home.
        else:
            flash('Login unsuccessful. Please check your email and password.', 'danger')
    return render_template('login.html', title = 'Login', form = form)


@app.route("/logout")
def logout():
    logout_user()
    flash('Goodbye, See you next time!', 'success')
    return redirect(url_for('home'))

#save image file the user updates. randomize the name to avoid cloissions with files the same name, split the extension off the filename and user "_" to throw away the unused filename
def save_picture(form_picture):
    random_name = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_name + f_ext
    #join together the package directory with the custom images location and the picture file name
    picture_path = os.path.join(app.root_path, 'static/profile_pictures', picture_fn)
    #resize picture to improve performance and save space
    output_size = (300, 300)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    #save image to filesystem
    i.save(picture_path)
    
    #TODO: clean up old pps after successfull change
    
    return picture_fn


def save_posted_picture(form_picture):
    random_name = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_name + f_ext
    #join together the package directory with the custom images location and the picture file name
    picture_path = os.path.join(app.root_path, 'static/posted_pictures', picture_fn)
    #resize picture to improve performance and save space
    output_size = (800, 600)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    #save image to filesystem
    i.save(picture_path)
    return picture_fn


@app.route("/account", methods = ['GET', 'POST'])
#require login to access account page
@login_required
def account():
    form = UpdateAccountInfoForm()
    #if form is valid on submit. Update the account information
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account information has been updated!', 'success')
        return redirect(url_for('account'))
    #populate form with current username and email
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    #set user profile picture as default.jpg when none is uploaded and pass to account template
    image_file = url_for('static', filename = 'profile_pictures/' + current_user.image_file)
    return render_template('account.html', title = 'My Account', image_file = image_file, 
                            form = form)


@app.route("/posts/new", methods = ['GET', 'POST'])
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
        return redirect(url_for('home'))
    return render_template('create_new_post.html', title = 'New Post', form=form, legend = 'Create new post')


@app.route("/post/<int:post_id>")
def post(post_id):
    #get post with post_id or throw 404
    post = Post.query.get_or_404(post_id)
    if post.picture != None:
        image_file = url_for('static', filename = 'posted_pictures/' + post.picture)
        return render_template('post.html', title = post.title, post = post, picture = post.picture)
    else: return render_template('post.html', title = post.title, post = post)


@app.route("/post/<int:post_id>/edit", methods = ['GET', 'POST'])
@login_required
def edit_post(post_id):
    form = PostForm()
    post = Post.query.get_or_404(post_id)
    #only user who wrote that post should be able to update
    if post.author != current_user:
        abort(403) #forbidden
    posted_picture = None
    if form.validate_on_submit():
        if form.picture.data:
            posted_picture = save_posted_picture(form.picture.data)
        post.title = form.title.data
        post.content = form.content.data
        post.picture = posted_picture
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('post', post_id = post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_new_post.html', title = 'Edit Post', form = form, picture = post.picture, legend = 'Edit post')


@app.route("/post/<int:post_id>/delete", methods = ['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    #only user who wrote that post should be able to delete
    if post.author != current_user:
        abort(403) #forbidden
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('home'))

#show complete user profile and a post history underneath
@app.route("/user/history/<string:username>")
def show_user_post_history(username):
    page = request.args.get('page', 1, type = int)
    user = User.query.filter_by(username = username).first_or_404()
    posts = Post.query.filter_by(author=user).order_by(Post.date_posted.desc()).paginate(page = page, per_page = 10)
    return render_template('post_history.html', posts = posts, user = user)
