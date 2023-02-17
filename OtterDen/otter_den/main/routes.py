# Copyright ByteOtter (c) 2021-2023

from flask import render_template, request, Blueprint, session, redirect
from otter_den.models import Post

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type = int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', title = 'Home', posts = posts)


@main.route("/about")
def about():
    return render_template('about.html', title = 'About')

@main.route("/topic/<string:topic>")
def topic_channel(topic):
    page = request.args.get('page', 1, type=int)
    if topic == 'Undefined':
        posts = Post.query.filter_by(topic='').order_by(Post.date_posted.desc()).paginate(page=page, per_page=10)
        return render_template('topic_channel.html', topic = 'Undefined', title = 'Misc', posts = posts)
    posts = Post.query.filter_by(topic=topic).order_by(Post.date_posted.desc()).paginate(page=page, per_page=10)
    return render_template('topic_channel.html',topic = topic, title = topic, posts = posts)


@main.route("/toggle-theme")
def toggle_theme():
    current_theme = session.get("theme")
    if current_theme == "dark":
        session["theme"] = "light"
    else:
        session["theme"] = "dark"
    return redirect(request.referrer)

@main.route("/license")
def license():
    return render_template('license.html', title = 'License')
