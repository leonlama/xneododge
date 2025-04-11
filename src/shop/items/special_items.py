from src.shop.items.base import BaseShopItem

class ShopResetChip(BaseShopItem):
    def __init__(self):
        super().__init__("Shop Reset Chip", "Refresh shop items instantly", 40, "uncommon")

    def apply_effect(self, player, game_view):
        game_view.shop_view.refresh_items()

class LuckyDraw(BaseShopItem):
    def __init__(self):
        super().__init__("Lucky Draw", "Get 1 random item for free", 60, "uncommon")

    def apply_effect(self, player, game_view):
        import random
        random.choice(game_view.shop_view.items).apply_effect(player, game_view)

class MysteryBox(BaseShopItem):
    def __init__(self):
        super().__init__("Mystery Box", "50% legendary item or nothing", 75, "rare")

    def apply_effect(self, player, game_view):
        import random
        if random.random() < 0.5:
            player.gold_hearts += 2
        else:
            game_view.display_popup("Mystery Box was empty!")