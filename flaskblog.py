from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app= Flask(__name__)

app.config['SECRET_KEY'] = '974aec450dc901b1d5c48aa69330963c'

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
def hello():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title='About')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html", title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title='Log In', form=form)

if __name__ == "__main__":
    app.run(debug=True)