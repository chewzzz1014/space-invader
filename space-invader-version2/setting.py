# setting class to store all the settings in one place
# pass around one setting object instead of many individual settings

class Settings():
    def __init__(self):
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)