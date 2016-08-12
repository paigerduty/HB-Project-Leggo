import os
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator


def authenticate():

	# Sets up Oauth for Yelp API requests
	auth = Oauth1Authenticator(
		consumer_key = os.environ.get('YELP_CONSUMER_KEY'),
		consumer_secret = os.environ.get('YELP_CONSUMER_SECRET'),
		token = os.environ.get('TOKEN'),
		token_secret = os.environ.get('TOKEN_SECRET')
	)
	return auth

def call_yelp(longitude,latitude,time_pref):
	auth = authenticate()

	# Binds a Client object giving it authentication credentials
	client = Client(auth)

	# Creates dict params based on Yelp Search parameters
	params = {
		'sort':2,
		'location':'San Francisco'
		}

	# Adds the user defined term to the params dictionary
	params['term'] = time_pref
	# params['cll'] = str(latitude)+","+str(longitude)

	# Calls Yelp API with parameters specified information
	response = client.search_by_coordinates(latitude,longitude,params)
	return response

def parse_data(longitude,latitude,time_pref):
	response = call_yelp(longitude,latitude,time_pref)

	businesses = response.businesses

	print type(businesses[0])

	business_list = []

	for business in businesses:
		business_list.append(business.name)

	print business_list
	return business_list


