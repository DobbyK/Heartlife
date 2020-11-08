def heartcentral():
	import cdline
	if cdline.cd == 'l' or 'look':
		print('You are in a huge city connected by mostly tunnels, You seem to think you are underground.')
	else:
		print(''' <--[  ]----[]---[   ]
		|       /        |
		[  ]---[ ]-[]   [ ]---> 
		|
		\         []--[]
		[ ]------[      ]-->
		''')
	
