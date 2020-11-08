import cds
from replit import db
def command():
	val = db["cd"]
	if val == 'l':
		cds.look()
		return
	elif val == 'm':
		cds.map()
		return
	elif val == 'sit':
		cds.sit()
		return
	else:
		print('Error, Invalid Command!')
		return
	