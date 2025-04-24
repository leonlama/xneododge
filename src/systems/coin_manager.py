import arcade
from src.config import COIN_SCORE_VALUE

class CoinManager:
    def __init__(self, player, coin_list):
        self.player = player
        self.coin_list = coin_list  # This was missing!
        self.coin_collect_sound = arcade.load_sound("assets/sounds/coin_collect.flac")

    @property
    def coins(self):
        return self.player.coin_count
        
    @coins.setter
    def coins(self, value):
        self.player.coin_count = max(0, value)  # prevent negative coins

    def check_collision(self, player):
        """Handle player-coin collisions: collect coins and award score."""
        for coin in arcade.check_for_collision_with_list(player, self.coin_list):
            # Increase coin count
            self.player.collect_coin()
            # Award score for coin collection
            self.player.score += COIN_SCORE_VALUE * self.player.score_multiplier
            coin.remove_from_sprite_lists()
            arcade.play_sound(self.coin_collect_sound)
