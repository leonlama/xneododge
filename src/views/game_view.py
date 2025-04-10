import arcade
from src.entities.player import Player
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT

class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.player = None
        self.player_list = None
        self.mouse_held = False

    def setup(self):
        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player)

    def on_draw(self):
        self.clear()
        self.player_list.draw()

    def on_update(self, delta_time: float):
        self.player.update_movement(delta_time)
        self.player_list.update()
        self.player_list.update_animation()

    def on_mouse_motion(self, x, y, dx, dy):
        if self.mouse_held:
            self.player.set_target(x, y)

    def on_mouse_press(self, x, y, button, modifiers):
        self.mouse_held = True
        self.player.set_target(x, y)

    def on_mouse_release(self, x, y, button, modifiers):
        self.mouse_held = False