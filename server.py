# Importing from Python
import os
import requests
import adventure
import yums

# Importing from pip installed libraries
from jinja2 import StrictUndefined
from flask import Flask, render_template, request, redirect, flash, session
# from flask_debugtoolbar import DebugToolbarExtension

# from model import connect_to_db, db

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

@app.route('/submit-data', methods=['POST'])
def submit_data():
	"""Submits user data and returns an adventure."""

	# Gets all fields of form data
	time_pref = request.form['time']
	radius = request.form['radius']
	latitude = request.form['latitude']
	longitude = request.form['longitude']

	# Returns a business list from Yelp API call
	yum_list = yums.parse_data(latitude,longitude,time_pref)

	# Returns a business name
	# yum = adventure.random_yum(yum_list)

	# Changes distance radius from miles to meters for Yelp API call
	radius_m = int(radius) * 1609.34


	# Return JSON 
	return render_template('lolz.html',yum_list=yum_list)


if __name__ == '__main__':
	app.debug = True
	# connect_to_db(app)
	# DebugToolbarExtension(app)
	app.run(host="0.0.0.0",port=5000)