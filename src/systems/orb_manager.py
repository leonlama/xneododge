import arcade
import random
import time
from src.entities.orb import Orb
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT, ORB_SCALES, ORB_COMBO_WINDOW, ORB_COMBO_SCORE

ORB_TYPES = {
    "speed": "assets/orbs/speed_orb.png",
    "multiplier": "assets/orbs/multiplier_orb.png",
    "cooldown": "assets/orbs/cooldown_orb.png",
    "shield": "assets/orbs/shield_orb.png",
    # Removed heart orbs from the spawn pool
}

class OrbManager:
    def __init__(self):
        self.orb_list = arcade.SpriteList()
        self.orb_textures = {}
        for orb_type, texture_path in ORB_TYPES.items():
            self.orb_textures[orb_type] = arcade.load_texture(texture_path)
        self.orb_collect_sound = arcade.load_sound("assets/sounds/orb_collect.wav")

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
        """Handle orb pickups, apply effects, and track combo bonuses."""
        hit_list = arcade.check_for_collision_with_list(player, self.orb_list)
        current_time = time.time()
        # Initialize combo tracking attributes if missing
        if not hasattr(self, 'last_orb_time'):
            self.last_orb_time = 0
            self.combo_count = 0
        for orb in hit_list:
            # Combo logic: reset or increment based on time window
            if current_time - self.last_orb_time <= ORB_COMBO_WINDOW:
                self.combo_count += 1
            else:
                self.combo_count = 1
            self.last_orb_time = current_time
            # Award combo bonus (beyond the first orb in a combo)
            if self.combo_count > 1:
                combo_bonus = ORB_COMBO_SCORE * (self.combo_count - 1) * player.score_multiplier
                player.score += combo_bonus
                print(f"🔥 Orb combo x{self.combo_count}! +{int(combo_bonus)} points")
            # Apply the orb's primary effect
            orb.apply_effect(player)
            arcade.play_sound(self.orb_collect_sound)
            orb.remove_from_sprite_lists()
