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
        self.player = player
        self.enemy_types = {
            "chaser": ChaserEnemy,
            "wanderer": WandererEnemy,
            "shooter": ShooterEnemy,
            "bomber": BomberEnemy
        }
        self.bullet_list = arcade.SpriteList()  # Initialize bullet list for shooter enemies

    def update(self, delta_time):
        for enemy in self.enemy_list:
            enemy.update()

    def draw(self):
        self.enemy_list.draw()

    def spawn_from_recipe(self, recipe: dict):
        for enemy_type, count in recipe.items():
            for _ in range(count):
                self.spawn_enemy(enemy_type)

    def spawn_wave(self, recipe: dict):
        for enemy_type, count in recipe.items():
            for _ in range(count):
                self.spawn_enemy(enemy_type)

    def spawn_enemy(self, enemy_type: str):
        max_attempts = 10
        for _ in range(max_attempts):
            x = random.randint(50, SCREEN_WIDTH - 50)
            y = random.randint(50, SCREEN_HEIGHT - 50)

            if not any(arcade.get_distance_between_sprites(enemy, arcade.Sprite(center_x=x, center_y=y)) < 50 for enemy in self.enemy_list):
                break  # Found a valid spot

        enemy_class_map = {
            "chaser": ChaserEnemy,
            "wanderer": WandererEnemy,
            "shooter": ShooterEnemy,
            "bomber": BomberEnemy
        }

        enemy_cls = enemy_class_map.get(enemy_type)
        if not enemy_cls:
            print(f"[ERROR] Unknown enemy type: {enemy_type}")
            return

        if enemy_type == "shooter":
            enemy = enemy_cls(x, y, self.player, self.bullet_list)
        else:
            enemy = enemy_cls(x, y, self.player)
        
        self.enemy_list.append(enemy)
        print(f"[SPAWN] {enemy_type} at ({x},{y})")

    def check_collisions(self, player):
        for enemy in self.enemy_list:
            if arcade.check_for_collision(player, enemy):
                if isinstance(enemy, BomberEnemy):
                    enemy.explode()
                else:
                    player.take_damage(1.0)  # For melee enemies

    def check_bullet_collisions(self, player):
        hit_list = arcade.check_for_collision_with_list(player, self.bullet_list)
        for bullet in hit_list:
            player.take_damage(0.5)
            bullet.remove_from_sprite_lists()

    def trim_enemies_for_new_wave(self):
        """Keep 1–3 random enemies, remove the rest before the new wave spawns."""
        keep_count = random.randint(1, 3)
        if len(self.enemy_list) > keep_count:
            # Shuffle and keep the first `keep_count`, remove the rest
            enemies = self.enemy_list[:]
            random.shuffle(enemies)
            to_keep = enemies[:keep_count]
            to_remove = enemies[keep_count:]

            for enemy in to_remove:
                enemy.remove_from_sprite_lists()

            print(f"[ENEMY MANAGER] Trimmed enemies: Kept {len(to_keep)}, removed {len(to_remove)}")