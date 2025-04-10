import arcade
from src.entities.player import Player

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "XNeododge"

class XNeododge(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.player = None
        self.keys = {}

    def setup(self):
        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    def on_draw(self):
        self.clear()
        self.player.draw()

    def on_update(self, delta_time):
        self.player.update_movement(self.keys)

    def on_key_press(self, key, modifiers):
        self.keys[key] = True

    def on_key_release(self, key, modifiers):
        self.keys[key] = False

def main():
    game = XNeododge()
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()