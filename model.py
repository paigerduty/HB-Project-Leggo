"""Classes for database only"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import geocoder


app = Flask(__name__)
DB_URI = "postgresql:///yays"

#Connects to PostgreSQL database via Flask-SQLAlchemy helper library
db = SQLAlchemy()

class Yay(db.Model):
	'''An activity with a name, url, location.'''
	__tablename__ = "yays"

	name = db.Column(db.String(75), primary_key=True,nullable=False)
	url = db.Column(db.String(300), nullable=False)
	location = db.Column(db.String(100), nullable=False)

	def __init__(self, name, url, location):
		self.name = name
		self.url = url
		self.location = location

	def __repr__(self):
		return '<Yay %r>' % self.name

	def geolocate(self):
		g = geocoder.google(self.location + ' San Francisco, CA')
		self.latitude, self.longitude = g.lat, g.lng 


####################################################################
# Helper functions

def connect_to_db(app,url='postgresql:///yays'):
	"""Connect the database to Flask app."""

	#Configure to use PostgreSQL database
	app.config['SQLALCHEMY_DATABASE_URI'] = url
	app.config['SQLALCHEMY_ECHO'] = True
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
	db.app = app
	db.init_app(app)

if __name__ == "__main__":
	connect_to_db(app)
	print "Connected to DB"

	db.create_all()
