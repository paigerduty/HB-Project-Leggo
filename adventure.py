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
		self.yums = YumPossibilities(latitude, longitude, time_pref)
		self.yays = YayPossibilities(latitude, longitude, time_pref)

	# GET YUMS GET YAYS AS SEPARATE FUNCTIONS
	# THEN GET YUM GET YAY AND HOLD LIST

	def get_adventure(self):
		"""Returns adventure_dict with list of yays and yums"""
		adventure_dict = {}
		yum_list = self.yums.get_yums()
		yay_list = self.yays.get_yays()

		yums = []
		for item in yum_list:
			yumm = {}
			yumm['name'] = item.name
			yumm['url'] = item.url
			yumm['location'] = str(item.location)

			yums.append(yumm)

		# GETS LIST OF YUMS AND YAYS THEN POPS OFF

		yays = []
		for item in yay_list:
			yayy = {}
			yayy['name'] = item.name
			yayy['url'] = item.url
			yayy['location'] = item.location

			yays.append(yayy)

		print "***********\n\n"
		print yums
		print "***********\n\n"
		print yays
		print "\n\n************\n\n"

		# for yay in yay_list:
		# 	yayy = {}
		# 	yayy['name'] = yay.name
		# 	yayy['url'] = yay.url
		# 	yayy['location'] = yay.location

		# 	yay_dict['yay'] = yayy

		# adventure_dict['yums'] = yum_dict
		adventure_dict['yays'] = yays
		adventure_dict['yums'] = yums

		return adventure_dict

	def swap_yay(self):
		new_yay = session['yay_list'].pop()

		yay_dict = {}
		yay_dict['name'] = (new_yay.name)
		yay_dict['url'] = (new_yay.url)
		yay_dict['location'] = (new_yay.location)

		return yay_dict

	# def swap_yum(self):
	# 	new_yum = self.yum_list.pop()
				
	# 	yum_dict = {}
	# 	yum_dict['name'] = (new_yum.name)
	# 	yum_dict['url'] = (new_yum.url)
	# 	yum_dict['location'] = str(new_yum.location)

	# 	return yum_dict

if __name__ == "__main__":
	connect_to_db(app)

