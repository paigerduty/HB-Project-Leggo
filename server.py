# Importing from Python
import os
import requests

# Importing from pip installed libraries
from jinja2 import StrictUndefined
from flask import Flask, render_template, request, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
from model import connect_to_db, db


app = Flask(__name__)

# Required for Flask sessions and debug toolbar
# Stored in secrets.sh
app.secret_key = os.environ.get('FLASK_SECRET_KEY')

# Raises an error in Jinja when an undefined var is used
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def index():
	"""First page."""

	return render_template('index.html')

@app.route('/submit-data')
def submit_data():
	"""Submits user data and returns an adventure."""

	# Gets all fields of form data
	time_pref = request.form['time']
	distance_radius = request.form['distance_radius']
	latitude = request.form['latitude']
	longitude = request.form['longitude']

	# Need to create a geographical bounding box to give to Yelp 
	# This will be based on the starting point +/- the given radius 
	# in all directions ne, nw, se, sw

	# Changes distance radius from miles to meters for Yelp API call
	distance_radius_m = int(distance_radius) * 1609.34

	# Creates a bounding box (4 coordinates ne, nw, se, sw)


	# Return JSON 
	return "Success"

@app.route('/yelp_call')
def call_yelp():

	# Sets up Oauth for Yelp API requests
	auth = Oauth1Authenticator(
		consumer_key = os.environ.get('YELP_CONSUMER_KEY'),
		consumer_secret = os.environ.get('YELP_CONSUMER_SECRET'),
		token = os.environ.get('TOKEN'),
		token_secret = os.environ.get('TOKEN_SECRET')
	)

	# Binds a Client object giving it authentication credentials
	client = Client(auth)

	# Creates dict params based on Yelp Search parameters
	params = {
		'term':'food',
		'sort': 2,
		'location':'San Francisco'
	}

	# Calls Yelp API with parameters specified information
	# ** allows an arbitrary amount of arguments to be passed
	response = client.search(**params)

if __name__ == '__main__':
	app.debug = True
	connect_to_db(app)
	DebugToolbarExtension(app)
	app.run(host="0.0.0.0")