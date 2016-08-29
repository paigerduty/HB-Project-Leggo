from adventure import YumPossibilities, Yum 	
import unittest


class YumPossibilitiesTest(unittest.TestCase):
	""" Testing the YumPossibilities object and methods """
	
	def setUp(self):
		"""Stuff to do before every test."""
		test_YP = YumPossibilities(37.773972, -122.431297, 'brunch')

		def _mock_call_yelp(self):

			return """[
			         <Yum Sweet Maple>, <Yum Straw>, <Yum Zazie>, 
			         <Yum Mission Beach Cafe>, <Yay Kitchen Story>, 
			         <Yay Brenda's French Soul Food>, <Yay farm:table>, <Yay Dottie's True Blue Cafe>, 
			         <Yay Chow>, <Yay Bacon Bacon>, <Yay Red Door Cafe>, 
			         <Yay Mission Public>, <Yay Brenda's Meat & Three>, <Yay Black Sands>, <
			         Yay b. Patisserie>, <Yay Mymy>, <Yay Bistro Central Parc>, 
			         <Yay 1428 HAIGHT Patio Cafe & Crepery>, <Yay Griddle Fresh>, <Yay Rusty's Southern>
			         ]"""

			server.call_yelp = _mock_call_yelp

	def test_YP(self):
		test_YP = YumPossibilities(37.773972, -122.431297, 'brunch')
		self.assertEqual(test_YP.latitude, 37.773972)

	def test_YP_get_access_token(self):
		test_YP = YumPossibilities(37.773972, -122.431297, 'brunch')
		test_YP.get_access_token()
		self.assertTrue(test_YP.token)


	def test_YP_get_yums(self):
		test_YP = YumPossibilities(37.773972, -122.431297, 'brunch')
		test_YP.get_yums()
		self.assertTrue(test_YP.yum_list)
		# Define mock call to yelp using access token



	def test_YP_get_yum(self):
		test_YP = YumPossibilities(37.773972, -122.431297, 'brunch')
		yums = test_YP.get_yums()
		yum = test_YP.get_yum()
		self.assertTrue(yum is not None)

class YayPossibilitiesTest():
	pass

# TEST SCRAPY SPIDER AND WEB
# TEST CRON JOB


# Create Class Test
# Define test functions within
# assertEqual True, False
# Incorporate setUp and tearDown

if __name__ == '__main__':

	unittest.main()