import pygame
from pygame.locals import *
import random
import ctypes

# Initialize Pygame
pygame.init()

# Get the screen size
user32 = ctypes.windll.user32
screen_width, screen_height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

# Set up the window
screen = pygame.display.set_mode((screen_width, screen_height), FULLSCREEN)
pygame.display.set_caption("Raining 0s and 1s")

# Define colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Create the raindrops
raindrops = []
for _ in range(100):
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    raindrops.append([x, y])

clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Update screen size if it changes
    screen_width, screen_height = pygame.display.get_surface().get_size()

    # Fill the background with black color
    screen.fill(BLACK)

    # Update and draw the raindrops
    for i in range(len(raindrops)):
        # Move the raindrop down
        raindrops[i][1] += 5

        # Draw the raindrop as a text (0 or 1) in green color
        text = random.choice(["0", "1"])
        raindrop_text = pygame.font.SysFont(None, 20).render(text, True, GREEN)
        screen.blit(raindrop_text, raindrops[i])

        # Reset the raindrop position when it reaches the bottom
        if raindrops[i][1] > screen_height:
            raindrops[i][1] = random.randint(-50, -10)
            raindrops[i][0] = random.randint(0, screen_width)

    pygame.display.update()
    clock.tick(30)

# Quit the game
pygame.quit()
