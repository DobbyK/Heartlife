	# import config
from colorama import Fore, Back, Style
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
		x = input(Fore.RED + '>> ')
		if x == 'y':
			print(Fore.WHITE + 'Ahh! Then we should explain the game to you!')
		if x == 'n':
			print(Fore.WHITE + 'In that case, do you want to start a new game? (y/n)')
			x = input(Fore.WHITE + '>> ')
			if x == 'y':
				return
			if x == 'n':
				print('Copy and paste your save data bellow:')
				x = input('>> ')