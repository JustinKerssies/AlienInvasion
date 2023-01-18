import os


ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__)))


class GameStats():
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_settings):
        """Initialize statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start Alien Invasion in an inactive state
        self.game_active = False

        # High score should never be reset.
        filename = os.path.join(ROOT_DIR, 'Documents', 'high_scores.txt')
        with open(filename) as file_object:
            contents = file_object.read()
        self.high_score = int(contents)

    def reset_stats(self):
        """Initialize statisticsthat can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
