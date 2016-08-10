"""Model & database function for Sprint 1 - Leggo."""

from flask_sqlalchemy import SQLAlchemy

#Connects to PostgreSQL database via Flask-SQLAlchemy helper library
db = SQLAlchemy()

####################################################################
# Model definitions

class User(db.Model):
	'''Defines a User object that interacts with app.'''
	pass

class Adventure(db.Model):
	'''Defines an Adventure object (1 Yay & 1 Yum)'''
	pass

class Component(db.Model):
	'''Defines unique attributes of a part of Adventure.'''
	pass

class Yay(db.Model):
	''' Defines a Yay object (1 restaurant/bar/snack). Child of Component'''

	__tablename__ = "yays"

	yay_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	description = db.Column(db.String(500), nullable=False)
	url = db.Column(db.String(500), nullable=True)

class Yum(db.Model):
	'''Defines a Yum object (1 activity). Child of Component.'''
	pass

####################################################################
# Helper functions

def connect_to_db(app):
	"""Connect the database to Flask app."""

	#Configure to use PostgreSQL database
	app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///yays'
	db.app = app
	db.init_app(app)

if __name__ == "__main__":
	from server import app
	connect_to_db(app)
	print "Connected to DB"