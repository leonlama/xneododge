from src.shop.items.base import BaseShopItem
import random

class ShopResetChip(BaseShopItem):
    def __init__(self):
        super().__init__("Shop Reset Chip", "Refresh shop items instantly", 40, "uncommon")

    def apply_effect(self, player, game_view, shop_items=None):
        game_view.shop_view.refresh_items()

class LuckyDraw(BaseShopItem):
    def __init__(self):
        super().__init__("Lucky Draw", "Get 1 random item for free", 60, "uncommon")

    def apply_effect(self, player, game_view, shop_items=None):
        if not shop_items:
            return
        random_item = random.choice(shop_items)
        random_item.apply_effect(player, game_view)
        game_view.player.active_items.append((random_item, None))

class MysteryBox(BaseShopItem):
    def __init__(self):
        super().__init__("Mystery Box", "50% legendary item or nothing", 75, "rare")

    def apply_effect(self, player, game_view, shop_items=None):
        if random.random() < 0.5:
            player.gold_hearts += 2
        else:
            game_view.display_popup("Mystery Box was empty!")