import arcade
import math

class EnemyBullet(arcade.Sprite):
    def __init__(self, x, y, target_x, target_y):
        super().__init__("assets/bullets/enemy_bullet.png", scale=0.02)

        self.center_x = x
        self.center_y = y

        # Compute angle to target
        x_diff = target_x - x
        y_diff = target_y - y
        angle = math.atan2(y_diff, x_diff)

        speed = 300.0
        self.change_x = math.cos(angle) * speed
        self.change_y = math.sin(angle) * speed

    def update(self, delta_time: float = 0.016):  # Accept delta_time
        self.center_x += self.change_x * delta_time
        self.center_y += self.change_y * delta_time

        # Optional: remove if off-screen
        if self.right < 0 or self.left > 800 or self.top < 0 or self.bottom > 600:
            self.remove_from_sprite_lists()
