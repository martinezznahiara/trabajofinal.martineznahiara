from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from nahi.db import get_db

bp = Blueprint('album', __name__)

@bp.route('/album')
def index():
    db = get_db()
    albums = db.execute(
        """SELECT title  AS titulo, ar.name AS Artista, sum(Milliseconds) AS Duracion
         FROM albums a 
         JOIN artists ar ON ar.ArtistId = a.ArtistId
         JOIN tracks t ON t.AlbumId = a.AlbumId
         GROUP BY a.albumId
         ORDER BY Artista ASC """
    ).fetchall()
    return render_template('album/index.html', albums=albums)

@bp.route('/album/<int:id>')
def detalle(id):
    db = get_db()
    album = db.execute(
        """SELECT title  AS titulo, ar.name AS Artista, sum(Milliseconds) AS Duracion
         FROM albums a 
         JOIN artists ar ON ar.ArtistId = a.ArtistId
         JOIN tracks t ON t.AlbumId = a.AlbumId
         WHERE a.albumId = ?
         GROUP BY a.albumId
         """, (id,)
    ).fetchone()
    return render_template('album/detalle.html', album=album)
