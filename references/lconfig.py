import references.config
class lc:
	class heartlook:
		def heartcentral():
			references.config.north = True
			references.config.south = True
			references.config.east = True
			references.config.west = True
			references.config.nw = False
			references.config.sw = False
			references.config.ne = True
			references.config.se = False
		def tree_of_hearts():
			references.config.north = True
			references.config.south = False
			references.config.east = True
			references.config.west = True
			references.config.nw = False
			references.config.sw = False
			references.config.ne = False
			references.config.se = False
		def goverment_plasa():
			references.config.north = False
			references.config.south = True
			references.config.east = True
			references.config.west = True
			references.config.nw = False
			references.config.sw = True
			references.config.ne = False
			references.config.se = False

		
	# class heartlook_suburbs: