"""Model & database function for Sprint 1 - Leggo."""

from flask_sqlalchemy import SQLAlchemy

#Connects to PostgreSQL database via Flask-SQLAlchemy helper library
db = SQLAlchemy()

####################################################################
# Model definitions

class Yay(db.Model):
	""" Activity option for adventure pairings."""

	__tablename__ = "yays"

	yay_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	description = db.Column(db.String(500), nullable=False)
	url = db.Column(db.String(500), nullable=True)

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