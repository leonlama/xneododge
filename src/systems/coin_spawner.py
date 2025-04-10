import arcade
import random
from src.entities.coin import Coin
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT

class CoinSpawner:
    def __init__(self, coin_list):
        self.coin_list = coin_list
        self.spawn_timer = 0

    def update(self, delta_time: float):
        self.spawn_timer += delta_time
        if self.spawn_timer > 5:  # spawn every 5s
            x = random.randint(32, SCREEN_WIDTH - 32)
            y = random.randint(32, SCREEN_HEIGHT - 32)
            coin = Coin()
            coin.center_x = x
            coin.center_y = y
            self.coin_list.append(coin)
            self.spawn_timer = 0
