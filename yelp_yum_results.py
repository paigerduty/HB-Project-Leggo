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
	
def call_yelp():
	auth = authenticate()

	# Binds a Client object giving it authentication credentials
	client = Client(auth)

	# Creates dict params based on Yelp Search parameters
	# How to dynamically get from form submission
	# Give yelp the lat/long and time preference from user form submit
	# Query Yelp for yums based on those preferences
	# Return the yums in a format (callback)?
	params = {
		'term':'brunch',
		'sort': 2,
		'location':'San Francisco'
	}

	# Calls Yelp API with parameters specified information
	# ** allows an arbitrary amount of arguments to be passed
	
	response = client.search(**params)
	print response.businesses[0].name
	return response


	# Hold all objects in a list
	# Choose the first
	# Hold the first and get the attributes that the app wants
	# return response

def parse_data():
	response = call_yelp()
	businesses = response.businesses
	for business in businesses:
		print business.name, business.url, business.location.address



