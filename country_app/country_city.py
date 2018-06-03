# -*-coding: utf-8 -*-

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from . import db as database
from . import constant

bp = Blueprint('country_city', __name__)

def prepare_data(id):
    db = database.get_db_connection()
    countries = sorted(
        db.execute(constant.SELECT_COUNTRY).fetchall(),
        key=lambda x: x['name']
    )
    if id == 0:
        id = countries[0][constant.ID]
    cities = db.execute(constant.SELECT_CITY_BY_COUNTRY, (id,)).fetchall()
    return (countries, sorted(cities, key=lambda x: x['name']), id)

@bp.route('/<int:id>/')
def index(id):
    countries, cities, g.id = prepare_data(id)
    return render_template(
        'country_city_index.html',
        countries=countries,
        cities=cities
    )

@bp.route('/<int:id>/create', methods=('GET', 'POST'))
def create(id):
    if request.method == 'POST':
        name = request.form[constant.NAME]
        description = request.form[constant.DESCRIPTION]

        error = None

        if not name:
            error = 'Name is required.'

        if error is not None:
            flash(error)
        else:
            db = database.get_db_connection()
            db.execute(constant.INSERT_CITY, (name, description, id))
            db.commit()
            return redirect(url_for('country_city.index', id=id))
    countries, cities, g.id = prepare_data(id)
    return render_template(
        'create.html',
        countries=countries,
        cities=cities
    )

