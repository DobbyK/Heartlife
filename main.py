import functions
import config
config.init()

functions.cutscenes.openingmenu()

if config.newbie == True:
	functions.cutscenes.newbie_adventure()
elif config.newbie == False:
	function.spawn.newgame()