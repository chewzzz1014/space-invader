import pygame
from setting import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button

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

    # make the Pay buttin
    play_button = Button(game_settings, screen, "Play")

    # set caption of the window
    pygame.display.set_caption("Alien Invasion")

    # instance for storing game statistics
    stats = GameStats(game_settings)

    # create the fleet of aliens
    gf.create_fleet(game_settings, screen, ship, aliens)

    while True:
        # use method from game_functions.py
        # check what had user inputted
        gf.check_events(game_settings, screen, stats, play_button, ship, bullets)

        if stats.game_active:
            ship.update()

            # update bullets
            gf.update_bullets(game_settings, screen, ship, aliens, bullets)

            # update aliens
            gf.update_aliens(game_settings, stats, screen, ship, aliens, bullets)

        # update screen
        gf.update_screen(game_settings, screen, stats, ship, aliens, bullets,play_button)

run_game()