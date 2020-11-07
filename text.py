	# import config
from colorama import Fore, Back, Style
import time

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
		print(Fore.RED + 'Is this your first time playing? (y/n)')
		x = input(Fore.WHITE + '>> ')
		if x == 'y':
			print(Fore.WHITE + 'Ahh! Then we should explain the game to you!')
			cutscenes.explain()
			cutscenes.newgame()
		if x == 'n':
			print(Fore.WHITE + 'Very Nice, thanks for playing again, do you want to start a new game? (y/n)')
			x = input(Fore.WHITE + '>> ')
			if x == 'y':
				cutscenes.newgame()
			if x == 'n':
				print('Copy and paste your save data bellow:')
				x = input('>> ')

# Explain The Games Goal
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
		print('What difficulity do you want? Easy (1), Medium (2), Hard (3), Realistic (4), Deadly (5), Psychically Immpossible (6)')
		x = input('>> ')
		if x == '1':
			gamemode = 1
		if x == '2':
			gamemode = 2
		if x == '3':
			gamemode = 3
		if x == '4':	
			gamemode = 4	
		if x == '5':
			gamemode = 5
		if x == '6':
			gamemode = 6
		print("What's your name?")
		name = input('>> ')
		print("What's your goal in life? Riches (1), Strength (2), Famousness (3), Power (4) as in goverment ")
