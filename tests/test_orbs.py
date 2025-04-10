import pytest
from src.entities.orb import Orb
from src.entities.player import Player
from src.systems.status_effects import StatusEffectManager

@pytest.fixture
def player():
    player = Player(0, 0)
    player.status_effects = StatusEffectManager(player)
    return player

@pytest.fixture
def dummy_texture():
    return ":resources:images/items/gemBlue.png"

def test_speed_orb_applies_effect(player, dummy_texture):
    orb = Orb("speed", 100, 100, dummy_texture)
    orb.apply_effect(player)
    assert "speed" in player.status_effects.active_effects

def test_multiplier_orb_applies_effect(player, dummy_texture):
    orb = Orb("multiplier", 100, 100, dummy_texture)
    orb.apply_effect(player)
    assert "multiplier" in player.status_effects.active_effects

def test_cooldown_orb_applies_effect(player, dummy_texture):
    orb = Orb("cooldown", 100, 100, dummy_texture)
    orb.apply_effect(player)
    assert "cooldown" in player.status_effects.active_effects

def test_shield_orb_applies_effect(player, dummy_texture):
    orb = Orb("shield", 100, 100, dummy_texture)
    orb.apply_effect(player)
    assert "shield" in player.status_effects.active_effects

def test_red_heart_orb_heals_player(player, dummy_texture):
    player.current_hearts = 2
    player.max_hearts = 3
    orb = Orb("red_heart", 0, 0, dummy_texture)
    orb.apply_effect(player)
    assert player.current_hearts == 3

def test_gray_heart_orb_adds_slot(player, dummy_texture):
    player.max_hearts = 3
    orb = Orb("gray_heart", 0, 0, dummy_texture)
    orb.apply_effect(player)
    assert player.max_hearts == 4

def test_golden_heart_orb_adds_overheart(player, dummy_texture):
    player.gold_hearts = 0
    orb = Orb("golden_heart", 0, 0, dummy_texture)
    orb.apply_effect(player)
    assert player.gold_hearts == 1