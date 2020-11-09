import cmline.cds
import references.config
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
		if references.config.north == True:
			cmline.cds.movement.north()
			return
		elif references.config.north == False:
			print("You can't seem to go that way!")
			return
	elif val == 's':
		if references.config.south == True:
			cmline.cds.movement.south()
			return
		elif references.config.south == False:
			print("You can't seem to go that way!")
			return
	elif val == 'e':
		if references.config.east == True:
			cmline.cds.movement.east()
			return
		elif references.config.east == False:
			print("You can't seem to go that way!")
			return
	elif val == 'w':
		if references.config.west == True:
			cmline.cds.movement.west()
			return
		elif references.config.west == False:
			print("You can't seem to go that way!")
			return
	elif val == 'q':
		print('Are you sure you want to exit? (y/n)')
		exitc = input('>> ')
		if exitc == 'y':
			print(';( Why?????')
			exit()
		else:
			print('Thanks For Staying :)')
			return
	else:
		print('Error, Invalid Command!')
		return
	