import arcade
from src.views.game_view import GameView
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT

class StartView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.DARK_SLATE_BLUE)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Click any key to start!", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.WHITE, font_size=20, anchor_x="center")

    def on_key_press(self, key, modifiers):
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)