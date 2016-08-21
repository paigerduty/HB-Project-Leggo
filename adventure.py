import os
import requests
from flask import jsonify
from random import choice
from model import Yay, connect_to_db, db

"""Makes Yelp API call to get Yums
   Queries db to get Yays
   Randomly picks a Yum & Yay"""


# Calls function that makes Yelp API call to get Yum

def get_access_token():
	''' Gets access token from Yelp.'''
	# Sets the parameters for POST request
	app_id = os.environ.get("YELP_APP_ID")
	app_secret = os.environ.get("YELP_APP_SECRET")

	payload = {'grant_type':'client_credentials',
				  'client_id': app_id,
				  'client_secret': app_secret}

	r = requests.post('https://api.yelp.com/oauth2/token', params=payload).json()

	token = r['access_token']
	return token


def call_yelp(latitude,longitude,time_pref):
	token = get_access_token()
	
	# Authenticates each API call with request headers
	headers = { }
	headers['Authorization'] = 'Bearer ' + str(token)

	# Creates dict params based on Yelp Search parameters
	payload = { }

	# Adds the user defined term to the params dictionary
	payload['term'] = time_pref
	payload['longitude'] = longitude
	payload['latitude'] = latitude

	# Yelp API call 
	url = 'https://api.yelp.com/v3/businesses/search?'
	response = requests.get(url, headers=headers, params=payload)
	return response

def parse_data(latitude,longitude,time_pref):
	''' Calls Yelp API, dictionary-fies the response, instantiates Yum objects.'''
	response = call_yelp(latitude,longitude,time_pref)

	yum_possibilities = response.json()

	businesses = yum_possibilities['businesses']
	
	yum_list = []

	for business in businesses:
		bus_dict = {}
		bus_dict['name'] = business['name']
		bus_dict['url'] = business['url']
		bus_dict['coordinates'] = business['coordinates']

		yum_list.append(bus_dict)

	return yum_list

# Call the function that queries the db for a Yay

def get_yay():
	yay = Yay.query.one()
	return yay

# Randomly chooses one 

# Returns 1 yum and 1 yay


def random_yum(yum_list):
	# Need to convert to JSON for AJAX call
	 yum = choice(yum_list)
	 return yum


if __name__ == "__main__":
	connect_to_db(app)

