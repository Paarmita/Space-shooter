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