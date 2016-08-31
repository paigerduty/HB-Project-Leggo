# Importing from Python
import os
import requests
import adventure
import json
from model import connect_to_db, db, app,Yay

# Importing from pip installed libraries
from jinja2 import StrictUndefined
from flask import Flask, render_template, jsonify, request, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension

# from model import connect_to_db, db

app = Flask(__name__)

# Required for Flask sessions and debug toolbar
# Stored in secrets.sh
app.secret_key = os.environ.get('FLASK_SECRET_KEY')

# Raises an error in Jinja when an undefined var is used
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

@app.route('/')
def index():
	"""First page."""
	return render_template('index.html')

@app.route('/submit-data', methods=['POST'])
def submit_data():
	"""Submits user data and returns an adventure."""
	# Gets all fields of form data
	time_pref = request.form.get('time_pref')
	latitude = request.form.get('latitude')
	longitude = request.form.get('longitude')

	adv = adventure.Adventure(latitude, longitude, time_pref)

	adventah = adv.get_adventure()
	adv_json = json.dumps(adventah)

	print "Im in route now...... adventah"

	# yum_list_json = jsonify(yum_list)

	session['adventure'] = adv_json

	print "********************\n\n\n"
	print "\n\n This is the adventah added to the session\n\n"
	print adventah
	print "********************\n\n\n"

	return adv_json

@app.route('/swap-yay')
def swap_yay():
	yay_list = session['yay_list']

	print "********************\n\n\n"
	print yay_list
	print "********************\n\n\n"


	# yay_list = json.loads(yay_list)
	# UNJSONIFY ADVENTURE
	# GRAB YAY LIST
	# POP OFF YAY
	# RETURN

	# print "********************\n\n\n"
	# print yay_list
	# print "********************\n\n\n"
	
	return yay_list

# Access yum and yay lists from session
# call method to pop a new one 

if __name__ == '__main__':
	app.debug = True
	connect_to_db(app)
	DebugToolbarExtension(app)
	app.run(host="0.0.0.0",port=5000)