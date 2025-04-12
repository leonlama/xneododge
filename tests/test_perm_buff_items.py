from src.shop.items.perm_buff_items import *
from tests.conftest import DummyPlayer

def test_cdr_core():
    player = DummyPlayer()
    CDRCore().apply_effect(player, None, shop_items=None)
    assert player.permanent_cooldown_reduction == 0.10

