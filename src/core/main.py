import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "XNeododge"

class XNeododge(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        self.clear()
        arcade.draw_text("XNeododge Starting...", 200, 300, arcade.color.WHITE, 20)

def main():
    window = XNeododge()
    arcade.run()

if __name__ == "__main__":
    main()
