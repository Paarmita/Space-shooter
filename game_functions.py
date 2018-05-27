import sys
import pygame
from bullet import Bullet

def check_events(ai_settings, screen, ship, bullets):
# Respond to keypresses and mouse events.
# Watch for keyboard and mouse events.
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			#to exit the game when the player quits
			sys.exit()

		# keydown->right->centre shift
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)

		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
			

def update_screen(ai_settings, screen, ship, aliens, bullets):
# Update images on the screen and flip to the new screen.
# Redraw the screen during each pass through the loop.
	# screen.fill(bg_color)
	screen.fill(ai_settings.bg_color)

	ship.blitme()
	aliens.draw(screen)
	alien.blitme()
	

	# Redraw all bullets behind ship and aliens.
	for bullet in bullets.sprites():
		# draw all fired bullets to the screen
		bullet.draw_bullet()

	# Make the most recently drawn screen visible.
	pygame.display.flip()

def check_keydown_events(event, ai_settings, screen, ship, bullets):
	#Respond to keypresses.
	if event.key == pygame.K_RIGHT:
		# true when key pressed false when released
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
		# Move the ship to the right.
		ship.rect.centerx += 1
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets)
	elif event.key == pygame.K_esc:
		sys.exit()
		

def check_keyup_events(event, ship):
	# Respond to key releases.
	if event.key == pygame.K_RIGHT:
		# set to false when keyup
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False



def update_bullets(bullets):
# Update position of bullets and get rid of old bullets
# Update bullet positions.
	bullets.update()

	# # Get rid of bullets that have disappeared as they consume memory.
	# for bullet in bullets.copy():
	# 	if bullet.rect.bottom <= 0:
	# 		bullets.remove(bullet)
	# print(len(bullets))

def fire_bullet(ai_settings, screen, ship, bullets):
	# Fire a bullet if limit not reached yet.
	# Create a new bullet and add it to the bullets group.
	# before firing check the no 
	# if len(bullets) < ai_settings.bullets_allowed:
	new_bullet = Bullet(ai_settings, screen, ship)
	bullets.add(new_bullet)