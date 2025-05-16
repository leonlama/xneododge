import pytest
from unittest.mock import MagicMock
import arcade
from src.views.hud import HUD
from src.entities.player import Player
from tests.conftest import DummyWaveManager, DummyStatusEffects

class DummyArtifactManager:
    def __init__(self):
        self.active_artifacts = []

@pytest.fixture
def dummy_player():
    player = Player(0, 0)
    player.status_effects = DummyStatusEffects()
    return player

def test_hud_with_no_effects(dummy_player):
    arcade.get_window = MagicMock(return_value=None)  # Mock arcade window to prevent errors
    hud = HUD(dummy_player, wave_manager=DummyWaveManager(), artifact_manager=DummyArtifactManager())
    dummy_player.status_effects.effects = {}
    output = hud.get_effect_text_lines()
    assert output == []

def test_hud_with_one_effect(dummy_player):
    arcade.get_window = MagicMock(return_value=None)  # Mock arcade window to prevent errors
    hud = HUD(dummy_player, wave_manager=DummyWaveManager(), artifact_manager=DummyArtifactManager())
    dummy_player.status_effects.effects = {"speed": {"duration": 5}}
    output = hud.get_effect_text_lines()
    assert output == ["speed: 5.0s"]

def test_hud_with_multiple_effects(dummy_player):
    arcade.get_window = MagicMock(return_value=None)  # Mock arcade window to prevent errors
    hud = HUD(dummy_player, wave_manager=DummyWaveManager(), artifact_manager=DummyArtifactManager())
    dummy_player.status_effects.effects = {
        "speed": {"duration": 10},
        "multiplier": {"duration": 8},
        "shield": {"duration": 12}
    }
    output = hud.get_effect_text_lines()
    assert output == ["speed: 10.0s", "multiplier: 8.0s", "shield: 12.0s"]