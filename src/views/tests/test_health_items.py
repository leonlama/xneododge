import arcade
from src.entities.player import Player

SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720

class HealthItemTestView(arcade.View):
    def __init__(self):
        super().__init__()
        self.player = Player(200, 200)
        self.ui_text = arcade.Text("Press 1-5 to apply test items", 20, SCREEN_HEIGHT - 30, arcade.color.WHITE, 16)

    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        self.player.draw_hearts()  # Call the new draw_hearts method from Player
        self.ui_text.draw()

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.KEY_1:
            self.player.add_red_heart()  # Corrected method to add a red heart
        elif symbol == arcade.key.KEY_2:
            self.player.add_gray_slot()  # Corrected method to add a gray heart slot
        elif symbol == arcade.key.KEY_3:
            self.player.add_gold_heart()  # Corrected method to add a golden heart
        elif symbol == arcade.key.KEY_4:
            self.player.add_gray_slot()
            # Assuming activate_shield is a method to be implemented
            # self.player.activate_shield()  # Uncomment if activate_shield is implemented
        elif symbol == arcade.key.KEY_5:
            self.player.max_heart_slots = max(1, self.player.max_heart_slots - 1)
            self.player.add_gold_heart()
            self.player.add_gold_heart()

    def on_update(self, delta_time: float):
        self.player.update(delta_time)  # Corrected method name to update
