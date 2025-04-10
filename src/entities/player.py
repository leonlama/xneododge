import arcade
import math
from src.config import PLAYER_SCALE, PLAYER_SPRITE_PATH, PLAYER_SPEED

class Player(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__(PLAYER_SPRITE_PATH, PLAYER_SCALE)
        self.center_x = x
        self.center_y = y
        self.target_x = x
        self.target_y = y

    def update_movement(self, delta_time: float):
        dx = self.target_x - self.center_x
        dy = self.target_y - self.center_y
        distance = math.hypot(dx, dy)

        if distance > 1:
            angle = math.atan2(dy, dx)
            move_x = PLAYER_SPEED * delta_time * math.cos(angle)
            move_y = PLAYER_SPEED * delta_time * math.sin(angle)

            # Avoid overshooting
            if abs(move_x) > abs(dx):
                move_x = dx
            if abs(move_y) > abs(dy):
                move_y = dy

            self.center_x += move_x
            self.center_y += move_y

    def set_target(self, x, y):
        self.target_x = x
        self.target_y = y
