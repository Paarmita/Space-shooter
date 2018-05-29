class Settings():
	# A class to store all settings for Alien Invasion.
	def __init__(self):
		# Initialize the game's settings.
		
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (255,255,255)

		# Ship settings
		self.ship_speed_factor = 1.5

		# Bullet settings
		self.bullet_speed_factor = 1
		self.bullet_width = 10
		self.bullet_height = 15
		self.bullet_color = (0,0,0)
		# self.bullets_allowed = 3 # to limit the no of bullets
		# Alien settings
		self.alien_speed_factor = 1
		# controls how quickly the fleet drops down 
		# the screen each time an alien reaches either edge. 
		self.fleet_drop_speed = 10
		# fleet_direction of 1 represents right; -1 represents left.
		self.fleet_direction = 1