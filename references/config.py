from replit import db
import pygame

def defaults():
	global black
	global screen
	size = (800, 600)
	screen = pygame.display.set_mode(size)
	pygame.display.set_caption("HeartLife")	
	global logo
	global working
	global status
	global cd
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
	working = True
	db["cd"] = 'None'
	newbie = None
	name = None
	gamemode = None
	goal = None
	locatation = 'Heart Central'
	free = False
	status = 'Standing'
	logo = pygame.image.load('.//sprites//heartlife_logo.png')



