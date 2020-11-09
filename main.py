# Import Everything
import functions
import references.config
import cmline.cdline
import pygame
from replit import db

# Default Settings
pygame.init()
# Opening Stuff 
functions.cutscenes.openingmenu()

if references.config.newbie == True:
  functions.cutscenes.newbie_adventure()
elif references.config.newbie == False:
  functions.spawn.newgame()

# Command line loop
while references.config.free == True:
	chc = input('>> ')
	db["cd"] = chc
	cmline.cdline.command()


