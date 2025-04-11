import arcade
import math
import time
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT, FONT_NAME
from src.shop.store_manager import StoreManager
from src.systems.star import StarManager

RARITY_COLORS = {
    "common": arcade.color.LIGHT_GRAY[:3],
    "uncommon": arcade.color.LIGHT_GREEN[:3],
    "rare": arcade.color.LIGHT_BLUE[:3],
    "legendary": arcade.color.GOLD[:3],
}

class ShopView(arcade.View):
    def __init__(self, player, coin_manager, return_callback, current_wave_number):
        super().__init__()
        self.player = player
        self.coin_manager = coin_manager
        self.return_callback = return_callback
        self.current_wave_number = current_wave_number

        # Use StarManager instead of star_list
        self.star_manager = StarManager()

        # Now use store manager
        self.store_manager = StoreManager()
        self.shop_items = self.store_manager.get_items_for_wave(self.current_wave_number)
        self.selected_index = None
        self.hovered_index = None
        self.start_time = time.time()  # Initialize start time for animation

    def on_show(self):
        self.selected_index = None
        self.hovered_index = None

    def on_draw(self):
        self.clear()
        self.star_manager.draw()  # ✨ moving stars background

        # Title
        arcade.draw_text("- NEO SHOP - ", SCREEN_WIDTH / 2, SCREEN_HEIGHT - 80,
                         arcade.color.YELLOW, 42, anchor_x="center", font_name=FONT_NAME)

        arcade.draw_text("CHOOSE YOUR BLESSIN´", SCREEN_WIDTH / 2, SCREEN_HEIGHT - 120,
                         arcade.color.ORANGE, 26, anchor_x="center", font_name=FONT_NAME)

        # Draw item boxes
        start_x = 150
        base_y = 300
        spacing = 250
        elapsed = time.time() - self.start_time

        for index, item in enumerate(self.shop_items):
            x = start_x + index * spacing
            y = base_y + math.sin(elapsed * 2 + index) * 5

            # Determine dimensions
            top = y + 110
            bottom = y - 110
            left = x - 100
            right = x + 100

            # Determine rarity color
            rarity_color = RARITY_COLORS.get(item.rarity, arcade.color.WHITE[:3])

            # Item background
            arcade.draw_lrbt_rectangle_filled(left, right, bottom, top, arcade.color.DARK_BLUE)

            # Glow effect for legendary
            if item.rarity == "legendary":
                glow_alpha = int((math.sin(elapsed * 5) + 1) * 50)
                glow_color = (*rarity_color, glow_alpha)
                for radius in range(115, 125, 2):
                    arcade.draw_circle_outline(x, y, radius, glow_color, 1)

            # Outline
            outline_color = arcade.color.LIGHT_GREEN if index == self.hovered_index else rarity_color
            arcade.draw_lrbt_rectangle_outline(left, right, bottom, top, outline_color, 2)

            # Item title
            arcade.draw_text(item.name, x, y + 90, rarity_color, 18, anchor_x="center", font_name=FONT_NAME)

            # Item description with pulse animation
            alpha = int((math.sin(elapsed * 3 + index) + 1) * 127.5)
            desc_color = (*rarity_color, alpha)
            arcade.draw_text(item.description, x, y + 50, desc_color, 12,
                             width=180, align="center", anchor_x="center", anchor_y="center", font_name=FONT_NAME)

            # Display rarity label
            arcade.draw_text(f"[{item.rarity.upper()}]", x, y - 30, rarity_color, 12, anchor_x="center", font_name=FONT_NAME)

            # Display cost
            arcade.draw_text(f"💰 {item.cost} coins", x, y - 60, arcade.color.GOLD, 14, anchor_x="center", font_name=FONT_NAME)

        # Bottom instructions
        arcade.draw_text(f"Coins: {self.coin_manager.coins}", 20, 20,
                         arcade.color.GOLD, 18, font_name=FONT_NAME)
        arcade.draw_text("Press [1] [2] [3] to buy, [Esc] to skip", SCREEN_WIDTH / 2, 20,
                         arcade.color.GRAY, 14, anchor_x="center", font_name=FONT_NAME)

    def on_update(self, delta_time):
        self.star_manager.update(delta_time)

    def on_mouse_motion(self, x, y, dx, dy):
        start_x = 150
        base_y = 300
        spacing = 250
        self.hovered_index = None
        for index in range(len(self.shop_items)):
            item_x = start_x + index * spacing
            item_y = base_y
            if item_x - 100 < x < item_x + 100 and item_y - 110 < y < item_y + 110:
                self.hovered_index = index
                break

    def on_mouse_press(self, x, y, button, modifiers):
        if self.hovered_index is not None:
            self.selected_index = self.hovered_index
            item = self.shop_items[self.selected_index]
            if self.coin_manager.coins >= item.cost:
                self.coin_manager.coins -= item.cost
                item.apply(self.player)
                print(f"✅ Bought: {item.name}")
                self.return_to_game()
            else:
                print("❌ Not enough coins!")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            self.return_to_game()
        elif key in (arcade.key.KEY_1, arcade.key.KEY_2, arcade.key.KEY_3):
            index = key - arcade.key.KEY_1
            if index < len(self.shop_items):
                self.selected_index = index
                item = self.shop_items[index]
                if self.coin_manager.coins >= item.cost:
                    self.coin_manager.coins -= item.cost
                    item.apply(self.player)
                    print(f"✅ Bought: {item.name}")
                    self.return_to_game()
                else:
                    print("❌ Not enough coins!")

    def return_to_game(self):
        self.return_callback()
