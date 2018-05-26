import sys
import pygame
from settings import Settings

def run_game():
	 # Initialize game, settings and create a screen object.
	 pygame.init()
	 #screen = pygame.display.set_mode((1200, 800))
	 ai_settings = Settings()
	 screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	 pygame.display.set_caption("Alien Invasion")
	 
	 # Set the background color RGB.
	 bg_color = (230, 230, 230)

	 # Start the main loop for the game.
	 while True:
		 
		 # Watch for keyboard and mouse events.
		 for event in pygame.event.get():
		 	if event.type == pygame.QUIT:
		 		#to exit the game when the player quits
				sys.exit()
		 	# Redraw the screen during each pass through the loop.
			screen.fill(bg_color)

		 # Make the most recently drawn screen visible.
		 pygame.display.flip()

run_game()