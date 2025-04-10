import arcade

class CoinManager:
    def __init__(self, coin_list):
        self.coin_list = coin_list
        self.coin_collect_sound = arcade.load_sound("assets/sounds/coin_collect.flac")

    def check_collision(self, player):
        for coin in arcade.check_for_collision_with_list(player, self.coin_list):
            player.coin_count += 1
            coin.remove_from_sprite_lists()
            arcade.play_sound(self.coin_collect_sound)
