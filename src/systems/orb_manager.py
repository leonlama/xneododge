import arcade
import random
from src.entities.orb import Orb
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT

class OrbManager:
    def __init__(self):
        self.orb_list = arcade.SpriteList()
        self.orb_textures = {
            "speed": arcade.load_texture("assets/orbs/speed_orb.png"),
            "multiplier": arcade.load_texture("assets/orbs/multiplier_orb.png"),
            "cooldown": arcade.load_texture("assets/orbs/cooldown_orb.png"),
            "shield": arcade.load_texture("assets/orbs/shield_orb.png")
        }

    def spawn_orb(self):
        orb_type = random.choice(list(self.orb_textures.keys()))
        x = random.randint(50, SCREEN_WIDTH - 50)
        y = random.randint(50, SCREEN_HEIGHT - 50)
        texture = self.orb_textures[orb_type]
        orb = Orb(orb_type, x, y, texture)
        self.orb_list.append(orb)

    def update(self, delta_time):
        self.orb_list.update()

    def draw(self):
        self.orb_list.draw()

    def check_collisions(self, player, apply_effect_fn):
        hit_list = arcade.check_for_collision_with_list(player, self.orb_list)
        for orb in hit_list:
            apply_effect_fn(orb.orb_type)
            orb.remove_from_sprite_lists()
