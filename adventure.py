import os
import requests
from model import Yay, connect_to_db, db, app
# from server import app
from flask import Flask, current_app, jsonify
from random import choice

''' Helper functions and classes'''

"""Makes Yelp API call to get Yums
   Queries db to get Yays
   Randomly picks a Yum & Yay"""

class YumPossibilities(object):
	'''Defines a possibility. Should be named either Yum or Yay'''
	yum_list = []
# STORE THIS OBJECT 
# PASS JAVASCRIPT AND TOGGLE HIDE/SHOW
# METHOD THAT MAKES REP OF CLASS FOR JS. JSONIFY DICT

	def __init__(self, latitude,longitude,time_pref):
		self.latitude = latitude
		self.longitude = longitude
		self.time_pref = time_pref

	def get_access_token(self):
		'''Gets access token from Yelp needed to make API call'''
		app_id = os.environ.get("YELP_APP_ID")
		app_secret = os.environ.get("YELP_APP_SECRET")

		payload = {'grant_type':'client_credentials',
					'client_id': app_id,
					'client_secret': app_secret}
		r = requests.post('https://api.yelp.com/oauth2/token', params=payload).json()
		token = r['access_token']

		self.token = token 

	def call_yelp(self):
		# Gets access token
		self.get_access_token()

		# Authenticates each API call with request headers
		headers = {}
		headers['Authorization'] = 'Bearer ' + str(self.token)

		# Creates a dictionary based on Yelp Search params
		# adds form data
		payload = {}
		payload['term'] = self.time_pref
		payload['longitude'] = self.longitude
		payload['latitude'] = self.latitude

		# Yelp API call
		url = 'https://api.yelp.com/v3/businesses/search?'
		response = requests.get(url,headers=headers,params=payload)
		self.response = response

	def get_yums(self):
		'''Calls Yelp API, returns a list of Yum objects'''
		self.call_yelp()
		businesses = self.response.json()['businesses']
		
		yum_list = []

		for business in businesses:
			name = business['name']
			url = business['url']
			location = business['coordinates']
			yum = Yum(name, url, location)
			
			yum_list.append(yum)
		
		self.yum_list = yum_list

	def get_yum(self):
		if not self.yum_list:
			raise AttributeError("Must call get_yums before get_yum")
		else:
			self.get_yums()
			# Need to convert to JSON for AJAX call
			yum = self.yum_list.pop()
			print yum
			return yum

	# function - get new
	# function - get current
	# made up of list of options

class Yum(object):
	def __init__(self, name, url, location):
		self.name = name
		self.url = url
		self.location = location

	def __repr__(self):
		return '<Yay %s>' % self.name

def get_yay():
	yay_list = Yay.query.all()
	yay = choice(yay_list)
	print yay	
	return yay

def dictionaryfy_objects(randoyay,randoyum):
	adventure_dict = {}
	
	yay_dict = {}
	yay_dict['name'] = randoyay.name
	yay_dict['url'] = randoyay.url
	yay_dict['location'] = randoyay.location

	yum_dict = {}
	yum_dict['name'] = randoyum.name
	yum_dict['url'] = randoyum.url
	yum_dict['location'] = randoyum.location

	adventure_dict['yum'] = yum_dict
	adventure_dict['yay'] = yay_dict

	return adventure_dict



if __name__ == "__main__":
	connect_to_db(app)

