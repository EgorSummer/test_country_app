import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext
from werkzeug.security import generate_password_hash
from . import constant


def get_db_connection():
    if constant.DB not in g:
        g.db = sqlite3.connect(
        current_app.config[constant.DATABASE],
        detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db_connection(e=None):
    db = g.pop(constant.DB, None)
    if db is not None:
        db.close()

def init_db():
    db = get_db_connection()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
    # add default user admin
    db.execute(constant.INSERT_USER,
               (constant.ADMIN, generate_password_hash(constant.ADMIN))
    )
    db.commit()


@click.command(constant.INIT_DB_COMMAND)
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables with new default data."""
    init_db()
    click.echo(constant.INIT_DB_MESS)

def init_app(app):
    app.teardown_appcontext(close_db_connection)
    app.cli.add_command(init_db_command)

