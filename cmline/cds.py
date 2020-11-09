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
	print('What do you need help with? 1. Commands 2. Story 3. Goal 4. I am bored')
	help = input('>> ')
	if help == '1':
		return
	return
