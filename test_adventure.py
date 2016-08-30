from adventure import YumPossibilities, Yum, YayPossibilities
from model import Yay, db, connect_to_db
import unittest
from server import app
import server


class YumPossibilitiesTest(unittest.TestCase):
	""" Testing the YumPossibilities object and methods """
	
	def setUp(self):
		"""Stuff to do before every test."""
		self.client = app.test_client()
		app.config['TESTING'] = True


		self.test_YP = YumPossibilities(37.773972, -122.431297, 'brunch')
		server.call_yelp = self._mock_call_yelp


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


	# def test_YP(self):
	# 	self.assertEqual(self.test_YP.latitude, 37.773972)

	def test_YP_get_access_token(self):
		self.test_YP.get_access_token()
		self.assertTrue(self.test_YP.token)


	def test_YP_get_yums(self):
		self.test_YP.get_yums()
		self.assertTrue(self.test_YP.yum_list)

	def test_YP_get_yum(self):
		yums = self.test_YP.get_yums()
		yum = self.test_YP.get_yum()
		self.assertTrue(yum is not None)

class YayPossibilitiesTest(unittest.TestCase):
	""" Testing the YumPossibilities object and methods """
	# Integration test, get Yay and see yay shows 
	
	def setUp(self):
		"""Stuff to do before every test."""
		self.test_YP = YayPossibilities(37.773972, -122.431297, 'brunch')
		self.client = app.test_client()
		app.config['TESTING'] = True
		connect_to_db(app, "postgresql:///testyays")
		db.create_all()

		Yay('Name 1','Url 1','Location 1')
		Yay('Name 2','Url 2','Location 2')
		Yay('Name 3','Url 3','Location 3')
		# Write a couple YAY objects to put in there
		
	def tearDown(self):
		"""Stuff to do at the end of every test."""
		db.session.close()
		db.drop_all()

	def test_YP_get_yays_with_mock(self):
		"""Query db for all yays."""
		# result = self.client.post("")

	def test_YP_get_yays(self):
		self.test_YP.get_yays()
		self.assertTrue(self.test_YP.yay_list is not None)


	def test_YP_get_yay(self):
		yays = self.test_YP.get_yays()
		yay = self.test_YP.get_yay()
		# is it instance of Yay object???
		self.assertTrue(yay is not None)

class YumYayObjectTest(unittest.TestCase):
	# Tests object attributes
	# def test_YP(self):
	# 	self.assertEqual(self.test_YP.latitude, 37.773972)
	pass
	

class AdventureTest(unittest.TestCase):
	# Tests Adventure
	# call get_adventure and assert
	pass


# TEST SCRAPY SPIDER AND WEB
# TEST CRON JOB




if __name__ == '__main__':

	unittest.main()