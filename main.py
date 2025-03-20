import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # start game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # quit and close window if X is clicked
                return
        screen.fill("black") # color the screen
        pygame.display.flip() # render the page
        dt = clock.tick(60) # set framerate and return delta


if __name__ == "__main__":
    main()