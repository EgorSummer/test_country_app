# -*- coding: utf-8 -*-


import functools

from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for
)

from werkzeug.security import check_password_hash
from . import db as database
from . import constant

bp = Blueprint('auth', __name__, url_prefix=constant.URL_PREFIX_AUTH)

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get(constant.USER_ID)

    if user_id is None:
        g.user = None
    else:
        g.user = database.get_db_connection().execute(
            constant.SELECT_USER_BY_ID, (user_id,)
        ).fetchone()

@bp.route(constant.URL_LOGIN, methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form[constant.USERNAME]
        password = request.form[constant.PASSWORD]
        db = database.get_db_connection()
        error = None
        user = db.execute(
           constant.SELECT_USER_BY_NAME, (username,)
        ).fetchone()

        if user is None:
            error = constant.ERR_INC_USER_NAME_MESS
        elif not check_password_hash(user[constant.PASSWORD], password):
            error = constant.ERR_INC_PASS_MESS

        if error is None:
            session.clear()
            session[constant.USER_ID] = user[constant.ID]
            return redirect(url_for(constant.URL_INDEX))

        flash(error)

    return render_template('auth.html')

@bp.route(constant.URL_LOGOUT)
def logout():
    session.clear()
    return redirect(url_for(constant.URL_INDEX))

