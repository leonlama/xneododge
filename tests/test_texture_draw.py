import arcade

class TestWindow(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Test Texture Draw")
        self.sprite_list = arcade.SpriteList()
        sprite = arcade.Sprite("X:/IndieGames/xneododge/assets/hud/hearts/heart.png", scale=0.5)
        sprite.center_x = 400
        sprite.center_y = 300
        self.sprite_list.append(sprite)

    def on_draw(self):
        self.clear()
        self.sprite_list.draw()

if __name__ == "__main__":
    window = TestWindow()
    arcade.run()
