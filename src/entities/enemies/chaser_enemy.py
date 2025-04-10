from src.entities.enemies.base_enemy import BaseEnemy
import arcade

class ChaserEnemy(BaseEnemy):
    def __init__(self, x, y, player):
        super().__init__("assets/enemies/chaser.png", x, y, speed=2.0)
        self.player = player

    def update(self):
        dx = self.player.center_x - self.center_x
        dy = self.player.center_y - self.center_y
        length = (dx**2 + dy**2) ** 0.5
        if length > 0:
            self.center_x += self.speed * dx / length
            self.center_y += self.speed * dy / length
