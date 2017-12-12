import pygame
import random
import os

# Names: Sara D’Alessandro and Arianna Chinchilla
# MH-CSC140
# Final Project

WIDTH = 800
HEIGHT = 600
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
		self.image.set_colorkey(black)
		self.rect = self.image.get_rect()
		self.rect.center = (WIDTH / 2, HEIGHT / 2)
		self.y_speed = 5

	def update(self):
		self.rect.x += 5
		self.rect.y += self.y_speed
		if self.rect.bottom > HEIGHT - 200:
			self.y_speed = -5
		if self.rect.top < 200:
			self.y_speed = 5
		if self.rect.left > WIDTH:
			self.rect.right = 0

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