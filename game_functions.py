import sys
import pygame

def check_events(ship):
# Respond to keypresses and mouse events.
# Watch for keyboard and mouse events.
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			#to exit the game when the player quits
			sys.exit()

		# keydown->right->centre shift
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ship)

		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
			

def update_screen(ai_settings,screen,ship):
# Update images on the screen and flip to the new screen.
# Redraw the screen during each pass through the loop.
	# screen.fill(bg_color)
	screen.fill(ai_settings.bg_color)
	ship.blitme()

	# Make the most recently drawn screen visible.
	pygame.display.flip()

def check_keydown_events(event, ship):
	#Respond to keypresses.
	if event.key == pygame.K_RIGHT:
		# true when key pressed false when released
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
		# Move the ship to the right.
		ship.rect.centerx += 1

def check_keyup_events(event, ship):
	# Respond to key releases.
	if event.key == pygame.K_RIGHT:
		# set to false when keyup
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False