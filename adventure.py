import os
import requests
from model import Yay, connect_to_db, db, app
from flask import Flask, current_app, jsonify
from random import choice

class YumPossibilities(object):
	'''A list of Yum objects returned from Yelp API call.'''
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
		'''Calls Yelp API using user submitted parameters'''
		# Gets access token
		self.get_access_token()

		# Authenticates each API call with request headers
		headers = {}
		headers['Authorization'] = 'Bearer ' + str(self.token)

		# Creates a dictionary based on Yelp Search params
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
			yum = self.yum_list.pop()
			return yum

class Yum(object):
	def __init__(self, name, url, location):
		self.name = name
		self.url = url
		self.location = location

	def __repr__(self):
		return '<Yum %s>' % self.name


class YayPossibilities(object):
	yay_list = []

	def __init__(self, latitude,longitude,time_pref):
		self.latitude = latitude
		self.longitude = longitude
		self.time_pref = time_pref

	def get_yays(self):
		yay_list = Yay.query.all()
		self.yay_list = yay_list

	def get_yay(self):
			if not self.yay_list:
				raise AttributeError("Must scrape & seed db before calling get_yay.")
			else:
				self.get_yays()
				yay = self.yay_list.pop()
				return yay


class Adventure(object):
	''' An object with YumPossibilities and YayPossibilities objects and methods 
	    to return a random one and dictionaryfy it.'''

	def __init__(self, latitude, longitude, time_pref):
		self.latitude = latitude
		self.longitude = longitude
		self.time_pref = time_pref
		self.yums = YumPossibilities(latitude, longitude, time_pref)
		self.yays = YayPossibilities(latitude, longitude, time_pref)

	def get_the_yum(self):
		yum_list = self.yums.get_yums()
		randoyum = self.yums.get_yum()
		return randoyum

	def get_the_yay(self):
		yay_list = self.yays.get_yays()
		randoyay = self.yays.get_yay()
		return randoyay

	# def dictionaryfy_objects(randoyay,randoyum):
	def dictionaryfy_objects(self):
		adventure_dict = {}
		
		randoyum = self.get_the_yum()
		randoyay = self.get_the_yay()


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

