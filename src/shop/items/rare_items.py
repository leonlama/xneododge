from src.shop.items.base import BaseShopItem

class SecondChance(BaseShopItem):
    def __init__(self):
        super().__init__("Second Chance", "Revive once with 2 red hearts", 100)

    def apply_effect(self, player, game_view):
        player.has_revive = True

class GhostDash(BaseShopItem):
    def __init__(self):
        super().__init__("Ghost Dash", "1.5s invincibility after dash", 85)

    def apply_effect(self, player, game_view):
        player.ghost_dash_enabled = True

class VoidArtifact(BaseShopItem):
    def __init__(self):
        super().__init__("Void Artifact", "Orb cooldowns -50% this wave", 90)

    def apply_effect(self, player, game_view):
        player.apply_status_effect("orb_cdr_wave", duration=1, value=0.5)

class ShopResetChip(BaseShopItem):
    def __init__(self):
        super().__init__("Shop Reset Chip", "Refresh shop items instantly", 40)

    def apply_effect(self, player, game_view):
        game_view.shop_view.refresh_items()

class LuckyDraw(BaseShopItem):
    def __init__(self):
        super().__init__("Lucky Draw", "Get 1 random item for free", 60)

    def apply_effect(self, player, game_view):
        import random
        random.choice(game_view.shop_view.items).apply_effect(player, game_view)

class MysteryBox(BaseShopItem):
    def __init__(self):
        super().__init__("Mystery Box", "50% amazing item or nothing", 75)

    def apply_effect(self, player, game_view):
        import random
        if random.random() < 0.5:
            player.gold_hearts += 2
        else:
            game_view.display_popup("Mystery Box was empty!")

class ArtifactInsurance(BaseShopItem):
    def __init__(self):
        super().__init__("Artifact Insurance", "First artifact cooldown is skipped", 65)

    def apply_effect(self, player, game_view):
        player.artifact_insurance = True
