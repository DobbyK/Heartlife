import config
import des
def look():
	print('Here is a description of the current area:')
	if config.locatation == 'Heart Central':
		des.heartcentral()
		return
	else:
		print('Error')

def map():
	import maps
	print('Here is a map of the current Area:')
	if config.locatation == 'Heart Central':
		maps.heartcentralmap()
		return
	else:
		print('Error')

def sit():
	if config.status == 'Standing':
		print('You sit down.')
		print('Nothing Much Happens.')
		config.status = 'Sitting'
		return
	elif config.status == 'Sitting':
		print('You are already sitting!')
		return
	else:
		print('Error')

def stand():
	if config.status == 'Sitting':
		print('You stand up')
		print('Nothing Much Happens')
		config.status = 'Standing'
		return
	elif config.status == 'Standing':
		print('You are already standing')
		return
	else:
		print('Error')
		return

def help():
	print('What do you need help with? 1. Commands 2. Story 3. Goal 4. I am bored')
	help = input('>> ')
	if help == '1':
		return
	return
