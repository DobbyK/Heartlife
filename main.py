# Import Everything
import functions
import references.config
import cmline.cdline
import pygame

# Default Settings
pygame.init()
# Opening Stuff 
functions.cutscenes.openingmenu()
# Newbie Adventure
if references.config.newbie == True:
  functions.cutscenes.newbie_adventure()
elif references.config.newbie == False:
  functions.spawn.newgame()

# Command line loop
while references.config.free == True:
	references.config.chc = input('>> ')
	cmline.cdline.command()


