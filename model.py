"""Classes for database only"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
DB_URI = "postgresql:///yays"

#Connects to PostgreSQL database via Flask-SQLAlchemy helper library
db = SQLAlchemy()

####################################################################
# Model definitions

# db.Model is a base class for all Models for SQLAlchemy

class Adventure(object):
	'''Defines an adventure'''
	# Contains 2 Possibilities (1 named Yum and 1 named Yay) 
	pass



class Yay(db.Model):
	''' Defines a Yay.'''
	# Objects created from either a db query or a Yelp API call
	__tablename__ = "yays"

	# yay_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(75), primary_key=True,nullable=False)
	url = db.Column(db.String(300), nullable=False)
	location = db.Column(db.String(100), nullable=False)

	def __init__(self, name, url, location):
		self.name = name
		self.url = url
		self.location = location

	def __repr__(self):
		return '<Yay %r>' % self.name

# class Yum(object):
# 	''' A Yum created after the Yelp API call.'''

# 	def __init__(self, name, url, coordinates):
# 		self.name = name
# 		self.url = url
# 		self.location = coordinates

# 	def __repr__(self):
# 		return '<Yum %s' % self.name

####################################################################
# Helper functions

def connect_to_db(app):
	"""Connect the database to Flask app."""

	#Configure to use PostgreSQL database
	app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///yays'
	app.config['SQLALCHEMY_ECHO'] = True
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
	db.app = app
	db.init_app(app)

if __name__ == "__main__":
	connect_to_db(app)
	print "Connected to DB"

	db.create_all()
