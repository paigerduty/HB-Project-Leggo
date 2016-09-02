import os
import requests
import geocoder
from model import Yay, connect_to_db, db, app
from flask import Flask, current_app, jsonify
from random import choice

class YumPossibilities(object):
	'''A list of Yum objects returned from Yelp API call.'''
	yum_list = []

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

		# Pass in address of Yay into payload (add SF)
		# Creates a dictionary based on Yelp Search params
		payload = {}
		payload['term'] = self.time_pref
		payload['longitude'] = self.longitude
		payload['latitude'] = self.latitude
		payload['radius_filter'] = 400

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
		return yum_list

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

		return yay_list

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
		# self.yums = YumPossibilities(latitude, longitude, time_pref)
		self.yays = YayPossibilities(latitude, longitude, time_pref)

	# GET YUMS GET YAYS AS SEPARATE FUNCTIONS
	# THEN GET YUM GET YAY AND HOLD LIST

	def get_adventure(self):
		"""Returns adventure_dict with list of yays and yums"""
		adventure_dict = {}
		yay_list = self.yays.get_yays()

		# GETS LIST OF YUMS AND YAYS THEN POPS OFF

		yays = []
		for item in yay_list:
			yayy = {}
			item.geolocate()
			yayy['name'] = str(item.name)
			yayy['url'] = item.url
			yayy['location'] = item.location
			yayy['latitude'] = item.latitude
			yayy['longitude'] = item.longitude

			yays.append(yayy)

		adventure_dict['yays'] = yays
		first_yay = yays[0]


		self.yums = YumPossibilities(first_yay['latitude'], first_yay['longitude'], self.time_pref)
		yum_list = self.yums.get_yums()

		yums = []
		for item in yum_list:
			yumm = {}
			yumm['name'] = item.name
			yumm['url'] = item.url
			yumm['location'] = str(item.location)

			yums.append(yumm)

		adventure_dict['yums'] = yums

		return adventure_dict


if __name__ == "__main__":
	connect_to_db(app)

