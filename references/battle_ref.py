import references.config
class fighting:
	class enemys:
		def __init__(self, hp, atk, battle, spc, wis, char, moves):
			self.hp = hp
			self.atk = atk
			self.dfe = battle
			self.spc = spc
			self.wis = wis
			self.char = char
			self.moves = moves
		def jarzo(self):
			self.hp = 150
			self.atk = 125
			self.dfe = 175
			self.spc = 100
			self.wis = 200
			self.char = 150
	class calc:
		def dmg_calc(target):
			dmg = 5
			return dmg
		def ptc_calc():
			if references.config.stats.stat_track.ptc == 1:
				references.config.stats.battle.dfe = references.config.stats.dfe * 1.1
			elif references.config.stats.stat_track.ptc == 2:
				references.config.stats.battle.dfe = references.config.stats.dfe * 1.2
			elif references.config.stats.stat_track.ptc == 3:
				references.config.stats.battle.dfe = references.config.stats.dfe * 1.3
			elif references.config.stats.stat_track.ptc == 4:
				references.config.stats.battle.dfe = references.config.stats.dfe * 1.4
			elif references.config.stats.stat_track.ptc == 5:
				references.config.stats.battle.dfe = references.config.stats.dfe * 1.5
			elif references.config.stats.stat_track.ptc == 6:
				references.config.stats.battle.dfe = references.config.stats.dfe * 1.6
			elif references.config.stats.stat_track.ptc == 7:
				references.config.stats.battle.dfe = references.config.stats.dfe * 1.7
			elif references.config.stats.stat_track.ptc == 8:
				references.config.stats.battle.dfe = references.config.stats.dfe * 1.8
			elif references.config.stats.stat_track.ptc == 9:
				references.config.stats.battle.dfe = references.config.stats.dfe * 1.9
			elif references.config.stats.stat_track.ptc == 10:
				references.config.stats.battle.dfe = references.config.stats.dfe * 2
			else:
				print('Error dfe stat not found!')
		
			
			
			
	