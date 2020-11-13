import cmline.cds
import references.config
def command():
	if references.config.chc == 'l':
		cmline.cds.look()
		return
	elif references.config.chc == 'm':
		cmline.cds.map()
		return
	elif references.config.chc == 'lm':
		cmline.cds.map()
		cmline.cds.look()
		return
	elif references.config.chc == 'sit':
		cmline.cds.sit()
		return
	elif references.config.chc == 'stand':
		cmline.cds.stand()
		return
	elif references.config.chc == 'help':
		cmline.cds.help()
		return
	elif references.config.chc == 'n':
		if references.config.north == True:
			cmline.cds.movement.north()
			return
		elif references.config.north == False:
			print("You can't seem to go that way!")
			return
	elif references.config.chc == 's':
		if references.config.south == True:
			cmline.cds.movement.south()
			return
		elif references.config.south == False:
			print("You can't seem to go that way!")
			return
	elif references.config.chc == 'e':
		if references.config.east == True:
			cmline.cds.movement.east()
			return
		elif references.config.east == False:
			print("You can't seem to go that way!")
			return
	elif references.config.chc == 'w':
		if references.config.west == True:
			cmline.cds.movement.west()
			return
		elif references.config.west == False:
			print("You can't seem to go that way!")
			return
	elif references.config.chc == 'q':
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
	