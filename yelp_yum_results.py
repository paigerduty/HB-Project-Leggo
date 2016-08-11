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

def call_yelp(longitude,latitude):
	auth = authenticate()

	# Binds a Client object giving it authentication credentials
	client = Client(auth)

	# Creates dict params based on Yelp Search parameters
	# How to dynamically get from form submission
	# Give yelp the lat/long and time preference from user form submit
	# Query Yelp for yums based on those preferences
	# Return the yums in a format (callback)?
	params = {
		'sort':2,
		'term':'brunch'
	}

	# Calls Yelp API with parameters specified information
	# ** allows an arbitrary amount of arguments to be passed
	response = client.search_by_coordinates(latitude,longitude,params)
	return response


	# Hold all objects in a list
	# Choose the first
	# Hold the first and get the attributes that the app wants
	# return response

def parse_data(longitude,latitude):
	response = call_yelp(longitude,latitude)
	businesses = response.businesses
	for business in businesses:
		print business.name, business.url, business.location.address



