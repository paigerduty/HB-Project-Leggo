import os

from jinja2 import StrictUndefined
from flask import Flask, render_template, request, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db

app = Flask(__name__)

# Required for Flask sessions and debug toolbar
# Store in environment
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

	time_pref = request.form['time']
	distance_radius = request.form['distance_radius']

	# Store these in the session so I can use to make API call
	session['time_pref'] = time_pref
	session['distance_radius'] = distance_radius

	return redirect('/')

if __name__ == '__main__':
	app.debug = True
	connect_to_db(app)
	DebugToolbarExtension(app)
	app.run(host="0.0.0.0")