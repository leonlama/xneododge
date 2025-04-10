import arcade
import random
from src.entities.enemies.base_enemy import BaseEnemy
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT

class WandererEnemy(BaseEnemy):
    def __init__(self, x, y):
        super().__init__("assets/enemies/wanderer.png", x, y, speed=1.5, scale=0.035)
        self.change_x = random.choice([-2, 2])
        self.change_y = random.choice([-2, 2])

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left <= 0 or self.right >= SCREEN_WIDTH:
            self.change_x *= -1
        if self.bottom <= 0 or self.top >= SCREEN_HEIGHT:
            self.change_y *= -1
