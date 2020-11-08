import functions
import config
import cdline
from replit import db


functions.cutscenes.openingmenu()

if config.newbie == True:
  functions.cutscenes.newbie_adventure()
elif config.newbie == False:
  functions.spawn.newgame()
		
while config.free == True:
	chc = input('>> ')
	db["cd"] = chc
	cdline.command()
