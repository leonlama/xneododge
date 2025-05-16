from src.shop.items.perm_buff_items import *
from tests.conftest import DummyPlayer

def test_cdr_core():
    player = DummyPlayer()
    player.permanent_effects = {"cooldown_reduction": 0.0}
    CDRCore().apply_effect(player, None, shop_items=None)
    assert player.permanent_effects["cooldown_reduction"] == 0.1
