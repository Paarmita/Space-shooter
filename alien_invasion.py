# -*- coding: utf-8 -*-
import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien
# to draw bullets to the screen 
from pygame.sprite import Group


def run_game():
	# Initialize game, settings and create a screen object.
	pygame.init()
	# screen = pygame.display.set_mode((1200, 800))
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Space-shooter")
	 
	# Make a ship.
	ship = Ship(ai_settings, screen)

	# Make a group to store bullets in and group of aliens.
	bullets = Group()
	aliens = Group()

	# Make an alien.
	alien = Alien(ai_settings, screen)

	# Create the fleet of aliens.
	gf.create_fleet(ai_settings, screen, ship, aliens)

	# Set the background color RGB.
	bg_color = (230, 230, 230)

	# Start the main loop for the game.
	while True:
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
		gf.update_aliens(ai_settings, aliens)
		gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()