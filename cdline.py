import cds
from replit import db
def command():
	val = db["cd"]
	print(val)
	if val == 'l':
		cds.look()
		return
	elif val == 'm':
		cds.map()
		return
	else:
		print('Error, Invalid Command!')
		return
	