from flask import Blueprint,  render_template
from models.book_models import Book
from db import db



book = Blueprint('book', __name__)


@book.route('/books')
def books():
    books = Book.query.all()
    return render_template('books.html', books=books)

@book.route('/book_detail/<int:id>')
def book_detail(id):
    book = Book.query.get(id)
    return render_template('book.html', book=book)
    
