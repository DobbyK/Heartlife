	# import config
from colorama import Fore, Back, Style
import time
import saving
import config
import maps
import cdline

config.init()

class cutscenes:
	def openingmenu():
		print('''
██╗░░██╗███████╗░█████╗░██████╗░████████╗██╗░░░░░██╗███████╗███████╗
██║░░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██║░░░░░██║██╔════╝██╔════╝
███████║█████╗░░███████║██████╔╝░░░██║░░░██║░░░░░██║█████╗░░█████╗░░
██╔══██║██╔══╝░░██╔══██║██╔══██╗░░░██║░░░██║░░░░░██║██╔══╝░░██╔══╝░░
██║░░██║███████╗██║░░██║██║░░██║░░░██║░░░███████╗██║██║░░░░░███████╗
╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝╚═╝░░░░░╚══════╝
____________________________________________________________________
		''')
		print('Is this your first time playing? (y/n)')
		x = input(Fore.WHITE + '>> ')
		if x == 'y':
			config.newbie = True
			print(Fore.WHITE + 'Ahh! Then we should explain the game to you!')
			cutscenes.explain()
			cutscenes.newgame()
			return
		if x == 'n':
			config.newbie = False
			print(Fore.WHITE + 'Very Nice, thanks for playing again, do you want to start a new game? (y/n)')
			x = input(Fore.WHITE + '>> ')
			if x == 'y':
				cutscenes.newgame()
				return
			if x == 'n':
				print('Copy and paste your save data bellow:')
				x = input('>> ')
				saving.load()


# Explain The Game
	def explain():
		print('This game is about anything you want, You can be a Scientist, An Astronaut, (Well Maybe Not). But you get the point!')
		print('The point of the this game is to make a fantasy world that feels real, using text, and graphics.')
		time.sleep(5)
		print('You could be a god!')
		time.sleep(1)
		print('You could be a cat! Or a Dog! (Dog Clearly Better)')
		time.sleep(1)
		print('You could be a criminal!')
		time.sleep(1)
		print('What do you want to be?')
		time.sleep(0.5)
		print('Just Kidding you dont have to decide now!')
		time.sleep(2.5)
		print("Now since there is basically nothing else to explain! Let's Get into it!")
		return


	def newgame():
		print(Back.RED + 'ALERT MAJOR BUG - LISTEN TO THE INSTRUCTIONS THE GAME DOESNT CATCH EVERYTHING')
		gamemodechoice = None
		while not gamemodechoice:
			print(Style.RESET_ALL + 'What difficulity do you want? Easy (1), Medium (2), Hard (3), Realistic (4), Deadly (5), Psychically Immpossible (6)')		
			choice = input('>> ')
			global gamemode
			choice = int(choice)
			if choice >= 1 and choice <= 6:
				config.gamemode = choice
				gamemodechoice = True
			else:
				print("Must be an Integer 1 to 6")

		print("What's your name?")
		config.name = input('>> ')
		goalchoice = None
		
		while not goalchoice:
			print("What's your goal in life? Riches (1), Strength (2), Famousness (3), Power (4) as in goverment, All of them (5), or something else (6)")
			choice = input('>> ')
			try:
				config.goal = int(choice)
				if config.goal >= 1 and config.goal <= 6: 
					goalchoice = True
			except:
				print("Must be an Integer 1 to 6")
		print('Is this good? Name:', config.name, '  Gamemode:', config.gamemode, '  Goal:', config.goal)
	def newbie_adventure():
		print('Welcome to Heartlook,', config.name ,'! This is a massive world!')
		time.sleep(2)
		print('Who am I? Oh! My Name is...')
		time.sleep(1.5)
		print("I wouldn't tell you that! Anyways you might want a map!")
		time.sleep(1.5)
		print('Hahaha You will not get one! Ahahaha.')
		time.sleep(4)
		print('But On a Serious Note, I do not have one')
		time.sleep(1.5)
		print('Do I look like a Cartographer? No.')
		time.sleep(1.5)
		print('You picked easy mode, right? I mean that does not matter for this adventure.')
		time.sleep(1)
		print('Okay Bye...')
		print(Back.GREEN + 'Type: Map!' + Style.RESET_ALL)
		cd = input('>> ')
		print(Style.RESET_ALL + "Oh Wait You can't")
		print(cd + " Didn't work")
		print('Oh Well')
		print('Try LOOKing around')
		cdline.command()

class spawn:
	def newgame():
		config.locatation = 'Heart Central'
		print('This is the map of the current area:', + config.locatation)
		maps.heartcentral()
		