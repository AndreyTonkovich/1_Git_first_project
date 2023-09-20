from flask_login import UserMixin
from datetime import datetime
from db import db


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.Unicode(255), nullable=False, unique=True)
    password = db.Column(db.String(300), nullable=False)
    name = db.Column(db.String(100))
    
    date = db.Column(db.DateTime(), default=datetime.utcnow) 
    # Relationships
    roles = db.relationship('Role', secondary='users_roles', backref=db.backref('users', lazy='dynamic')) 


# Define the Role data model
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    # for display purposes
    label = db.Column(db.Unicode(255)) 


# Define the UserRoles association model
class UsersRoles(db.Model):
    __tablename__ = 'users_roles'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey(
        'users.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey(
        'roles.id', ondelete='CASCADE'))    