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

	adv_json = adv.get_adventure()
	adv_json = json.dumps(adv_json)

	# # Create vars to hold lists of yums and yays
	# # add to session
	# yum_list = adv.yums.yum_list
	# yay_list = adv.yays.yay_list

	session['adventure'] = adv_json

	return adv_json

@app.route('/swap-yay')
def swap_yay():
	yay_list = session.get['yay_list']
	yay = yay_list.pop()
	
	# yay_dict = {}
	# yay_dict['name'] = yay.name
	# yay_dict['url'] = yay.url
	# yay_dict['location'] = yay.location

	return yay

# Access yum and yay lists from session
# call method to pop a new one 

if __name__ == '__main__':
	app.debug = True
	connect_to_db(app)
	DebugToolbarExtension(app)
	app.run(host="0.0.0.0",port=5000)