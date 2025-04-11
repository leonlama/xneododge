from src.shop.items.base import BaseShopItem

class SecondChance(BaseShopItem):
    def __init__(self):
        super().__init__("Second Chance", "Revive once with 2 red hearts", 100, "rare")

    def apply_effect(self, player, game_view):
        player.has_revive = True

class GhostDash(BaseShopItem):
    def __init__(self):
        super().__init__("Ghost Dash", "1.5s invincibility after dash", 85, "legendary")

    def apply_effect(self, player, game_view):
        player.ghost_dash_enabled = True

class VoidArtifact(BaseShopItem):
    def __init__(self):
        super().__init__("Void Artifact", "Orb cooldowns -50% this wave", 90, "legendary")

    def apply_effect(self, player, game_view):
        player.apply_status_effect("orb_cdr_wave", duration=1, value=0.5)

class ArtifactInsurance(BaseShopItem):
    def __init__(self):
        super().__init__("Artifact Insurance", "First artifact cooldown is skipped", 65, "legendary")

    def apply_effect(self, player, game_view):
        player.artifact_insurance = True
