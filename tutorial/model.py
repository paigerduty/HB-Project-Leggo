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

class Yay(db.Model):
	''' Defines a Yay.'''
	# Objects created from either a db query
	__tablename__ = "yays"
	name = db.Column(db.String(75), nullable=False, primary_key=True)
	url = db.Column(db.String(300), nullable=False)
	location = db.Column(db.String(100), nullable=False)

	def __init__(self, name, url, location):
		self.name = name
		self.url = url
		self.location = location

	def __repr__(self):
		return '<Option %r>' % self.name

	def make_json(self):
		return {
				'name' : self.name,
				'url' : self.url,
				'location' : self.location
		 		}
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

