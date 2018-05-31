# -*- coding: utf-8 -*-
import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	
	# constructor
	def __init__(self, ai_settings, screen):
		# Initialize the ship and set its starting position.
		super(Ship, self).__init__()
		self.screen = screen
		# access speed settings
		self.ai_settings = ai_settings

		# Load the ship image and get its rect.
		self.image = pygame.image.load('images/ship.bmp')
		self.image = pygame.transform.scale(self.image, (50,50))
		# to access the surface’s rect attribute
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# Start each new ship at the bottom center of the screen.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
	 	
	 	# Store a decimal value for the ship's center aswe are using in speed
		self.center = float(self.rect.centerx)

		# Movement flags
		self.moving_right = False
		self.moving_left = False

	def update(self):
		# Update the ship's position based on the movement flag.
		# limiting the range of ship
		if self.moving_right and self.rect.right < self.screen_rect.right:
			# Update the ship's center value, not the rect.
			self.center += self.ai_settings.ship_speed_factor
			# self.rect.centerx += 1

		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor
			# self.rect.centerx -= 1

		# Update rect object from self.center.
		self.rect.centerx = self.center

	def blitme(self):
		# Draw the ship at its current location.
		self.screen.blit(self.image, self.rect)

	def center_ship(self):
		# Center the ship on the screen.
		self.center = self.screen_rect.centerx

# centerx store only integer values and not decimal and we are using decimal values for speed