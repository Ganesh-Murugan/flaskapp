from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Shop.db'
db = SQLAlchemy(app)
class Category(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    category_name = db.Column(db.String(length=20), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    subitems = db.relationship('Subcate', backref='belong_to', lazy=True)

    
    def __repr__(self) -> str:
        return f'Item {self.category_name}'

class Subcate(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    subcate_name = db.Column(db.String(length=20), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    belong = db.Column(db.Integer(), db.ForeignKey('category.id'))
    products = db.relationship('Product', backref='product_of', lazy=True)

class Product(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    product_name = db.Column(db.String(length=20), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    category_of = db.Column(db.Integer(), db.ForeignKey('category.id'))
    subcate_of = db.Column(db.Integer(), db.ForeignKey('subcate.id'))

    # def __repr__(self) -> str:
    #     return f'Item {self.product_name}'