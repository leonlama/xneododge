import arcade
from src.config import ARTIFACT_SCALE

class DashArtifact(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__("assets/artifacts/dash_artifact.png", scale=ARTIFACT_SCALE)
        self.center_x = x
        self.center_y = y
        self.cooldown = 3.0
        self.time_left = 0.0
        self.artifact_type = "dash"
        self.ghost_sprite = None  # Initialize ghost sprite as None

    def update(self, delta_time: float):
        if self.time_left > 0:
            self.time_left -= delta_time
        elif self.ghost_sprite:
            self.ghost_sprite.remove_from_sprite_lists()  # Remove ghost sprite when cooldown ends
            self.ghost_sprite = None

    def activate(self, player, player_list):
        if self.time_left > 0:
            return False  # Cooldown

        # Check Dash Logic for Zero Direction
        dx = player.change_x
        dy = player.change_y

        # Prevent dash if no movement input
        if dx == 0 and dy == 0:
            print("No movement input, dash skipped.")
            return False

        # Trigger dash
        player.dash()

        # Spawn ghost sprite (optional visual effect)
        if not self.ghost_sprite:
            self.ghost_sprite = arcade.Sprite("assets/artifacts/ghost_effect.png", scale=ARTIFACT_SCALE)
            self.ghost_sprite.center_x = player.center_x
            self.ghost_sprite.center_y = player.center_y
            player_list.append(self.ghost_sprite)

        self.time_left = self.cooldown
        print("Player dashed!")
        return True
