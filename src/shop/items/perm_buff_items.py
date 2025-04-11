from src.shop.items.base import BaseShopItem

class CDRCore(BaseShopItem):
    def __init__(self):
        super().__init__("CDR Core", "-10% Artifact Cooldown permanently", 60)

    def apply_effect(self, player, game_view):
        player.perma_cdr_bonus += 0.10

class MMSChip(BaseShopItem):
    def __init__(self):
        super().__init__("MMS Chip", "+15% Movement Speed permanently", 60)

    def apply_effect(self, player, game_view):
        player.perma_speed_bonus += 0.15

class SpawnBooster(BaseShopItem):
    def __init__(self):
        super().__init__("Spawn Booster", "+10% orb spawn chance", 50)

    def apply_effect(self, player, game_view):
        game_view.orb_spawn_chance += 0.10

class GoldTooth(BaseShopItem):
    def __init__(self):
        super().__init__("Gold Tooth", "+10% coin drop chance", 50)

    def apply_effect(self, player, game_view):
        player.coin_bonus += 0.10

class AbsorptionModule(BaseShopItem):
    def __init__(self):
        super().__init__("Absorption Module", "10% chance to ignore damage", 70)

    def apply_effect(self, player, game_view):
        player.absorption_chance += 0.10
