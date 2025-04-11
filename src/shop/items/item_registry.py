from shop.items.health_items import HeartSnack, EmptyShell, GoldenKernel

ITEM_REGISTRY = {
    "health": [
        HeartSnack(),
        EmptyShell(),
        GoldenKernel()
    ],
    # Add other item categories later (wavemod, tempbuff, permbuff, etc.)
}

ALL_ITEMS = []
for category_items in ITEM_REGISTRY.values():
    ALL_ITEMS.extend(category_items)
