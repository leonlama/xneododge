import arcade
import random

from src.entities.enemies.chaser_enemy import ChaserEnemy
from src.entities.enemies.wanderer_enemy import WandererEnemy
from src.entities.enemies.shooter_enemy import ShooterEnemy
from src.entities.enemies.bomber_enemy import BomberEnemy
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT

class EnemyManager:
    def __init__(self, player):
        self.enemy_list = arcade.SpriteList()
        self.spawn_timer = 0
        self.spawn_interval = 5.0  # seconds
        self.player = player

    def update(self, delta_time):
        self.spawn_timer += delta_time
        if self.spawn_timer >= self.spawn_interval:
            self.spawn_random_enemy()
            self.spawn_timer = 0

        for enemy in self.enemy_list:
            enemy.update()

    def draw(self):
        self.enemy_list.draw()

    def spawn_random_enemy(self):
        x = random.randint(100, SCREEN_WIDTH - 100)
        y = random.randint(100, SCREEN_HEIGHT - 100)
        enemy_type = random.choice(["chaser", "wanderer", "shooter", "bomber"])

        print(f"[DEBUG] Spawning enemy at ({x}, {y}) of type {enemy_type}")

        if enemy_type == "chaser":
            enemy = ChaserEnemy(x, y, self.player)
        elif enemy_type == "wanderer":
            enemy = WandererEnemy(x, y)
        elif enemy_type == "shooter":
            enemy = ShooterEnemy(x, y, self.player)
        elif enemy_type == "bomber":
            enemy = BomberEnemy(x, y, self.player)

        self.enemy_list.append(enemy)

    def check_collisions(self, player):
        for enemy in self.enemy_list:
            if arcade.check_for_collision(player, enemy):
                if isinstance(enemy, BomberEnemy):
                    enemy.explode()
                else:
                    print("⚔️ Player takes damage!")