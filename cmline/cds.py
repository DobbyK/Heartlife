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