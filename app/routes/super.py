from flask import Blueprint,  render_template, request, redirect
from models.super_models import Grocery
from db import db


super = Blueprint('super', __name__)


@super.route('/supers', methods=['GET'])
def supers():
    groceries = Grocery.query.all()
    return render_template('supers.html', groceries=groceries)

@super.route('/super_add', methods=['GET', 'POST'])
def super_add():
    if request.method == 'POST':
        new_item = Grocery()
        new_item.name = request.form['name']
        new_item.description = request.form['description']
        new_item.weight = request.form['weight']
        new_item.quantity = request.form['quantity']
        new_item.price = request.form['price']
        try:
            db.session.add(new_item)
            db.session.commit()

            return redirect('/supers')
        except:
            return('Ошибка записи') 
    else:      
        return render_template("super_add.html")