"""Randomly picks a yay and a yum from the list of possible ones."""

from random import choice

# Calls function that makes Yelp API call to get Yum
# Randomly chooses one of possible businesses, holds onto the possibilities
def random_yum(business_list):
	return choice(business_list)

# Call the function that queries the db for a Yay
# Randomly chooses one 

# Returns 1 yum and 1 yay