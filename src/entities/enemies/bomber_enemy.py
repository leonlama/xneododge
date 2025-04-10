import arcade
import random
from src.entities.enemies.base_enemy import BaseEnemy

class BomberEnemy(BaseEnemy):
    def __init__(self, x, y, player):
        super().__init__("assets/enemies/bomber.png", x, y, speed=0.5, scale=0.035)
        self.player = player
        self.explode_range = 60
        self.change_x = random.choice([-1, 1])
        self.change_y = random.choice([-1, 1])
        self.has_exploded = False

    def update(self):
        self.center_x += self.change_x * 0.5
        self.center_y += self.change_y * 0.5

        if arcade.get_distance_between_sprites(self, self.player) < self.explode_range and not self.has_exploded:
            print("💥 Bomber explodes!")
            self.player.take_damage(1)  # or 0.5 if you prefer
            self.has_exploded = True
            self.remove_from_sprite_lists()

    def explode(self):
        print("💥 Bomber explodes!")
        self.remove_from_sprite_lists()
