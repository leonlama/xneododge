from src.shop.items.base import BaseShopItem

class HeartSnack(BaseShopItem):
    def __init__(self):
        super().__init__("Heart Snack", "Restore 1 red heart.", 25, rarity="common")

    def apply_effect(self, player, game_view):
        player.heal(1)

class EmptyShell(BaseShopItem):
    def __init__(self):
        super().__init__("Empty Shell", "Gain 1 max gray heart slot.", 30, rarity="common")

    def apply_effect(self, player, game_view):
        player.max_gray_hearts += 1

class GoldenKernel(BaseShopItem):
    def __init__(self):
        super().__init__("Golden Kernel", "Gain 1 golden heart (overheal).", 40, rarity="uncommon")

    def apply_effect(self, player, game_view):
        player.add_golden_heart()
