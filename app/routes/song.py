from flask import Blueprint, request, redirect, render_template
from models.song_models import Song
from db import db


song = Blueprint('song', __name__)

@song.route('/songs')
def songs():
    songs_list = Song.query.all()
    return render_template('songs.html', songs=songs_list)