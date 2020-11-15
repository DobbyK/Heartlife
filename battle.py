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
	
		