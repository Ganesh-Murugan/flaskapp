from unicodedata import category
from main import app, db
from flask import redirect, render_template, request, url_for
from main.models import Category, Product
from flask_wtf import FlaskForm
from wtforms import SelectField

class Form(FlaskForm):
    
    category = SelectField('category', choices=[])

@app.route('/', methods=['GET','POST'])
def index():
    form=Form()
    form.category.choices = [(category.id, category.category_name) for category in Category.query.all()]
    if request.method == 'POST':
        
        res = Product.query.filter_by(category_of=form.category.data).all()
        for x in res:
            print(x.price)
        print(res)
        return render_template('home2.html', res = res, form=form)
    return render_template('index.html', form=form)
# @app.route('/')
# @app.route('/home')
# def home():
#     tables = db.engine.table_names()
#     return render_template('home.html', tables=tables)


# @app.route('/category', methods = ['GET', 'POST'])
# def categories():
#     
#     return render_template('home2.html', tables=ct)