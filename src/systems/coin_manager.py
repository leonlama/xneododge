import arcade

class CoinManager:
    def __init__(self, player, coin_list):
        self.player = player
        self.coin_list = coin_list  # This was missing!
        self.coin_collect_sound = arcade.load_sound("assets/sounds/coin_collect.flac")

    @property
    def coins(self):
        return self.player.coin_count

    def check_collision(self, player):
        for coin in arcade.check_for_collision_with_list(player, self.coin_list):
            self.player.collect_coin()
            coin.remove_from_sprite_lists()
            arcade.play_sound(self.coin_collect_sound)
