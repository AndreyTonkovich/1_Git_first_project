from flask import Blueprint, request, redirect, render_template
from models.post_models import Posts
from db import db


post = Blueprint('post', __name__)


@post.route("/post_add", methods=["POST", "GET"])
def post_add():
    if request.method == 'POST': 
        n = Posts()
        n.title = request.form['title']
        n.intro = request.form['intro']
        n.text = request.form['text']
        try:
            db.session.add(n)
            db.session.commit()
            
            return redirect('/posts')
            
        except:
            return('Ошибка записи') 
    else:      
        return render_template("post_add.html")
    

@post.route("/posts")
def posts():
    n = Posts.query.order_by(Posts.date.desc()).all()
    return render_template("posts.html", n=n)


@post.route("/posts/<int:id>")
def post_datail(id):
    n = Posts.query.get(id)
    return render_template("post_datail.html", n=n)

    
@post.route("/posts/<int:id>/del")
def post_delete(id):
    n = Posts.query.get_or_404(id)

    try:
        db.session.delete(n)
        db.session.commit()
        return redirect('/posts')
    except:
        return "При удалении статьи произошла ошибка"


@post.route("/posts/<int:id>/update", methods=["POST", "GET"]) 
def post_update(id):
    n = Posts.query.get(id)
    if request.method == 'POST': 
        n.title = request.form['title']
        n.intro = request.form['intro']
        n.text = request.form['text']
        try:
            db.session.commit()
            return redirect('/posts') 
        except:
            return "При редактировании статьи произошла ошибка"
         
    else:    
        return render_template("post_update.html", n=n)    