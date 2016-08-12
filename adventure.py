"""Randomly picks a yay and a yum from the list of possible ones."""

from random import choice

# Calls function that makes Yelp API call
# Randomly chooses one of possible businesses

def random_yum(yum_list):
	return choice(yum_list)
	

