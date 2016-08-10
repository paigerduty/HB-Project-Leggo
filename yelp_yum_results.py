import os
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator


def call_yelp():

	# Sets up Oauth for Yelp API requests
	auth = Oauth1Authenticator(
		consumer_key = os.environ.get('YELP_CONSUMER_KEY'),
		consumer_secret = os.environ.get('YELP_CONSUMER_SECRET'),
		token = os.environ.get('TOKEN'),
		token_secret = os.environ.get('TOKEN_SECRET')
	)

	# Binds a Client object giving it authentication credentials
	client = Client(auth)

	# Creates dict params based on Yelp Search parameters
	# How to dynamically get from form submission
	params = {
		'term':'food',
		'sort': 2,
		'location':'San Francisco'
	}

	# Calls Yelp API with parameters specified information
	# ** allows an arbitrary amount of arguments to be passed
	response = client.search(**params)

	# Hold all objects in a list
	# Choose the first
	# Hold the first and get the attributes that the app wants

	return response


# Give yelp the lat/long and time preference from user form submit

# Query Yelp for yums based on those preferences

# Return the yums in a format (callback)?