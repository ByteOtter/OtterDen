# Welcome to LogBlog!

LogBlog is (going to be) a small and simple Flask-based Blog application with database and everything.

Please note that this application is for testing and learning purposes only and not meant to be deployed in any capacity. **Security flaws are bound to be present**. Feel free to report or fix any bugs you find.

Thank you!

#### - ByteOtter

### How to Install

If you want to pull and install this application you need to create a database and pass it to the application. The app can't do that on its own yet. I am working on a fix.

To install this app you need to...

...make sure that you have python3 and pip installed

...pull the repository

...make sure pip installs all of logblog's requirements

...specifythe path to your database as an environment variable. Check config.py for the variable name and run something like this:

    - SQLALCHEMY_DATABASE_URI = sqlite:///logBlogDEV.py

...run the following commands in your python interpreter while in the LogBlog directory:

    - from main import create_app //this imports the create_app function from main.py
    - from logblog import db //imports the db variable and database instance
    - app = create_app()
    - app = app.app_context().push() //push the app app_context
    - db.create_all()

