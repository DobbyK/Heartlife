import references.config
import references.des
import references.maps
def look():
	print('Here is a description of the current area:')
	if references.config.locatation == 'Heart Central':
		references.des.heartcentral()
		return
	else:
		print('Error')

def map():
	print('Here is a map of the current Area:')
	if references.config.locatation == 'Heart Central':
		references.maps.heartcentralmap()
		return
	else:
		print('Error')

def sit():
	if references.config.status == 'Standing':
		print('You sit down.')
		print('Nothing Much Happens.')
		references.config.status = 'Sitting'
		return
	elif references.config.status == 'Sitting':
		print('You are already sitting!')
		return
	else:
		print('Error')

def stand():
	if references.config.status == 'Sitting':
		print('You stand up')
		print('Nothing Much Happens')
		references.config.status = 'Standing'
		return
	elif references.config.status == 'Standing':
		print('You are already standing')
		return
	else:
		print('Error')
		return

def help():
	try:
		print('What do you need help with? 1. Commands 2. Story 3. Goal 4. I am bored')
		help = input('>> ')
		help = int(help)
	except:
		print('Error Please enter a interger.')
		help()
	if help == 1:
		print('List all commands (1) or Search (2)?')
		help2 = input('>> ')
		help2 = int(help2)
		if help2 == 1:
			print('''
l - gives a description of current area
m - shows map of current area					
			''')
			return
		elif help2 == 2:
			print('''
test
			''')
			return
	# elif help == 2:
		# search = input('>>')
	else:
		print('Please enter a interger 1 - 3')

class movement():
	def north():
		if references.config.north == True:
			print('You move north')
			if references.config.precise_location == 'Central Heartlook':
				print('You are now in Heartlook Goverement Plasa')
				references.config.precise_location == 'Heartlook Goverement Plasa'
				return
			else:
				print('Error')
				return
		elif references.config.north == False:
			print('There is no path north you can see')
			return
		else:
			print('Error')
			return
	def south():
		if references.config.south == True:
			print('You move south')
			if references.config.precise_location == 'Central Heartlook':
				print('You are now in Tree of Heartlook')
				references.config.precise_location == 'Tree of Heartlook'
				return
			else:
				print('Error')
				return
		elif references.config.north == False:
			print('There is no path south you can see')
			return
		else:
			print('Error')
			return
	def east():
		if references.config.east == True:
			print('You move east')
			if references.config.precise_location == 'Central Heartlook':
				print('You are now in Heartlook Hotel Outside')
				references.config.precise_location == 'Heartlook Hotel Outside'
				return
			else:
				print('Error')
				return
		elif references.config.east == False:
			print('There is no path east you can see')
			return
		else:
			print('Error')
			return
	def west():
		if references.config.west == True:
			print('You move west')
			if references.config.precise_location == 'Central Heartlook':
				print('You are now in Heartlook Shoping Center')
				references.config.precise_location == 'Heartlook Shoping Center'
				return
			else:
				print('Error')
				return
		elif references.config.north == False:
			print('There is no path west you can see')
			return
		else:
			print('Error')
			return