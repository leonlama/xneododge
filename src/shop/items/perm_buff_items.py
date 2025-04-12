from src.shop.items.base import BaseShopItem

class CDRCore(BaseShopItem):
    def __init__(self):
        super().__init__(
            "CDR Core",
            "-10% Artifact Cooldown permanently",
            price=60,
            rarity="uncommon"
        )

    def apply_effect(self, player, game_view):
        player.permanent_effects["cooldown_reduction"] = player.permanent_effects.get("cooldown_reduction", 0) + 0.10


class MMSChip(BaseShopItem):
    def __init__(self):
        super().__init__(
            "MMS Chip",
            "+15% Movement Speed permanently",
            price=60,
            rarity="uncommon"
        )

    def apply_effect(self, player, game_view):
        player.permanent_effects["movement_speed"] = player.permanent_effects.get("movement_speed", 0) + 0.15


class SpawnBooster(BaseShopItem):
    def __init__(self):
        super().__init__(
            "Spawn Booster",
            "+10% Orb Spawn Chance permanently",
            price=50,
            rarity="uncommon"
        )

    def apply_effect(self, player, game_view):
        player.permanent_effects["orb_spawn_chance"] = player.permanent_effects.get("orb_spawn_chance", 0) + 0.10


class GoldTooth(BaseShopItem):
    def __init__(self):
        super().__init__(
            "Gold Tooth",
            "+10% Coin Drop Chance permanently",
            price=50,
            rarity="uncommon"
        )

    def apply_effect(self, player, game_view):
        player.permanent_effects["coin_drop_chance"] = player.permanent_effects.get("coin_drop_chance", 0) + 0.10


class AbsorptionModule(BaseShopItem):
    def __init__(self):
        super().__init__(
            "Absorption Module",
            "10% chance to ignore damage entirely",
            price=80,
            rarity="rare"
        )

    def apply_effect(self, player, game_view):
        player.permanent_effects["absorb_chance"] = player.permanent_effects.get("absorb_chance", 0) + 0.10
