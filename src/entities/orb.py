import arcade
from src.config import ORB_SCALE

class Orb(arcade.Sprite):
    def __init__(self, orb_type: str, x: float, y: float, texture: arcade.Texture):
        super().__init__(texture, scale=ORB_SCALE)
        self.center_x = x
        self.center_y = y
        self.orb_type = orb_type
