import datetime
from sqlalchemy import func
from model import Yay, connect_to_db, db
from server import app


def load_yays():
	"""Loads users from scraped_itmes into db."""
	for i, row in enumerate(open("tutorial/scraped_items.txt")):
		row = row.strip()
		if row != '':
			name, url, location = row.split("|") 

			# instantiate Yay object
			yay = Yay(name=name,url=url,location=location)
			# Add yay to session to store it
			db.session.add(yay)

		# Save changes
		db.session.commit()

if __name__ == "__main__":
	connect_to_db(app)
	db.create_all()

	load_yays()
