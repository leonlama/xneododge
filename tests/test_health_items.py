from src.shop.items.health_items import HeartSnack, EmptyShell, GoldenKernel
from tests.conftest import DummyPlayer

def test_heart_snack():
    player = DummyPlayer(current_hearts=2, max_hearts=3, max_heart_slots=3)
    HeartSnack().apply_effect(player, None, shop_items=None)
    assert player.current_hearts == 3

def test_empty_shell():
    player = DummyPlayer(max_heart_slots=3)
    EmptyShell().apply_effect(player, None, shop_items=None)
    assert player.max_heart_slots == 4

def test_golden_kernel():
    player = DummyPlayer(golden_hearts=1)
    GoldenKernel().apply_effect(player, None, shop_items=None)
    assert player.golden_hearts == 2
