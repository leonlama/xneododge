import arcade
import arcade.gui
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, FONT_PATH, FONT_NAME, TITLE_MUSIC_PATH, VERSION
from src.views.game_view import GameView
from src.systems.star import StarManager

class StartView(arcade.View):
    def __init__(self):
        super().__init__()
        self.star_manager = StarManager()
        self.music_player = None
        self.ui_manager = arcade.gui.UIManager()
        self.ui_manager.enable()
        # Load font manually
        arcade.load_font(FONT_PATH)
        self.font_name = FONT_NAME

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_show_view(self):
        # Play title music
        self.title_music = arcade.load_sound(TITLE_MUSIC_PATH)
        self.music_player = arcade.play_sound(self.title_music, volume=0.45, loop=True)

    def on_draw(self):
        self.clear()
        self.star_manager.draw()

        # Title
        arcade.draw_text(
            "NEODODGE", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 100,
            arcade.color.WHITE, font_size=36, anchor_x="center", font_name=self.font_name
        )

        # Button prompt
        arcade.draw_text(
            "Click to Start", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 40,
            arcade.color.LIGHT_GRAY, font_size=18, anchor_x="center", font_name=self.font_name
        )

        # Controls
        arcade.draw_text(
            "Controls: Mouse to move, Space to dash", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 20,
            arcade.color.GRAY, font_size=14, anchor_x="center", font_name=self.font_name
        )

        # Footer
        arcade.draw_text(
            VERSION, SCREEN_WIDTH - 10, 10,
            arcade.color.GRAY, font_size=12, anchor_x="right", font_name=self.font_name
        )

    def on_update(self, delta_time: float):
        self.star_manager.update(delta_time)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        self.switch_to_game()

    def on_key_press(self, key: int, modifiers: int):
        self.switch_to_game()

    def switch_to_game(self):
        if self.music_player:
            self.music_player.pause()
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)