import pygame
from setting import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # initialization
    pygame.init()

    # instance of class settings
    # so that we can modify the settings of the game easily
    game_settings = Settings()

    # create window screen (surface). Width is 1200 and height is 800
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))

    # make a ship
    ship = Ship(game_settings, screen)

    # set caption of the window
    pygame.display.set_caption("Alien Invasion")

    while True:
        # use method from game_functions.py
        # check what had user inputted
        gf.check_events(ship)

        ship.update()
        # update screen
        gf.update_screen(game_settings, screen, ship)

run_game()