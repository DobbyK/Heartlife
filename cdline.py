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
	elif val == 'lm':
		cds.map()
		cds.look()
		return
	elif val == 'sit':
		cds.sit()
		return
	elif val == 'stand':
		cds.stand()
	elif val == 'help':
		cds.help()
	else:
		print('Error, Invalid Command!')
		return
	