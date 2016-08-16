"""Randomly picks a yay and a yum from the list of possible ones."""

from random import choice
import yums

# Calls function that makes Yelp API call to get Yum

yum_list = yums.parse_data(latitude,longitude,time_pref)
# Randomly chooses one of possible businesses, holds onto the possibilities
def random_yum(yum_list):
	return choice(yum_list)

# Call the function that queries the db for a Yay
# Randomly chooses one 

# Returns 1 yum and 1 yay