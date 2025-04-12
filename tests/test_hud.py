import pytest
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
    hud = HUD(dummy_player, wave_manager=DummyWaveManager(), artifact_manager=DummyArtifactManager())
    dummy_player.status_effects.effects = {}
    output = hud.get_effect_text_lines()
    assert output == []

def test_hud_with_one_effect(dummy_player):
    hud = HUD(dummy_player, wave_manager=DummyWaveManager(), artifact_manager=DummyArtifactManager())
    dummy_player.status_effects.effects = {"speed": {"duration": 5}}
    output = hud.get_effect_text_lines()
    assert output == ["speed: 5.0s"]

def test_hud_with_multiple_effects(dummy_player):
    hud = HUD(dummy_player, wave_manager=DummyWaveManager(), artifact_manager=DummyArtifactManager())
    dummy_player.status_effects.effects = {
        "speed": {"duration": 10},
        "multiplier": {"duration": 8},
        "shield": {"duration": 12}
    }
    output = hud.get_effect_text_lines()
    assert "speed: 10.0s" in output
    assert "multiplier: 8.0s" in output
    assert "shield: 12.0s" in output