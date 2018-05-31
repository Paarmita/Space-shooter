# -*- coding: utf-8 -*-
import sys
import pygame
from time import sleep
from bullet import Bullet
from alien import Alien

def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
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

		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			# to check mouse click on buttoon only from get_pos()
			check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)
			
def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
# Update images on the screen and flip to the new screen.
# Redraw the screen during each pass through the loop.
	# screen.fill(bg_color)
	screen.fill(ai_settings.bg_color)

	ship.blitme()
	aliens.draw(screen)
	# aliens.blitme()s

	# Redraw all bullets behind ship and aliens.
	for bullet in bullets.sprites():
		# draw all fired bullets to the screen
		bullet.draw_bullet()

	# Draw the score information.
	sb.show_score()
	
	# Draw the play button if the game is inactive.
	if not stats.game_active:
		play_button.draw_button()

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
	elif event.key == pygame.K_ESCAPE:
		sys.exit()
	
		
def check_keyup_events(event, ship):
	# Respond to key releases.
	if event.key == pygame.K_RIGHT:
		# set to false when keyup
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
	# Update position of bullets and get rid of old bullets
	# Update bullet positions.
	bullets.update()

	# # Get rid of bullets that have disappeared as they consume memory.
	# for bullet in bullets.copy():
	# 	if bullet.rect.bottom <= 0:
	# 		bullets.remove(bullet)
	# print(len(bullets))

	check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)
	
# Whenever the rects of a bullet and alien overlap, 
# groupcollide() adds a key-value pair to the dictionary it returns. 
# The two True arguments tell Pygame whether to delete the bullets and aliens that have collided


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
	# Respond to bullet-alien collisions.
	# Remove any bullets and aliens that have collided
	# Check for any bullets that have hit aliens.
	# If so, get rid of the bullet and the alien.
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

	if collisions:
		# stats.score += ai_settings.alien_points
		# to ensure if 2 bullets collide at same time then score for two or more precise game
		for aliens in collisions.values(): #collisions dictionary
			stats.score += ai_settings.alien_points * len(aliens)
			sb.prep_score()
			# call prep_score() to create a new image for the updated score
		check_high_score(stats, sb)

	if len(aliens) == 0: # check group aliens empty
		# Destroy existing bullets, speed up game and create new fleet.
		bullets.empty()
		ai_settings.increase_speed()

		# If the entire fleet is destroyed, start a new level.
		# Increase level.
		stats.level += 1
		sb.prep_level()		

		create_fleet(ai_settings, screen, ship, aliens)
		print("Collision!!!")

def fire_bullet(ai_settings, screen, ship, bullets):
	# Fire a bullet if limit not reached yet.
	# Create a new bullet and add it to the bullets group.
	# before firing check the no 
	# if len(bullets) < ai_settings.bullets_allowed:
	new_bullet = Bullet(ai_settings, screen, ship)
	bullets.add(new_bullet)

def get_number_aliens_x(ai_settings, alien_width):
	# Determine the number of aliens that fit in a row.
	# calculating horizontal space to fit 
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
	# Determine the number of rows of aliens that fit on the screen.
	available_space_y = (ai_settings.screen_height - (2 * alien_height) - ship_height)
	number_rows = int(available_space_y / (2 * alien_height))
	return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
	# Create an alien and place it in the row.
	alien = Alien(ai_settings, screen)
	# Create an alien and find the number of aliens in a row.
	# Spacing between each alien is equal to one alien width.
	alien_width = alien.rect.width
	# Create an alien and place it in the row.
	alien = Alien(ai_settings, screen)
	# set it's x-coordinate value to place it in the row
	alien.x = alien_width + 2 * alien_width * alien_number
	# pushed to the right one alien width from the left margin
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	# add to alien group
	aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
	# Create a full fleet of aliens.
	alien = Alien(ai_settings, screen)
	number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
	number_rows = get_number_rows(ai_settings, ship.rect.height,alien.rect.height)

	# Create the fleet of aliens.
	for row_number in range(number_rows):
		# Create the first row of aliens.
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings, screen, aliens, alien_number,row_number)

def check_fleet_edges(ai_settings, aliens):
	# Respond appropriately if any aliens have reached an edge."""
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings, aliens)
			# print("Fleet direction changed!!!")
			break

def change_fleet_direction(ai_settings, aliens):
	# Drop the entire fleet and change the fleet's direction."""
	for alien in aliens.sprites():
		# loop through all the aliens and drop each one using the setting fleet_drop_speed 
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1

def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
	# Respond to ship being hit by alien.
	# to check atleast 1 ship remaining
	if stats.ships_left > 0:
		# Decrement ships_left.
		stats.ships_left -= 1

		# Update scoreboard.
		sb.prep_ships()

		# Empty the list of aliens and bullets.
		aliens.empty()
		bullets.empty()

		# Create a new fleet and center the ship.
		create_fleet(ai_settings, screen, ship, aliens)
		ship.center_ship()
		print("New fleet after hit!!!")

		# Pause.
		sleep(0.5)
	else:
		stats.game_active = False
		pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
	# Check if any aliens have reached the bottom of the screen.
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			# Treat this the same as if the ship got hit.
			ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
			print("Aliens bottom!!!")
			break

def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
	# Check if the fleet is at an edge,
	# and then update the postions of all aliens in the fleet.
	check_fleet_edges(ai_settings, aliens)
	# Update the postions of all aliens in the fleet.
	aliens.update()
	# Look for alien-ship collisions.
	# spritecollideany() looks for any member of the group that’s collided with 
	# the sprite and stops looping through the group as soon as it finds one member 
	# has collided with the sprite.
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
		print("Ship hit!!!")
	# Look for aliens hitting the bottom of the screen.
	check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)

# Start a new game when the player clicks Play.
def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):	
	button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
	if button_clicked and not stats.game_active:
		# Reset the game settings.
		ai_settings.initialize_dynamic_settings()

		# Hide the mouse cursor after button click
		pygame.mouse.set_visible(False)

		# Reset the game statistics.
		stats.reset_stats() # gives player 3 new ships
		stats.game_active = True

		# Reset the scoreboard images.
		sb.prep_score()
		sb.prep_high_score()
		sb.prep_level()
		# To show the player how many ships they have to start with
		sb.prep_ships()

		# Empty the list of aliens and bullets.
		aliens.empty()
		bullets.empty()

		# Create a new fleet and center the ship.
		create_fleet(ai_settings, screen, ship, aliens)
		ship.center_ship()

def check_high_score(stats, sb):
	# Check to see if there's a new high score.
	if stats.score > stats.high_score:
		stats.high_score = stats.score
		sb.prep_high_score()