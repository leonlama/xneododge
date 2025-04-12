from src.shop.items.base import BaseShopItem
import arcade

class SecondChance(BaseShopItem):
    def __init__(self):
        super().__init__("Second Chance", "Revive once with 2 red hearts", 150, rarity="legendary")

    def apply_effect(self, player, game_view):
        player.status_effects.add("second_chance")


class GhostDash(BaseShopItem):
    def __init__(self):
        super().__init__("Ghost Dash", "After dashing, you're invincible for 1.5s", 120, rarity="legendary")

    def apply_effect(self, player, game_view):
        player.status_effects.add("ghost_dash", duration=1.5)


class VoidArtifact(BaseShopItem):
    def __init__(self):
        super().__init__("Void Artifact", "All orb cooldowns -50% this wave", 110, rarity="legendary")

    def apply_effect(self, player, game_view):
        player.status_effects.add("cooldown", duration=game_view.wave_manager.wave_duration, reduction=0.5)


class ArtifactInsurance(BaseShopItem):
    def __init__(self):
        super().__init__("Artifact Insurance", "Your first artifact won't go on cooldown", 100, rarity="legendary")

    def apply_effect(self, player, game_view):
        player.status_effects.add("artifact_insurance")


class ShopResetChip(BaseShopItem):
    def __init__(self):
        super().__init__("Shop Reset Chip", "Refresh shop items instantly", 90, rarity="rare")

    def apply_effect(self, player, game_view):
        game_view.refresh_shop_items()


class LuckyDraw(BaseShopItem):
    def __init__(self):
        super().__init__("Lucky Draw", "Get 1 random item for free", 70, rarity="rare")

    def apply_effect(self, player, game_view):
        from src.shop.items.item_registry import ALL_ITEMS
        import random
        choice = random.choice(ALL_ITEMS)
        choice.apply_effect(player, game_view)
        print(f"🎁 Lucky Draw gave you: {choice.name}")


class MysteryBox(BaseShopItem):
    def __init__(self):
        super().__init__("Mystery Box", "50% chance: amazing item or nothing", 50, rarity="rare")

    def apply_effect(self, player, game_view):
        import random
        if random.random() < 0.5:
            from src.shop.items.rare_items import SecondChance
            item = SecondChance()
            item.apply_effect(player, game_view)
            print("🎉 Mystery Box granted: Second Chance!")
        else:
            print("💨 Mystery Box was empty...")
