from src.shop.items.temp_buff_items import *
from tests.conftest import DummyPlayer

def test_energy_surge():
    player = DummyPlayer()
    EnergySurge().apply_effect(player, None)
    assert player.status_effects.has("speed")

def test_shield_protocol():
    player = DummyPlayer()
    ShieldProtocol().apply_effect(player, None)
    assert player.status_effects.has("shield")

