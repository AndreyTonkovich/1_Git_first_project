from flask import Blueprint, render_template
from flask_login import login_required, current_user
from models.user_models import Users

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/about')
def about():
    return render_template('about.html')


@main.route('/profile')
@login_required
def profile():
    n = Users.query.order_by(Users.date.desc()).all()
    return render_template('profile.html', name=current_user.name, n=n)