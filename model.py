"""Model & database function for Sprint 1 - Leggo."""

from flask_sqlalchemy import SQLAlchemy

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

class Adventure(db.Model):
	'''Defines an Adventure object (1 Yay & 1 Yum)'''
	__tablename__ = "adventures"
	# id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	# yum_possibilities_id = db.Column(db.Integer, db.ForeignKey('yum_possibilities_id', nullable=False)
	# yay_possibilities_id = db.Column(db.Integer, db.ForeignKey('yay_possibilities_id', nullable=False)
	# Contains yum_possibilities and yay_possibilities list
	# Contains a collection of yum_possibilities and yay_possibilites
	# Contains a function to calculate all the possibilites
	# Contains a function to hold lists of possibilities and 'pop' them
	pass

class Component(db.Model):
	'''Defines unique attributes of a part of Adventure.'''
	
	# Not the best table name plz fix
	__tablename__ = "components"

	# id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
	# time = db.Column(db.Time, nullable=False)
	# lat = db.Column(db.Integer(8), nullable=False)
	# lng = db.Column(db.Integer(8), nullable=False)
	# name = db.Column(db.String(50), nullable=False)
	# desc = db.Column(db.String(300), nullable=False)
	# url = db.Column(db.String(200), nullable=False)
	# genre = db.Column(db.String(20), nullable=True)
	# time_bucket = db.Column(db.Integer(1), nullable=False)
	
	# Define relationship between Component and Yay
	# Define relationship bewteen Component and Yum
	# Backref them!!1
	
class Yay(Component):
	''' Defines a Yay object (1 restaurant/bar/snack). Child of Component'''
	__tablename__ = "yays"

	# id = db.Column(db.Integer, primary_key=True, autoincrement=True)


class Yum(Component):
	'''Defines a Yum object (1 activity). Child of Component.'''
	__tablename__ = "yums"

	# id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	# def __init__(self):
	# def __repr__(self):

####################################################################
# Helper functions

def connect_to_db(app):
	"""Connect the database to Flask app."""

	#Configure to use PostgreSQL database
	app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///yays'
	app.config['SQLALCHEMY_ECHO'] = True
	db.app = app
	db.init_app(app)

if __name__ == "__main__":
	from server import app
	connect_to_db(app)
	print "Connected to DB"