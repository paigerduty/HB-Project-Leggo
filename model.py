"""Classes for database only"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
DB_URI = "postgresql:///yays"

#Connects to PostgreSQL database via Flask-SQLAlchemy helper library
db = SQLAlchemy()

class Yay(db.Model):
	'''An activity with a name, url, location.'''
	__tablename__ = "yays"

	def __init__(self, name, url, location):
		self.name = name
		self.url = url
		self.location = location

	def __repr__(self):
		return '<Yay %r>' % self.name

	name = db.Column(db.String(75), primary_key=True,nullable=False)
	url = db.Column(db.String(300), nullable=False)
	location = db.Column(db.String(100), nullable=False)


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
