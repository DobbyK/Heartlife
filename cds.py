import config

def look():
	import maps
	print('Here is a description of the current area:')
	if config.locatation == 'Heart Central':
		maps.heartcentral()
		return
	else:
		print('Error')
	