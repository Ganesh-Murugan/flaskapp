from main import app, db
from flask import redirect, render_template, request, url_for
from main.models import Category, Product
from main.forms import Category_form, delete_form



@app.route('/', methods=['GET','POST'])
def index():
    # form=Form()
    # form.category.choices = [(category.id, category.category_name) for category in Category.query.all()]
    global x
    index.x = Category.query.all()
    if request.method == 'POST':
        select = request.form.get('cat')
        res = Product.query.filter_by(category_of=str(select)).all()
        delete_for = delete_form()
        if delete_for.validate_on_submit():
            value = request.form.get('deleted')
            deleted_product= Product.query.filter_by(id=value).first()
            db.session.delete(deleted_product)
            db.session.commit()
            print(deleted_product)
            
            print(request.form.get('deleted'))
            return redirect(url_for('index'))
            

        return render_template('home2.html', res = res , form=delete_for, x=index.x)
    
        
    return render_template('index.html', x=index.x)



@app.route('/add', methods =['GET', 'POST'])
def add():
    form_cat = Category_form()
    if form_cat.validate_on_submit():
        added = Category(category_name=form_cat.category_name.data,
                        description=form_cat.description.data)
        db.session.add(added)
        db.session.commit()
        return redirect(url_for('index'))
    
    return render_template('add.html', form=form_cat, x = index.x) 


