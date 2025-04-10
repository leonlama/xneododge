import arcade
import random
from src.entities.enemies.base_enemy import BaseEnemy
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT
from src.entities.enemies.bullets.enemy_bullet import EnemyBullet

class ShooterEnemy(BaseEnemy):
    def __init__(self, x, y, player, bullet_list):
        super().__init__("assets/enemies/shooter.png", x, y, player, speed=1.5, scale=0.035)
        self.shoot_timer = 0
        self.change_x = random.choice([-1, 1])
        self.change_y = random.choice([-1, 1])
        self.bullet_list = bullet_list

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left <= 0 or self.right >= SCREEN_WIDTH:
            self.change_x *= -1
        if self.bottom <= 0 or self.top >= SCREEN_HEIGHT:
            self.change_y *= -1

        self.shoot_timer += 1
        if self.shoot_timer % 120 == 0:
            self.shoot()

    def shoot(self):
        print("ShooterEnemy shoots towards player!")
        bullet = EnemyBullet(self.center_x, self.center_y, self.player.center_x, self.player.center_y)
        self.bullet_list.append(bullet)
