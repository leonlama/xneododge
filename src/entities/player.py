import arcade
import math
from src.config import PLAYER_SCALE, PLAYER_SPRITE_PATH, PLAYER_SPEED
from src.systems.status_effects import StatusEffectManager

class Player(arcade.Sprite):
    def __init__(self, x, y, window=None):
        super().__init__(PLAYER_SPRITE_PATH, PLAYER_SCALE)
        self.window = window  # 💡 Store window reference here
        self.center_x = x
        self.center_y = y
        self.target_x = x
        self.target_y = y
        self.change_x = 0
        self.change_y = 0
        self.last_dx = 0
        self.last_dy = 0
        self.speed = PLAYER_SPEED
        self.score_multiplier = 1.0
        self.artifact_cooldown_multiplier = 1.0
        self.has_shield = False
        self.max_hearts = 3      # Default max hearts (can be increased with artifacts later)
        self.current_hearts = 3  # Starting health
        self.gold_hearts = 0
        self.score = 0           # Starting score
        self.coin_count = 0
        self.status_effects = StatusEffectManager(self)

    def update(self, delta_time: float = 1/60):
        self.update_movement(delta_time)

    def update_movement(self, delta_time: float):
        dx = self.target_x - self.center_x
        dy = self.target_y - self.center_y
        distance = math.hypot(dx, dy)

        if distance > 1:
            dx /= distance
            dy /= distance
            self.center_x += dx * self.speed * delta_time
            self.center_y += dy * self.speed * delta_time
            self.last_dx = dx
            self.last_dy = dy
        else:
            self.change_x = 0
            self.change_y = 0

    def set_target(self, x, y):
        self.target_x = x
        self.target_y = y
        # Calculate and store direction as change_x and change_y
        dx = self.target_x - self.center_x
        dy = self.target_y - self.center_y
        distance = math.hypot(dx, dy)
        if distance > 0:
            self.change_x = dx / distance
            self.change_y = dy / distance
        else:
            self.change_x = 0
            self.change_y = 0
       
    def dash(self, distance=150):
        dx, dy = self.last_dx, self.last_dy
        if dx == 0 and dy == 0:
            return  # No direction

        # Dash target
        dash_x = self.center_x + dx * distance
        dash_y = self.center_y + dy * distance

        # Clamp inside screen
        dash_x = max(0, min(dash_x, self.window.width))
        dash_y = max(0, min(dash_y, self.window.height))

        # Set current and target position
        self.center_x = dash_x
        self.center_y = dash_y
        self.target_x = dash_x
        self.target_y = dash_y

        print("Dashing!")
        
    def apply_orb_effect(self, effect_name: str):
        self.status_effects.apply_effect(effect_name)
