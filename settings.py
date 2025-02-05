class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (200, 175, 240)

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3
        self.kills = 0

        # Bullet settings - dark grey bullets that a re 3 pixels wide and 15
        # pixels high. Bullets travel slower than the ship.
        self.bullet_speed = 1.5
        self.bullet_width = 1
        self.bullet_height = 15
        self.bullet_color = (155, 135, 12)
        self.bullets_allowed = 3

        # alien settings
        self.alien_speed = 3.0
        self.fleet_drop_speed = 10

        # fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
