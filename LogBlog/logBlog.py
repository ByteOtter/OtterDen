from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

##secret key for tampering protection. 256 Bit python key from secrets module. THIS IS NOT GOOD ENOUGH OF A SOLUTION.
app.config['SECRET_KEY'] = '7e71d5735808a54d9a38d1ebc573ac1429242e464f7f322413a2c8e44392d37d11827c8792c81ca3ccc5cab4bbd5f2d3442823e6919ff74e3339199bd143e81da2e83ff986b2965742ae9b900b1811226b93b01d85ae3d86dd6f5ba6e7aea85d08bc6998f90402310c0ba86519a4d8d56eb5fb1bdcab1e90dc54cfde0164c89f60eeb198c74c813f3eb3e165e767f0d47aa8b1ba33c3fbe6461dc151430f7d46a5480306f87aaae953f5e2570d28663b6100ff06ed7c494c5cadcdac79b03d175288da284e327eab7c38f52b41a641176c66ece2b7083d180f7353f52adb42d6f897801c2639c1a5d6224db8b54985e5410e70b6e198c19de8fa549b474d1e43'

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


if __name__ == '__main__':
    app.run(debug=True)
