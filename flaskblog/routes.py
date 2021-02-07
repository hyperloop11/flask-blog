from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.models import User, Post
from flaskblog.forms import RegistrationForm, LoginForm


posts=[
    {
        'author':'man 1',
        'title' : 'blog post 1',
        'content': 'content blog 1',
        'date_posted': '12 feb 2021'
    },
    {
        'author':'man 2',
        'title' : 'blog post 2',
        'content': 'content blog 2',
        'date_posted': '14 feb 2021'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        #2 parameters for falsh, latter is name of bootstrap message
        flash(f'Account created for {form.username.data}.', 'success')

        return redirect(url_for('home')) 

    return render_template("register.html", title='Register', form=form)

@app.route("/login",methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'hello@gmail.com' and form.password.data=="12345":
            flash('You logged in successfully', 'success')
            return redirect(url_for('home'))
        else:
            flash('log in unsuccessful. Please enter correct email and password.', 'danger')
    return render_template("login.html", title='Log In', form=form)
