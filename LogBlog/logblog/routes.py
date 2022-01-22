from flask import render_template, url_for, flash, redirect
from logblog import app
from logblog.forms import RegistrationForm, LoginForm
from logblog.models import User, Post

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
    form = RegistrationForm()
    #displays flash message when form validates successfully & redirects user to home page
    #TODO: This does not redirect the User to the home page yet! Fix it!
    if form.validate_on_submit():
        flash(f'Your Account has been created! Welcome, {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form = form)


@app.route("/login", methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    #temporary code to simulate login!
    if form.validate_on_submit():
        if form.email.data == 'admin@logBlog.com' and form.password.data == 'password':
            flash(f'Welcome,  {form.email.data}', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check your email and password.', 'danger')
    return render_template('login.html', title = 'Login', form = form)
