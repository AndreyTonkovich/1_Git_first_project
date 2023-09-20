from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models.user_models import Users
from db import db
from flask_login import login_user, logout_user, login_required


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=["POST", "GET"])
def login():
        if request.method == 'POST':
            password = request.form['password']
            remember = True if request.form.get('remember') else False
            user = Users.query.filter(Users.email == request.form['email']).first()
            
            if user and check_password_hash(user.password, password): 
                login_user(user, remember=remember)   
                return redirect(url_for('main.profile'))
            else:
                flash('Please check your login details and try again.')
                return render_template('login.html')  
        else:    
            return render_template('login.html')


@auth.route('/signup', methods=["POST", "GET"])
def signup():
    if request.method == 'POST':
        count = Users.query.filter(Users.email == request.form['email']).count()
        if count == 0:
            
            
            n = Users()
            n.name = request.form['name']
            n.email = request.form['email']
            password = request.form['password']
            n.password = generate_password_hash(password, method='sha256')
            
            try:
                db.session.add(n)
                db.session.commit()
                   
                return redirect(url_for('auth.login'))
            except:
                return render_template('signup.html')
                
        else:
            flash('Email address already exists')
            return render_template('signup.html')      
    else:
        return render_template('signup.html')
    
    
    
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('song.songs'))