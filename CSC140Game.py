import pygame
import random
import os

# Names: Sara D’Alessandro and Arianna Chinchilla
# MH-CSC140
# Final Project

WIDTH = 800
HEIGHT = 300
FPS = 30
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)

# set up assets folders
# Mac: /Users/arianna/Documents/SCHOOL/CSC140
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder,"img")

class Player(pygame.sprite.Sprite):
	# sprite for the player
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(os.path.join(img_folder,"healer.png")).convert()
		self.rect = self.image.get_rect()
		self.image.set_colorkey(black)
		self.rect.centerx = WIDTH / 2
		self.rect.bottom = HEIGHT - 10
		self.speedx = 0

	def update(self):
		self.speedx = 0
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
			self.speedx = -5
		if keys[pygame.K_RIGHT]:
			self.speedx = 5
		self.rect.x += self.speedx

# initial pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("game")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# game loop
running = True
while running:
	# keep loop running at the right speed
	clock.tick(FPS)
	# process input (events)
	for event in pygame.event.get():
		# check for closing window
		if event.type == pygame.QUIT:
			running = False
	# Update
	all_sprites.update()

	# Draw / render
	screen.fill(blue)
	all_sprites.draw(screen)
	# !! after drawing everything, flip display
	pygame.display.flip()

pygame.quit()