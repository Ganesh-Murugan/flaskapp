from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Shop.db'
app.config['SECRET_KEY'] = 'secret'
db = SQLAlchemy(app)

from main import routes