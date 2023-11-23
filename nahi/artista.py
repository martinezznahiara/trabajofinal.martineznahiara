from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from nahi.db import get_db

bp = Blueprint('artista', __name__, url_prefix="/artista")

@bp.route('/')
def index():
    db = get_db()
    artista = db.execute(
        """SELECT ar.name AS Nombre, count(al.AlbumId) AS Albums
         FROM artists ar JOIN albums al ON ar.ArtistId = al.ArtistId
         GROUP BY Nombre
         ORDER BY Nombre ASC """
    ).fetchall()
    return render_template('artista/index.html', artista=artista)