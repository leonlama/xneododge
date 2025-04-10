import arcade
from src.config import PLAYER_SCALE, PLAYER_SPRITE_PATH

class Player(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__(PLAYER_SPRITE_PATH, PLAYER_SCALE)
        self.center_x = x
        self.center_y = y
        self.target_x = x
        self.target_y = y
        self.easing = 0.15  # How fast the player moves toward the mouse

    def update_movement(self):
        # Smooth lerping to target position
        self.center_x += (self.target_x - self.center_x) * self.easing
        self.center_y += (self.target_y - self.center_y) * self.easing

    def set_target(self, x, y):
        self.target_x = x
        self.target_y = y