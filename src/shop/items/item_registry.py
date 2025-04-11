from src.shop.items.health_items import HeartSnack, EmptyShell, GoldenKernel
from src.shop.items.wave_mod_items import SkipTicket, Smokescreen, ChaserRepellent, EMPPulse, BombDefuser, MazeJammer
from src.shop.items.temp_buff_items import OverclockFlask, EnergySurge, PointMagnet, ShieldProtocol
from src.shop.items.perm_buff_items import CDRCore, MMSChip, SpawnBooster, GoldTooth, AbsorptionModule
from src.shop.items.rare_items import SecondChance, GhostDash, VoidArtifact, ArtifactInsurance
from src.shop.items.special_items import ShopResetChip, LuckyDraw, MysteryBox

ALL_ITEMS = [
    # Health
    HeartSnack(), EmptyShell(), GoldenKernel(),
    # Wave Mods
    SkipTicket(), Smokescreen(), ChaserRepellent(), EMPPulse(), BombDefuser(), MazeJammer(),
    # Temp Buffs
    OverclockFlask(), EnergySurge(), PointMagnet(), ShieldProtocol(),
    # Perm Buffs
    CDRCore(), MMSChip(), SpawnBooster(), GoldTooth(), AbsorptionModule(),
    # Rare
    SecondChance(), GhostDash(), VoidArtifact(), ShopResetChip(), LuckyDraw(), MysteryBox(), ArtifactInsurance(),
]
