from src.shop.items.rare_items import *
from tests.conftest import DummyPlayer, DummyGameView

def test_second_chance():
    player = DummyPlayer()
    game_view = DummyGameView()
    SecondChance().apply_effect(player, game_view, shop_items=None)
    assert player.has_second_chance == True
    assert player.current_hearts == 2

