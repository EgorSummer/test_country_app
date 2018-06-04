Install

# create application directory:

mkdir test_app

cd test_app

# clone the repository

https://github.com/EgorSummer/test_country_app

#Create a virtualenv and activate it:

python3 -m venv venv

. venv/bin/activate


# install flask

pip install flask


# initialize the database

export FLASK_APP=country_app

flask init-db


#Configure the Secret Key

python -c 'import os; print(os.urandom(16))'


# you get something like this 

b'_5#y2L"F4Q8z\n\xec]/'

# Create the config.py file in the instance folder

# Copy the generated value into it.

# SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'


# run the application

flask run


# you get something like this 
 * Serving Flask app "country_app" (lazy loading)
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 

# visit http://127.0.0.1:5000/auth/login



#there is no registration, but the existing user: admin with password: admin


