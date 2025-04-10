import pytest
from src.views.hud import HUD
from src.entities.player import Player

@pytest.fixture
def dummy_player():
    return Player(0, 0)

def test_hud_with_no_effects(dummy_player):
    hud = HUD(dummy_player)
    dummy_player.status_effects = {}
    output = hud.get_effect_text_lines()
    assert output == []

def test_hud_with_one_effect(dummy_player):
    hud = HUD(dummy_player)
    dummy_player.status_effects = {"speed": 5}
    output = hud.get_effect_text_lines()
    assert output == ["speed: 5.0s"]

def test_hud_with_multiple_effects(dummy_player):
    hud = HUD(dummy_player)
    dummy_player.status_effects = {
        "speed": 10,
        "multiplier": 8,
        "shield": 12
    }
    output = hud.get_effect_text_lines()
    assert "speed: 10.0s" in output
    assert "multiplier: 8.0s" in output
    assert "shield: 12.0s" in output