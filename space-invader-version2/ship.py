import pygame
from setting import Settings

class Ship():
    def __init__(self,ai_settings, screen):
        self.screen = screen
        self.ai_settings = Settings()

        # load image and get its rect
        self.image = pygame.image.load("images/space-invaders.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # the starting position of the ship: center bottom of the surface
        # every game element in pygame is treated as rect (rectangular)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # store a decimal value for the ship's center
        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    # display the image of ship
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):

        # update the ship's center value
        # make sure that the ship wiil not go beyond the edge
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center