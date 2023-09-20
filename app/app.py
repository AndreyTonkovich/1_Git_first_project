from flask import Flask
from flask_login import LoginManager
from flask import jsonify


from cli import command
from routes.post import post
from routes.auth import auth
from routes.main import main
from routes.song import song
from routes.book import book
from routes.item import item
from routes.super import super
from routes.clinic import clinic


from db import db

from models.user_models import Users



app = Flask(__name__)


app.config['FLASK_ENV'] = 'development'
app.config.from_pyfile("config.py")
app.config['JSON_AS_ASCII'] = False
db.init_app(app)


login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


app.register_blueprint(command)
app.register_blueprint(post)
app.register_blueprint(auth)
app.register_blueprint(main)
app.register_blueprint(song)
app.register_blueprint(book)
app.register_blueprint(item)
app.register_blueprint(super)
app.register_blueprint(clinic)


@app.route('/json')
def json():
    users = Users.query.all()
    
    user = []
    
    for u in users:
      user.append("id")
      user.append(u.id)
      user.append("email")
      user.append(u.email)
      user.append("name")
      user.append(u.name)

    return jsonify(user)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")