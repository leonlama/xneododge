import pytest
from src.shop.items.health_items import HeartSnack, EmptyShell, GoldenKernel
from src.shop.items.temp_buff_items import EnergySurge, ShieldProtocol
from src.shop.items.perm_buff_items import CDRCore
from src.shop.items.wave_mod_items import SkipTicket, Smokescreen
from src.shop.items.rare_items import SecondChance

# Dummy implementations to mock player and game state

class DummyStatusEffects:
    def __init__(self):
        self.effects = {}

    def apply(self, name, **kwargs):
        self.effects[name] = kwargs

    def has(self, name):
        return name in self.effects

class DummyPlayer:
    def __init__(self, current_hearts=3, max_heart_slots=3, golden_hearts=0):
        self.current_hearts = current_hearts
        self.max_heart_slots = max_heart_slots
        self.golden_hearts = golden_hearts
        self.status_effects = DummyStatusEffects()
        self.permanent_effects = {}

    def heal(self, amount):
        self.current_hearts += amount

    def add_golden_heart(self):
        self.golden_hearts += 1

    def apply_orb_effect(self, name, duration=None, magnitude=None):
        self.status_effects.effects[name] = {"duration": duration, "magnitude": magnitude}

    def add_permanent_item(self, name):
        self.permanent_effects[name] = True

    def add_temporary_item(self, name, duration):
        self.status_effects.effects[name] = {"duration": duration}

class DummyGameView:
    def __init__(self):
        self.skip_wave_called = False

    def skip_wave(self):
        self.skip_wave_called = True

# Health Items

def test_heart_snack_heals_player():
    player = DummyPlayer(current_hearts=2)
    HeartSnack().apply_effect(player, None)
    assert player.current_hearts == 3

def test_empty_shell_adds_heart_slot():
    player = DummyPlayer(max_heart_slots=3)
    EmptyShell().apply_effect(player, None)
    assert player.max_heart_slots == 4

def test_golden_kernel_adds_golden_heart():
    player = DummyPlayer(golden_hearts=0)
    GoldenKernel().apply_effect(player, None)
    assert player.golden_hearts == 1

# Temporary Buff Items

def test_energy_surge_adds_speed_effect():
    player = DummyPlayer()
    EnergySurge().apply_effect(player, None)
    assert player.status_effects.has("speed")

def test_shield_protocol_applies_shield():
    player = DummyPlayer()
    ShieldProtocol().apply_effect(player, None)
    assert player.status_effects.has("shield")

# Permanent Buff Items

def test_cdr_core_increases_cooldown_reduction():
    player = DummyPlayer()
    CDRCore().apply_effect(player, None)
    assert player.permanent_effects.get("cooldown_reduction", 0) == 0.1

# Wave Modifiers

def test_skip_ticket_skips_wave():
    player = DummyPlayer()
    game_view = DummyGameView()
    SkipTicket().apply_effect(player, game_view)
    assert game_view.skip_wave_called is True

def test_smokescreen_applies_effect():
    player = DummyPlayer()
    Smokescreen().apply_effect(player, None)
    assert player.status_effects.has("smokescreen")

# Rare Effects

def test_second_chance_applies_and_heals():
    player = DummyPlayer(current_hearts=2)
    game_view = DummyGameView()
    SecondChance().apply_effect(player, game_view)
    assert "second_chance" in player.status_effects.effects
    assert player.current_hearts == 3
