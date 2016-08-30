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

		self.yays = [Yay(name='Name 1',url='Url 1',location='Location 1'),
				Yay(name='Name 2',url='Url 2',location='Location 2'),
				Yay(name='Name 3',url='Url 3',location='Location 3')]

		for yay in self.yays:
			db.session.add(yay)
		db.session.commit()
		
	def tearDown(self):
		"""Stuff to do at the end of every test."""
		db.session.close()
		db.drop_all()

	def test_YP_get_yays_with_mock(self):
		"""Query db for all yays."""
		# result = self.client.post("")
		yay_list = self.test_YP.get_yays()
		print self.yay_list
		"""FIX ME"""
		self.assertTrue(len(yay_list) > 0)

	# def test_YP_get_yay_with_mock(self):
	# 	self.test_YP.yay_list = self.test_YP.get_yays()
	# 	yay = self.test_YP.get_yay()

	# 	# is it instance of Yay object???
	# 	self.assertTrue(type(Yay) is object)

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