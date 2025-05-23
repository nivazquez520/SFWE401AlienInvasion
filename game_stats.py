class GameStats:
# Track statistics for Alien Invasion
    def __init__(self, ai_game):
    # Initialize the stats for the game
        self.settings = ai_game.settings
        self.reset_stats()

        #Start the Alien Invasion game in an active state
        self.game_active = True

    def reset_stats(self):
        # Initialize statistics that can change during the game
        self.ships_left = self.settings.ship_limit
        self.aliens_killed = self.settings.kills