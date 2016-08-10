# Importing from Python
import os
import requests

# Importing from pip installed libraries
from rauth import OAuth2Service
from jinja2 import StrictUndefined
from flask import Flask, render_template, request, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db

app = Flask(__name__)

# Required for Flask sessions and debug toolbar
# Stored in secrets.sh
app.secret_key = os.environ.get('FLASK_SECRET_KEY')

# Raises an error in Jinja when an undefined var is used
app.jinja_env.undefined = StrictUndefined

# Sets up a service wrapper to obtain an access token 
# after the authorization URL has been visited by the client

yelp = OAuth2Service(
	client_id = os.environ.get'YELP_CONSUMER_KEY'
	client_secret = os.environ.get'YELP_CONSUMER_SECRET'
	name='yelp'
	authorize_url=''
	token
	token_secret


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

	# Changes distance radius from miles to meters for Yelp API call
	# Limits to 2 decimal points
	 distance_radius_m = float("{0:2f}".format(int(distance_radius) * 1609.34))

	# Store these in the session so I can use to make API call
	session['time_pref'] = time_pref
	session['distance_radius'] = distance_radius
	session['latitude'] = latitude
	session['longitude'] = longitude

	# Return JSON 
	return "Success"

if __name__ == '__main__':
	app.debug = True
	connect_to_db(app)
	DebugToolbarExtension(app)
	app.run(host="0.0.0.0")