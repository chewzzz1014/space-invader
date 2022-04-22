import pygame
import sys
from setting import Settings
from ship import Ship

def run_game():
    # initialization
    pygame.init()

    # instance of class settings
    # so that we can modify the settings of the game easily
    game_settings = Settings()

    # create window screen (surface). Width is 1200 and height is 800
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))

    # make a ship
    ship = Ship(screen)

    # set caption of the window
    pygame.display.set_caption("Alien Invasion")

    while True:
        # did user close the window?
        # monitor user's event using event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # fill the screen with background color
        screen.fill(game_settings.bg_color)

        # draw the ship to screen
        ship.blitme()

        # update the screen
        pygame.display.flip()

run_game()