import pygame

def defaults():
	global blue_black
	global precise_location
	global north
	global south
	global east 
	global west 
	global nw
	global sw 
	global ne
	global se
	global black
	global screen
	size = (800, 600)
	screen = pygame.display.set_mode(size)
	pygame.display.set_caption("HeartLife")	
	global logo
	global working
	global status
	global cdc
	global free
	global newbie
	global locatation
	global name 
	global gamemode
	global goal
	global locatation
	global white
	black = (0, 0, 0)
	white = (255, 255, 255)
	blue_black = (20, 12, 28)
	working = True
	cdc = None
	newbie = None
	name = None
	gamemode = None
	goal = None
	locatation = 'Heart Central'
	free = False
	status = 'Standing'
	logo = pygame.image.load('.//sprites/logo_art_2x.png')
	north = True
	south = True
	east = True
	west = True
	nw = False
	sw = False
	ne = True
	se = False
	precise_location = 'Central Heartlook'



