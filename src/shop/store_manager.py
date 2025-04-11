import random
from src.shop.items.item_registry import ALL_ITEMS

class StoreManager:
    def __init__(self):
        pass

    def get_items_for_wave(self, wave_number: int, count: int = 3):
        # Filter and weight items by wave_number
        common = []
        rare = []

        for item in ALL_ITEMS:
            if hasattr(item, "rarity"):
                if item.rarity == "rare":
                    rare.append(item)
                else:
                    common.append(item)
            else:
                common.append(item)

        if wave_number < 10:
            pool = common
        elif wave_number < 20:
            pool = common + random.choices(rare, k=1)
        else:
            pool = common + rare

        return random.sample(pool, min(count, len(pool)))
