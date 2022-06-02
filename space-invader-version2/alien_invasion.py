import pygame
from setting import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien

def run_game():
    # initialization
    pygame.init()

    # instance of class settings
    # so that we can modify the settings of the game easily
    game_settings = Settings()

    # create window screen (surface). Width is 1200 and height is 800
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))

    alien = Alien(game_settings, screen)

    # make ship, bullets group and aliens group
    ship = Ship(game_settings, screen)
    bullets = Group()
    aliens = Group()

    # set caption of the window
    pygame.display.set_caption("Alien Invasion")

    # create the fleet of aliens
    gf.create_fleet(game_settings, screen, ship, aliens)

    while True:
        # use method from game_functions.py
        # check what had user inputted
        gf.check_events(game_settings, screen, ship, bullets)
        ship.update()

        # update bullets
        gf.update_bullets(bullets)

        # update aliens
        gf.update_aliens(aliens)

        # update screen
        gf.update_screen(game_settings, screen, ship, aliens, bullets)

run_game()