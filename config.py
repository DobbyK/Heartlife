from replit import db

def defaults():
	global status
	global cd
	global free
	global newbie
	global locatation
	global name 
	global gamemode
	global goal
	global locatation 
	db["cd"] = 'None'
	newbie = None
	name = None
	gamemode = None
	goal = None
	locatation = 'Heart Central'
	free = False
	status = 'Standing'

