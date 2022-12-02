# Contributing

Thank you for wanting to contribute to LogBlog!<br>
This guide will explain how to make contributions to this project as smooth and easy as possible.

## Index - So you know where to start

1. [New to OpenSource? Start here!](#NewToOSS)
2. [Getting started](#GettingStarted)
    1. [Getting the Repository](#GetIt)
    2. [Setting up LogBlog](#SetUp)
3. [Making Changes](#ContributingChanges)
    1. [Testing your changes manually](#ManualTesting)
    2. [Changeing the Testsuite](#AutomatedTesting)
4. [Contributing Checklist](#CommitChecklist)
5. [Help](#Help)

## 1. New to OpenSource? Start here!<a name="NewToOSS"></a>

Contributions to Open Source projects are a fantastic way to learn the ropes of software development and<br>
provide potential future employers with a public record of your skills and interests in the field.<br>
Aside from that the most important and cherished resource for any OSS are contributors like **You**!<br>

Before we can get into the nitty gritty details of how to contribute to LogBlog though, there are some prerequisites you need to familiarize yourself with before starting.

The first, and most obvious one, is familiarizing yourself with the version control system `git`.<br>
If you do not know `git` or are insecure during your work you can always refer to the official [`git` documentation](https://git-scm.com/book/en/v2).<br>
Important for your work on LogBlog will be the following chapters:

1. [Installing `Git`](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
2. [First Time Setup](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)
3. [Getting a Repository (Cloning)](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository)
4. [Recording changes to a Repository](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository)
5. [Working with remotes](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes)
6. [Working with branches](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell)

When in doubt about how something works with `git` you can refer to the documentation linked above and take a look at the [Getting Help](https://git-scm.com/book/en/v2/Getting-Started-Getting-Help) section.<br>

This seems like a lot of work to get started with it, but once you committed a few changes all of this will come natural to you. Or at least it will not get in your way anymore. ;)

***

## 2. Getting Started<a name="GettingStarted"></a>

When you have familiarized youself with `git` you can start setting up your work environment.

### 2.1 Getting the repository<a name="GetIt"></a>

Getting a `GitHub` repository is pretty straight forward.

First, I would recommend creating a directory where you keep all your OSS work related project directories. So something like a `Dev` directory in your `home/` folder or anywhere else you would like.

Then go to [LogBlogs `GitHub` page](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell) and click the green `Code` button.<br>
Select the SSH tab and copy the link shown in the dropdown menu.

After that, while inside your `Dev/` directory, run the following command on your command line.

```
git clone git@github.com:ByteOtter/LogBlog.git
```

You may be asked to enter the credentials for your `SSH Public Key` and once you enter it `git` will download all files stored in the repository.<br>
Once this is done you should see a `LogBlog/` directory in your `Dev/` folder. This is LogBlog how it lives and breathes - almost.

I know you want to start now, but there are some steps left before you can do so.

Before we touch the repository you should go back to LogBlogs `GitHub` page and click the `Fork` button in the top right corner.<br>
This will **create a copy of LogBlog in your own `GitHub` account.** Some people would call this piracy; not so the open source community!<br>
Jokes aside, you are probably wondering why you need a copy in your own account when you already pulled it. Let me explain:

When contributing to an Open Source project, or any software project for that matter, it can always happen that you make changes which would break the project. To avoid this it is necessary that you *do not* push your code into the project directly. Some projects even *require* you to push code into your own fork first. How your changes end up in `LogBlog`? With a great little feature called a `Pull Request`!<br>
A `Pull Request` can be created after pushing changes to any branch of your fork and is a formal request to the maintainers of the original project to merge your changes with the original codebase. (Note that creating a `Pull Request` is by no means mandatory. Forks can be used to branch off a existing project and publish your very own version that is how you like it! Isn't Open Source (depending on the license) amazing!)<br>

Anyhow, when you have created a fork of LogBlog in your own profile you need to run the following commands on your command line while you are withing the `Dev/LogBlog/` directory:

```
git remote add fork git@github.com:[YourUserName]/LogBlog.git
```
This will add your fork to the list of existing locations `git` can `push` into or `pull` from.<br>
If you now run `git remote -v` to check what that list looks like it should look like this:

```
fork git@github.com:[YourUserName]/LogBlog.git (fetch)
fork git@github.com:[YourUserName]/LogBlog.git (push)
origin git@github.com:ByteOtter/LogBlog.git (fetch)
origin git@github.com:ByteOtter/LogBlog.git (push)
```
`Origin` in this list is the original repository (as you might have guessed) and `fork` your copy of it in your own `GitHub` account.<br>
Now `git` knows to pull all new changes from the `origin` remote and push all of your custom changes you are working on to your own fork.

Great! Now we can start setting up LogBlog itself! Finally!
***
### 2.2 Setting up LogBlog

You have made it this far, stick to it and you will be working with Open Source Software in no time!

Setting up LogBlog does require a little bit more configuration.<br>
After cloning the repository, make sure you have the newest [Python](https://www.python.org/) version and the Python package manager [`Pip`](https://pypi.org/project/pip/) installed.

After that, while in the `Dev/LogBlog/` directory run:

```
pip install -r requirements.txt
```
Pip will now install all necessary requirements to run LogBlog on your system.

Once Pip is done we need the command line again.<br>
We need to set an environment variable to let the operating system know where our database will be located. How that is done varies from OS to OS so you need to ask Dr. Google for help if the following command does not work.
```
SQLALCHEMY_DATABASE_URI='sqlite:///logBlogDEV.db'
```
Sometimes it is necessary to add this line directly to the file where these variables are stored. In Linux this is in `etc/environment`.

Once that is done, while in the `Dev/LogBlog/LogBlog/`directory, open the python interpreter in your command line by running `python3` then enter the following:
```
from main import create_app
from logblog import db
db.create_all(app=create_app())
```
This will create the database file aswell as initialize the app.

That's it! You can now run `python3 main.py` while in the `Dev/LogBlog/LogBlog/` directory to run LogBlog! Good job! :)
***
## 3. Making Changes<a name="Contributing Changes"></a>

Now, finally you are set up to tinker around with the codebase as you please. Feel free to really examine every file and function and get an idea of how everything works! :)

***

### 3.1 Testing your changes manuall<a name=ManualTesting></a>

The easiest way to test if what you write works is to keep an instance of LogBlog running in a dedicated command line/terminal window. If it crashes, you know your code is broken. :P<br>
If it does not crash, you can simply and easily open the browser, pull up LogBlog by going to `localhost:5000/` and click yourself through and see if the behaviour you expect your change to have shows up.

When all looks good you can commit your changes and open a pull request!

***

### 3.2 Changing the Testsuite<a name=AutomatedTesting></a>

LogBlog offers a automated testsuite using `Selenium` and the `Behave` framework to automatically click itself through the WebUI and observe LogBlogs behaviour using pre defined test scenarios you can find in `testsuite/features`.<br>
Whether you test your changes locally or use this testsuite, larger changes and especially new features will require the Testsuite to be adapted or expanded.<br>
I strongly encourage you to do this yourself in parallel to your change if it is necessary. Not only would lead this to your PR being merged quicker but it also would help me out greatly.<br>
However, I can understand when you do not touch the testsuite as `Selenium` can be pain in the buttocks. :P

In this case after opening a pull request please also open a Feature Request by clicking on `Issues` and `New Issue` and select `Feature Request`. Please add here what you changed and what needs to be done to the testsuite and add the `testsuite` label to it. Then take the URL and add it to your PRs `Links` section.

The help is very appreciated! :)

***

## 4. Contributing Checklist<a name=CommitChecklist></a>

Finally you have made it to the point you wanted to read all along: The checklist of how to commit changes to LogBlog!<br>
Simply follow these steps and your pull request is open in no time!

1. Run `git status` to list all of your changes and once satisfied...
2. ... run `git add path/to/your/changed/file` to add the file or files to your `commit`
3. Then open a new `branch` with `git checkout -b your-branch-name`so your suggested change can be thuroughly examined without breaking anything ;P
4. Once on a new branch type `git commit -m "Your Commit Message"` to create a new commit with a *helpful* commit message. Please be aware that you should use this for a short summary of what this commit does and it should be formulated in an active form. (e.g "Add user page"/"Fix crash...", etc)
5. Push your changes with `git push fork`. This will push your custom branch with all the changes to your copy of LogBlog.
6. Visit the `GitHub` page of your LogBlog fork, you should see an orange banner saying `your-branch-name had recent commits` with a green button next to it saying `create pull request`. Click that button.
7. This brings you to the create pull request editor. You can see that the window has been pre-filled with a pull request template so check your boxes and provide a clear explanation of what your change does.
8. Once you are done and all the automatic checks are green, click `Create Pull Request`
9. Wait. You can assign someone to review your request but this should not be necessary as I get notified when you open a PR. How long it will take to review? That sadly varies wildly depending on what your commit does, but I will get back to you if something comes up!

That's it. You have committed your first change! Thank you!

But **don't forget**: Once your changes have been merged you need to check out your master branch in your `Dev/LogBlog/` repository and pull the newest version of LogBlog by running `git pull` or `git pull origin master`!

***

## 5. Help<a name="Help"></a>

If you, at any point need help or have questions about anything LogBlog related you can contact me here:

- christopher-hock@protonmail.com

**Further information coming soon!**
