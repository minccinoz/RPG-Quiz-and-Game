import pygame
import random

# Names: Sara D’Alessandro and Arianna Chinchilla
# MH-CSC140
# Final Project

WIDTH = 360
HEIGHT = 480
FPS = 30
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# initial pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("game")
clock = pygame.time.Clock()

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

	# Draw / render
	screen.fill(black)
	# !! after drawing everything, flip display
	pygame.display.flip()

pygame.quit()