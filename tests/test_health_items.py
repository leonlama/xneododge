from src.shop.items.health_items import HeartSnack, EmptyShell, GoldenKernel
from tests.conftest import DummyPlayer

def test_heart_snack():
    player = DummyPlayer(current_hearts=2, max_hearts=3)
    HeartSnack().apply_effect(player, None)
    assert player.current_hearts == 3

def test_empty_shell():
    player = DummyPlayer(max_hearts=3)
    EmptyShell().apply_effect(player, None)
    assert player.max_hearts == 4

def test_golden_kernel():
    player = DummyPlayer(golden_hearts=0)
    GoldenKernel().apply_effect(player, None)
    assert player.golden_hearts == 2

