# -*- coding: utf-8 -*-

DB = 'db'
DATABASE = 'DATABASE'
USERNAME = 'username'
PASSWORD = 'password'
USER_ID = 'user_id'
ID = 'id'
ADMIN = 'admin'
NAME = 'name'
DESCRIPTION = 'description'
COUNTRY_ID = 'country_id'

INIT_DB_MESS = 'Initialised the database.'
INIT_DB_COMMAND = 'init-db'

SELECT_USER_BY_NAME = 'SELECT * FROM user WHERE username = ?'
SELECT_USER_BY_ID = 'SELECT * FROM user WHERE id = ?'
SELECT_COUNTRY = 'SELECT * FROM country'
SELECT_CITY_BY_COUNTRY = 'SELECT * FROM city WHERE country_id = ?'
INSERT_USER = 'INSERT INTO user (username, password) VALUES (?, ?)'
INSERT_CITY = (
    'INSERT INTO city (name, description, country_id) VALUES (?, ?, ?)'
)

URL_PREFIX_AUTH = '/auth'
URL_LOGIN = '/login'
URL_LOGOUT = '/logout'
URL_INDEX = 'index'

ERR_INC_USER_NAME_MESS = 'Incorrect username.'
ERR_INC_PASS_MESS = 'Incorrect password.'


