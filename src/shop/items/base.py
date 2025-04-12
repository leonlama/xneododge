class BaseShopItem:
    def __init__(self, name, description, price=0, rarity="common"):
        self.name = name
        self.description = description
        self.price = price
        self.rarity = rarity

    def apply(self, player, game_view, shop_items=None):
        self.apply_effect(player, game_view, shop_items)

    def apply_effect(self, player, game_view, shop_items=None):
        """Override this in child classes to apply effect to the player or game."""
        raise NotImplementedError("Each shop item must implement apply_effect()")

    def is_available(self, player, game_view):
        """Optional: You can override to make items conditional."""
        return True
