from flask import render_template, url_for, flash, redirect, request
from logblog import app, db, bcrypt
from logblog.forms import RegistrationForm, LoginForm
from logblog.models import User, Post
from flask_login import login_user, logout_user, current_user, login_required

posts = [
    {
        'author': 'Hans Ranz',
        'title': 'Example Post 1',
        'content': 'Hans Ranz Kanns!',
        'date_posted': 'January 1, 2022'
    },
    {
        'author': 'Peter Ruprecht',
        'title': 'Example Post 2',
        'content': 'Get the hell outta here!',
        'date_posted': 'January 2, 2022'
    }
    
]

@app.route("/")
@app.route("/home")
def home():
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

#log the user out
@app.route("/logout")
def logout():
    logout_user()
    flash('Goodbye, See you next time!', 'success')
    return redirect(url_for('home'))


@app.route("/account")
#require login to access account page
@login_required
def account():
    return render_template('account.html', title = 'My Account')
