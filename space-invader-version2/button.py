import pygame.font  # render text to screen

class Button():

    def __init__(self, ai_settings, screen, msg):
        # initialize button attributes
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # set dimensions and properties of button
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)     # green
        self.text_color = (255, 255, 255)   # white
        self.font = pygame.font.SysFont(None, 48)   # None mean use default font with size 48

        # build button's rect object and center it on screen
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # button message needs to be prepped only once
        self.prep_msg(msg)

    def prep_msg(self, msg):
        # turn msg into rendered image and center text on button

        # assigning True ti antialiase so that edges of text is smoother
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # draw blank button and draw message
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)




