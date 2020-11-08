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