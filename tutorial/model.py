"""Model & database function for Sprint 1 - Leggo."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import settings

from sqlalchemy.engine.url import URL

app = Flask(__name__)
DB_URI = "postgresql:///yays"

#Connects to PostgreSQL database via Flask-SQLAlchemy helper library
db = SQLAlchemy()

####################################################################
# Model definitions

# db.Model is a base class for all Models for SQLAlchemy
# class User(db.Model):
# 	'''Defines a User object that interacts with app.'''
# 	# Needs to go to SQLAlchemy
# 	__tablename__ = "users"
# 	# Contains likes/dislikes of adventures and/or yums yays
# 	# Contains password
# 	# Contains their 'genre'

# 	# email & pass needed to instantiate User
# 	def __init__(self,email,password):
# 		self.email = email
# 		self.password = password

# 	# when object called, show helpful info
# 	def __repr__(self):
# 		return '<User %r>' % self.email
# 	pass

class Adventure(object):
	'''Defines an adventure'''
	# Contains 2 Possibilities (1 named Yum and 1 named Yay) 
	pass

class Possibility(object):
	'''Defines a possibility. Should be named either Yum or Yay'''
	# __init__ self.lat, self.long, self.radius, self.time
	# function - get new
	# function - get current
	# made up of list of options
	pass

class Yay(db.Model):
	''' Defines a Yay.'''
	# Objects created from either a db query or a Yelp API call
	__tablename__ = "yays"

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(75), nullable=False)
	url = db.Column(db.String(300), nullable=False)
	location = db.Column(db.String(100), nullable=False)

	def __init__(self, name, url, location):
		self.name = name
		self.url = url
		self.location = location

	def __repr__(self):
		return '<Option %r>' % self.name



####################################################################
# Helper functions

def connect_to_db(app):
	"""
	Performs db connection using db settings from settings.py
	"""

	#Configure to use PostgreSQL database
	app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///yays'
	app.config['SQLALCHEMY_ECHO'] = True
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	db.app = app
	db.init_app(app)

if __name__ == "__main__":
	from server import app
	connect_to_db(app)
	print "Connected to DB"

