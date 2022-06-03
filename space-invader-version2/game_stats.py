class GameStats():
    # track statistics for Alien Invasion

    def __init__(self, ai_settings):
        # initialize statistics
        self.ai_settings = ai_settings
        self.reset_stats()

        # starts the game in active state
        self.game_active = True

    def reset_stats(self):
        # initialize changeable statistics
        self.ships_left = self.ai_settings.ship_limit