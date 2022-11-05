#Copyright ByteOtter (c) 2021-2022

from flask import render_template, request, Blueprint, session, redirect
from logblog.models import Post

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type = int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts = posts)


@main.route("/about")
def about():
    return render_template('about.html', title = 'About LogBlog')


@main.route("/togge-theme")
def toggle_theme():
    current_theme = session.get("theme")
    if current_theme == "dark":
        session["theme"] = "light"
    else:
        session["theme"] = "dark"
    return redirect(request.args.get("current_page"))
