import arcade
import random
from src.entities.enemies.base_enemy import BaseEnemy

class BomberEnemy(BaseEnemy):
    def __init__(self, x, y, player):
        super().__init__("assets/enemies/bomber.png", x, y, player, speed=0.5, scale=0.035)
        self.explode_range = 60
        self.player = player  # Ensure player is assigned
        self.explode_sound = arcade.load_sound("assets/sounds/explode.wav")  # Load explode sound
        self.has_exploded = False

    def update(self):
        # Move randomly or stay idle (custom logic)
        self.center_x += random.choice([-1, 0, 1])
        self.center_y += random.choice([-1, 0, 1])

        # Check if close enough to explode
        if self.distance_to(self.player) < self.explode_range and not self.has_exploded:
            print("💥 Bomber explodes!")
            self.player.take_damage(1.0)  # Deal 1 full heart
            arcade.play_sound(self.explode_sound)
            self.has_exploded = True
            self.kill()  # Ensure self.kill() removes the bomber

    def distance_to(self, target):
        return arcade.get_distance_between_sprites(self, target)
