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
		return
	elif val == 'help':
		cmline.cds.help()
		return
	elif val == 'n':
		cmline.cds.movement.north()
		return
	elif val == 's':
		cmline.cds.movement.south()
		return
	elif val == 'e':
		cmline.cds.movement.east()
		return
	elif val == 'w':
		cmline.cds.movement.west()
		return
	elif val == 'q':
		exit()
	else:
		print('Error, Invalid Command!')
		return
	