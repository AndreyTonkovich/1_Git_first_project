import click
import csv
from flask import Blueprint
from models.song_models import Artist, Album, Song
from models.book_models import Book
from models.item_models import Category, Item, Manufacturer
import json


from db import db

command = Blueprint('command', __name__)


@command.cli.command("create_db")
@click.option('-name', default="Noname")
def create_db(name):
    print("creating db %s " % name)
    db.drop_all() 
    db.create_all()
    db.session.commit()


@command.cli.command("create_tab")
@click.option('-name', default="Noname")
def create_tab(name):
    print("creating tab %s " % name)
     
    db.create_all()
    db.session.commit() 


@command.cli.command("create_book")
@click.option('-name', default="Noname")
def create_book(name):
    print("creating tab %s " % name)
     
    db.create_all()
    db.session.commit()

    with open('books.json', encoding='utf-8') as f:
        books_data = json.load(f)

    for book_data in books_data:
        book = Book(title=book_data['название'], author=book_data['автор'], year=book_data['год публикации'], description=book_data['описание'])
        db.session.add(book)

    db.session.commit() 
   


@command.cli.command("create_song")
@click.option('-name', default="Noname")
def create_song(name):
    print("creating song %s " % name)
    
    db.create_all()
    db.session.commit() 


    # создаем тестовых исполнителей
    artist1 = Artist(name='The Rolling Stones')
    artist2 = Artist(name='Jefferson Airplane')
    artist3 = Artist(name='Nine Inch Nails')
    artist4 = Artist(name='Tool')
    db.session.add_all([artist1, artist2, artist3, artist4])
    db.session.commit()    

    # создаем тестовые альбомы
    album1 = Album(title='Aftermath', year='1966', artist=artist1)
    album2 = Album(title='Beggars Banquet', year='1968', artist=artist1)
    album3 = Album(title='Surrealistic Pillow', year='1967', artist=artist2)
    album4 = Album(title='Broken', year='1992', artist=artist3)
    album5 = Album(title='The Fragile', year='1999', artist=artist3)
    album6 = Album(title='Lateralus', year='2001', artist=artist4) 
    album7 = Album(title='AEnima', year='1996', artist=artist4) 
    album8 = Album(title='10,000 Days', year='2006', artist=artist4) 

        # создаем тестовые песни
    song1 = Song(title='Paint it Black', length='4:20', track_number=1, album=album1)
    song2 = Song(title='Sympathy For The Devil', length='3:53', track_number=2, album=album1)
    song3 = Song(title='White Rabbit', length='3:42', track_number=5, album=album3)
    song4 = Song(title='Wish', length='3:46', track_number=6, album=album4)
    song5 = Song(title='Starfuckers, Inc.', length='5:00', track_number=1, album=album5)
    song6 = Song(title='Schism', length='6:46', track_number=7, album=album6)
    song7 = Song(title='Eulogy', length='8:29', track_number=3, album=album7)
    song8 = Song(title='Vicarious', length='7:07', track_number=5, album=album8)
    db.session.add_all([album1, album2, album3, album4, album5, album6, album7, album8, song1, song2, song3, song4, song5, song6, song7, song8])
    db.session.commit() 


@command.cli.command("create_item")
@click.option('-name', default="Noname")
def create_item(name):
    print("creating tab %s " % name)
     
    db.create_all()
    db.session.commit()

    with open('info.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        rows = list(reader)

    # lowercase column names and replace spaces with underscores
    for row in rows:
        row['name'] = row.pop('Name')
        row['description'] = row.pop('Description')
        row['price'] = float(row.pop('Price').replace(',', '.'))
        row['quantity'] = int(row.pop('Quantity'))
        row['category'] = row.pop('Category')
        row['manufacturer'] = row.pop('Manufacturer')

    # create database
    
    db.create_all()

        # add categories to database
    categories = set(row['category'] for row in rows)
    for name in categories:
        category = Category(name=name)
        db.session.add(category)

        # add manufacturers to database
    manufacturers = set(row['manufacturer'] for row in rows)
    for name in manufacturers:
        manufacturer = Manufacturer(name=name)
        db.session.add(manufacturer)

        # add items to database
    for row in rows:
        item = Item(name=row['name'], description=row['description'], price=row['price'], quantity=row['quantity'])
            # set category relationship
        category_name = row['category']
        category = Category.query.filter_by(name=category_name).first()
        item.category = category
            # set manufacturer relationship
        manufacturer_name = row['manufacturer']
        manufacturer = Manufacturer.query.filter_by(name=manufacturer_name).first()
        item.manufacturers.append(manufacturer)
        db.session.add(item)

        db.session.commit()  


@command.cli.command("create_super")
@click.option('-name', default="Noname")
def create_super(name):
    print("creating super %s " % name)
    
    db.create_all()


@command.cli.command("create_clinic")
@click.option('-name', default="Noname")
def create_clinic(name):
    print("creating clinic %s " % name)
    
    db.create_all()    
    


@command.cli.command("say_my_name")
@click.option('-name', default="Noname")
def say_my_name(name):
    print("say_my_name %s " % name)      