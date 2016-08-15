import os
import requests


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
	# params['radius'] = radius
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

	yum_list = []

	for yum in yum_possibilities:
		# Find way to pass in name and url from dictionary
		x = Option()
		yum_list.append(x)

	print yum_list
	return yum_list

