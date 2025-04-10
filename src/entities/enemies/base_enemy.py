import arcade
from src.config import PLAYER_SCALE

class BaseEnemy(arcade.Sprite):
    def __init__(self, texture_path: str, x: float, y: float, speed: float = 2.0, scale: float = PLAYER_SCALE):
        super().__init__(texture_path, scale=scale)
        self.center_x = float(x)
        self.center_y = float(y)
        self.speed = speed

    def update(self, player):
        """Override in subclasses."""
        pass
