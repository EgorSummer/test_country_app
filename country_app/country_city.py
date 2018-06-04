# -*-coding: utf-8 -*-

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from country_app.auth import login_required
from . import db as database
from . import constant

bp = Blueprint('country_city', __name__)

def prepare_data(id_country):
    db = database.get_db_connection()
    countries = sorted(
        db.execute(constant.SELECT_COUNTRY).fetchall(),
        key=lambda x: x[constant.NAME]
    )
    if id_country == 0:
        id_country = countries[0][constant.ID]
    get_record(id_country, constant.COUNTRY)
    cities = db.execute(constant.SELECT_CITY_BY_COUNTRY,
                        (id_country,)).fetchall()
    return (countries, sorted(cities,
                              key=lambda x: x[constant.NAME]), id_country)

def get_record(rec_id, table_name):
    record = database.get_db_connection().execute(
        constant.SELECT_RECORD.format(table_name), (rec_id,)
    ).fetchone()
    if record is None:
        abort(404, constant.ERR_RECORD_NOT_EXIST.format(table_name, rec_id))
    return record

@bp.route('/<int:id_country>')
def index(id_country):
    countries, cities, g.active_country_id = prepare_data(id_country)
    return render_template(
        'country_city_base.html',
        countries=countries,
        cities=cities
    )

@bp.route('/<int:id_country>/create', methods=('GET', 'POST'))
@login_required
def create(id_country):
    get_record(id_country, constant.COUNTRY)
    if request.method == 'POST':
        name = request.form[constant.NAME]
        description = request.form[constant.DESCRIPTION]

        error = None

        if not name:
            error = constant.ERR_NAME_IS_REQUIRED

        if error is not None:
            flash(error)
        else:
            db = database.get_db_connection()
            db.execute(constant.INSERT_CITY, (name, description, id_country))
            db.commit()
            return redirect(url_for('country_city.index',
                                    id_country=id_country))
    countries, cities, g.active_country_id = prepare_data(id_country)
    return render_template(
        'create.html',
        countries=countries,
        cities=cities

    )

@bp.route('/<int:id_country>/<int:id_city>/update', methods=('GET', 'POST'))
@login_required
def update(id_country, id_city):
    city = get_record(id_city, constant.CITY)
    get_record(id_country, constant.COUNTRY)
    if request.method == 'POST':
        name = request.form[constant.NAME]
        description = request.form[constant.DESCRIPTION]
        error = None

        if not name:
            error = constant.ERR_NAME_IS_REQUIRED

        if error is not None:
            flash(error)
        else:
            db = database.get_db_connection()
            db.execute(constant.UPDATE_CITY,
                (name, description, id_country, id_city)
                       )
            db.commit()
            return redirect(url_for('country_city.index',
                                    id_country=id_country))
    countries, cities, g.active_country_id = prepare_data(id_country)
    return render_template(
        'update.html',
        city_update=city,
        countries=countries,
        cities=cities
    )

@bp.route('/<int:id_country>/<int:id_city>/delete', methods=('GET', 'POST'))
@login_required
def delete(id_country, id_city):
    get_record(id_city, constant.CITY)
    get_record(id_country, constant.COUNTRY)
    db = database.get_db_connection()
    db.execute(constant.DELETE_CITY, (id_city,))
    db.commit()
    return redirect(url_for('country_city.index', id_country=id_country))

