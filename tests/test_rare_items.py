from src.shop.items.rare_items import *
from tests.conftest import DummyPlayer, DummyGameView

def test_second_chance():
    player = DummyPlayer()
    game_view = DummyGameView()
    SecondChance().apply_effect(player, game_view, shop_items=None)

    # Debug output
    print("Effects after applying second chance:", player.status_effects.effects.keys())
    print("Current hearts:", player.current_hearts)

    # Assertions
    assert "second_chance" in player.status_effects.effects
    assert player.current_hearts == 3
    assert len(player.status_effects.effects) == 1  # adjust this after seeing print output
