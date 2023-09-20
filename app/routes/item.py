from flask import Blueprint,  render_template
from models.item_models import Category, Item, Manufacturer
from db import db


item = Blueprint('item', __name__)




@item.route('/items')
def items():
    manufacturers = Manufacturer.query.all()
    return render_template('index.html', manufacturers=manufacturers)

@item.route('/<manufacturer>/categories')
def show_categories(manufacturer):
    manufacturer = Manufacturer.query.filter_by(name=manufacturer).first()
    items = manufacturer.items
    categories = set(item.category for item in items)
    return render_template('categories.html', manufacturer=manufacturer, categories=categories)

@item.route('/<manufacturer>/<category>')
def show_items(manufacturer, category):
    items = Item.query.join(Item.manufacturers).join(Item.category).\
                filter(Manufacturer.name == manufacturer).\
                filter(Category.name == category).all()
    return render_template('items.html', manufacturer=manufacturer, category=category, items=items)