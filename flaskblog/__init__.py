from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app= Flask(__name__)

app.config['SECRET_KEY'] = '974aec450dc901b1d5c48aa69330963c'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'

db=SQLAlchemy(app)

from flaskblog import routes