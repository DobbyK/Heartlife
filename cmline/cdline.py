import cmline.cds
from replit import db
def command():
	val = db["cd"]
	if val == 'l':
		cmline.cds.look()
		return
	elif val == 'm':
		cmline.cds.map()
		return
	elif val == 'lm':
		cmline.cds.map()
		cmline.cds.look()
		return
	elif val == 'sit':
		cmline.cds.sit()
		return
	elif val == 'stand':
		cmline.cds.stand()
	elif val == 'help':
		cmline.cds.help()
	else:
		print('Error, Invalid Command!')
		return
	