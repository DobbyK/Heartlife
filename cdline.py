import cds
cd = None

def command():
	global cd
	cd = None
	while not cd:
		cd = input('>> ')
	if cd == 'l' or 'look':
		cds.look()
		return
	