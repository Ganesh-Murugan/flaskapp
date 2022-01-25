from operator import sub
from unicodedata import category
from main import app, db
from flask import jsonify, redirect, render_template, request, url_for
from main.models import Category, Product, Subcate
from main.forms import Category_form, delete_form, View
import sqlite3

x = Category.query.all()

@app.route('/', methods=['GET','POST'])
def index():
    form=View()
    form.category.choices = [(category.id, category.category_name) for category in x]
    form.subcate.choices = [(subcate.id, subcate.subcate_name) for subcate in Subcate.query.all()]
    
    if request.method == 'POST':
        #print(form.subcate.data)
        #subcate = Subcate.query.filter_by(belong=form.category.data).all()
    #     select = request.form.get('cat')
        res = Product.query.filter_by(subcate_of=form.subcate.data).all()
        
            

        return render_template('home2.html',form=form, res = res, x=x)
    
        
    return render_template('index.html', x=x, form=form)

@app.route('/subcate/<category>')
def subcate(category):
    subcates = Subcate.query.filter_by(belong=category).all()
    subcateList = []
    for subcate in subcates:
        subObj = {}
        subObj['id'] = subcate.id
        subObj['subcate_name'] = subcate.subcate_name
        subcateList.append(subObj)

    return jsonify({'subcates' : subcateList})

@app.route('/add', methods =['GET', 'POST'])
def add():
    form_cat = Category_form()
    if form_cat.validate_on_submit():
        added = Category(category_name=form_cat.category_name.data,
                        description=form_cat.description.data)
        db.session.add(added)
        db.session.commit()
        db.session.remove()
        return redirect(url_for('index'), x = x)
    
    return render_template('add.html', form=form_cat, x = x) 


@app.route('/delete/<id>', methods =['GET', 'POST'])
def delete(id):
    
    # if delete_for.validate_on_submit():
    #         value = request.form.get('deleted')
    #         cursor.execute(f'DELETE FROM product WHERE id = {value}')
    #         conn.commit()
    
        print(id)
        conn = sqlite3.connect('app2\main\Shop.db', check_same_thread=False)
        cursor=conn.cursor()
        cursor.execute(f'DELETE FROM product WHERE id = {id}')
        conn.commit()
        conn.close()
        # deleted_product = Product.query.filter(Product.id==id).one()
        # print(deleted_product)
        
        # #print(request.form.get('deleted'))
        # db.session.close()
        # db.session.delete(deleted_product)
        # db.session.commit()
            
        return redirect(url_for('index'))
    
    