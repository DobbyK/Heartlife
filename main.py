import functions
import config
import cdline
import pygame
from replit import db

pygame.init()

functions.cutscenes.openingmenu()

if config.newbie == True:
  functions.cutscenes.newbie_adventure()
elif config.newbie == False:
  functions.spawn.newgame()
		
while config.free == True:
	chc = input('>> ')
	db["cd"] = chc
	cdline.command()

while config.working == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            config.working = False
