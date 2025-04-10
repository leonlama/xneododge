import arcade
import random
from src.entities.orb import Orb
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT, ORB_SCALES

ORB_TYPES = {
    "speed": "assets/orbs/speed_orb.png",
    "multiplier": "assets/orbs/multiplier_orb.png",
    "cooldown": "assets/orbs/cooldown_orb.png",
    "shield": "assets/orbs/shield_orb.png",
    "red_heart": "assets/orbs/red_heart_orb.png",
    "gray_heart": "assets/orbs/gray_heart_orb.png",
    "golden_heart": "assets/orbs/golden_heart_orb.png",
}

class OrbManager:
    def __init__(self):
        self.orb_list = arcade.SpriteList()
        self.orb_textures = {}
        for orb_type, texture_path in ORB_TYPES.items():
            self.orb_textures[orb_type] = arcade.load_texture(texture_path)

    def spawn_orb(self):
        # Random spawn from all orb types
        orb_type = random.choice(list(ORB_TYPES.keys()))
        
        # For testing specific orbs, uncomment the line below and comment out the random choice above
        # orb_type = "golden_heart"  # swap with others for testing visuals
        
        x = random.randint(50, SCREEN_WIDTH - 50)
        y = random.randint(50, SCREEN_HEIGHT - 50)
        texture = self.orb_textures[orb_type]
        scale = ORB_SCALES.get(orb_type, 0.6)  # fallback to 0.6 if missing
        orb = Orb(orb_type, x, y, texture, scale=scale)
        self.orb_list.append(orb)

    def update(self, delta_time):
        self.orb_list.update()

    def draw(self):
        self.orb_list.draw()

    def check_collisions(self, player, apply_effect_fn):
        hit_list = arcade.check_for_collision_with_list(player, self.orb_list)
        for orb in hit_list:
            orb.apply_effect(player)
            orb.remove_from_sprite_lists()
