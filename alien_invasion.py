# -*- coding: utf-8 -*-
import sys
import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
from button import Button # to draw bullets to the screen 
from scoreboard import Scoreboard
from pygame.sprite import Group


def run_game():
	# Initialize game, settings and create a screen object.
	pygame.init()
	# screen = pygame.display.set_mode((1200, 800))
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Space-shooter")
	 
	# Make the Play button.
	play_button = Button(ai_settings, screen, "Play")
	
	# Create an instance to store game statistics and create a scoreboard.
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats) 

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
		gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
		
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
			gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
		
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()