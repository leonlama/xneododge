from src.shop.items.wave_mod_items import *
from tests.conftest import DummyPlayer, DummyGameView

def test_skip_ticket():
    game_view = DummyGameView()
    SkipTicket().apply_effect(None, game_view, shop_items=None)
    assert game_view.wave_manager.modifiers["skip_next_wave"]

def test_smokescreen():
    game_view = DummyGameView()
    Smokescreen().apply_effect(None, game_view, shop_items=None)
    assert game_view.wave_manager.modifiers["reduce_spawn_rate"] == (0.75, 5)
