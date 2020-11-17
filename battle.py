import references.battle_ref
def battle(person):
	person()
	battleon = True
	while battleon == True:
		print('''
BATTLE!
1. Attack
2. Defend
3. Talk
4. Inventory
5. Run 
6. Help
		''')
		chc = input('>> ')
		chc = int(chc)
		if chc == 1:
			print('Attacking with Selected Weapen')
			references.battle_ref.fighting.calc.dmg_calc(person)
		elif chc == 2:
			print('Protecting Your Self')
			references.battle_ref.calc.ptc_calc()
		elif chc == 3:
			print('What do you want to say?')
			say = input('>> ')
			references.text.battle(say)
		elif chc == 4:
			print(references.self())
		elif chc == 5:
			references.battle_ref.run()
		elif chc == 6:
			references.help('battle')
		else:
			print('Error with Choice')

	
		