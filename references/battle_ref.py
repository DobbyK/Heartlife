import config
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
			if config.stats.stat_track.ptc == 1:
				config.stats.battle = config.stats.battle * 1.1
			if config.stats.stat_track.ptc == 2:
				config.stats.battle = config.stats.battle * 1.2
			if config.stats.stat_track.ptc == 3:
				config.stats.battle = config.stats.battle * 1.3
			if config.stats.stat_track.ptc == 4:
				config.stats.battle = config.stats.battle * 1.4
			if config.stats.stat_track.ptc == 5:
				config.stats.battle = config.stats.battle * 1.5
			if config.stats.stat_track.ptc == 6:
				config.stats.battle = config.stats.battle * 1.6
			if config.stats.stat_track.ptc == 7:
				config.stats.battle = config.stats.battle * 1.1
			if config.stats.stat_track.ptc == 8:
				config.stats.battle = config.stats.battle * 1.1
			if config.stats.stat_track.ptc == 9:
				config.stats.battle = config.stats.battle * 1.1
			if config.stats.stat_track.ptc == 10:
				config.stats.battle = config.stats.battle * 1.1
		
			
			
			
	