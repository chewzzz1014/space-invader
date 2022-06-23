class GameStats():
    # track statistics for Alien Invasion

    def __init__(self, ai_settings):
        # initialize statistics
        self.ai_settings = ai_settings
        self.reset_stats()

        # starts game in inactive state
        self.game_active = False

        # starts the game in active state
        self.game_active = True

        # high score should never be reset
        self.high_score = 0

    def reset_stats(self):
        # initialize changeable statistics
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1