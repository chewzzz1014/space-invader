import pygame

class Ship():
    def __init__(self, screen):
        self.screen = screen

        # load image and get its rect
        self.image = pygame.image.load("images/space-invaders.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # the starting position of the ship: center bottom of the surface
        # every game element in pygame is treated as rect (rectangular)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False

    # display the image of ship
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1