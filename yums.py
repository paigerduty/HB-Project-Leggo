import os
import urllib
import urllib2
import json


def get_access_token():
	''' Gets access token from Yelp.'''
	# Sets the parameters for POST request
	app_id = os.environ.get("YELP_APP_ID")
	app_secret = os.environ.get("YELP_APP_SECRET")

	query_args = {'grant_type':'client_credentials',
				  'client_id': app_id,
				  'client_secret': app_secret}

	# Encodes query_args dict to application/x-www-form-urlencoded
	encoded_args = urllib.urlencode(query_args)
	url = 'https://api.yelp.com/oauth2/token'

	# Turns respons JSON into a dictionary
	response_dict = json.load(urllib2.urlopen(url,encoded_args))

	token = response_dict['access_token']

	return token


def call_yelp(latitude,longitude,radius,time_pref):
	token = get_access_token()
	
	# Authenticates each API call with request headers
	headers = { }
	headers['Authorization'] = 'Bearer ' + str(token)

	# Creates dict params based on Yelp Search parameters
	params = { }

	# Adds the user defined term to the params dictionary
	params['term'] = time_pref
	params['radius'] = radius

	# Yelp API call 
	location = 'latitude=' + str(latitude) + "," + 'longitude=' + "," + str(longitude)
	data = urllib.urlencode(params)
	url = 'https://api.yelp.com/v3/businesses/search?'+location
	
	# packages up request
	request = urllib2.Request(url,data,headers)

	# sends request and catches respons
	response = urllib2.urlopen(request)

	# extracts response
	response_dict = json.load(response.read())

	print response_dict


	# response = client.search_by_coordinates(longitude,latitude,params)
	# return response

def parse_data(latitude,longitude,radius,time_pref):
	response = call_yelp(latitude,longitude,time_pref)

	businesses = response.businesses

	business_list = []

	for business in businesses:
		business_list.append(business.name)

	print business_list
	return business_list


