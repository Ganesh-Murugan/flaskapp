from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField


class View(FlaskForm):
    category = SelectField('category', choices=[])
    subcate = SelectField('subcate', choices=[])

class Category_form(FlaskForm):
    category_name = StringField(label='Category Name')
    description = StringField(label='Description')
    Submit = SubmitField(label='Submit')


class delete_form(FlaskForm):
    Submit = SubmitField(label='Delete')