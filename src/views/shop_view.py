import arcade
import random
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT, FONT_NAME
from src.shop.items.item_registry import ALL_ITEMS
from src.systems.star import StarManager


class ShopView(arcade.View):
    def __init__(self, player, coin_manager, return_callback):
        super().__init__()
        self.player = player
        self.coin_manager = coin_manager
        self.return_callback = return_callback
        self.star_list = arcade.SpriteList()
        self.selected_items = random.sample(ALL_ITEMS, 3)  # Pick 3 random items
        self.selected_index = None

    def on_show(self):
        self.star_list = arcade.SpriteList()
        self.selected_index = None

    def on_draw(self):
        self.clear()
        self.star_list.draw()

        # Title
        arcade.draw_text("- NEO SHOP - ", SCREEN_WIDTH / 2, SCREEN_HEIGHT - 80,
                         arcade.color.YELLOW, 42, anchor_x="center", font_name=FONT_NAME)

        arcade.draw_text("CHOOSE YOUR BLESSIN´", SCREEN_WIDTH / 2, SCREEN_HEIGHT - 120,
                         arcade.color.ORANGE, 26, anchor_x="center", font_name=FONT_NAME)

        # Draw item boxes
        start_x = 150
        y = 300
        spacing = 250

        for index, item in enumerate(self.selected_items):
            x = start_x + index * spacing

            # Box using lrtb_rectangle_filled
            top = y + 110
            bottom = y - 110
            left = x - 100
            right = x + 100
            arcade.draw_lrbt_rectangle_filled(left, right, bottom, top, arcade.color.DARK_BLUE)
            arcade.draw_lrbt_rectangle_outline(left, right, bottom, top, arcade.color.WHITE, 2)

            # Title
            arcade.draw_text(item.name, x, y + 80, arcade.color.YELLOW, 16, width=180, align="center", anchor_x="center")

            # Description
            arcade.draw_text(item.description, x, y + 40, arcade.color.LIGHT_GRAY, 12,
                             width=180, align="center", anchor_x="center")

            # Cost
            arcade.draw_text(f"💰 {item.cost} coins", x, y - 60, arcade.color.GOLD, 14,
                             anchor_x="center")

        # Bottom instructions
        arcade.draw_text(f"Coins: {self.coin_manager.coins}", 20, 20,
                         arcade.color.GOLD, 18, font_name=FONT_NAME)
        arcade.draw_text("Press [1] [2] [3] to buy, [Esc] to skip", SCREEN_WIDTH / 2, 20,
                         arcade.color.GRAY, 14, anchor_x="center", font_name=FONT_NAME)

    def on_update(self, delta_time):
        self.star_list.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            self.return_to_game()
        elif key in (arcade.key.KEY_1, arcade.key.KEY_2, arcade.key.KEY_3):
            index = key - arcade.key.KEY_1
            if index < len(self.selected_items):
                self.selected_index = index
                item = self.selected_items[index]
                if self.coin_manager.coins >= item.cost:
                    self.coin_manager.coins -= item.cost
                    item.apply(self.player)
                    print(f"✅ Bought: {item.name}")
                    self.return_to_game()
                else:
                    print("❌ Not enough coins!")

    def return_to_game(self):
        self.return_callback()
