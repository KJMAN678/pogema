from gymnasium import register

from pogema.a_star_policy import AStarAgent, BatchAStarAgent
from pogema.grid_config import (Easy8x8, Easy16x16, Easy32x32, Easy64x64,
                                ExtraHard8x8, ExtraHard16x16, ExtraHard32x32,
                                ExtraHard64x64, GridConfig, Hard8x8, Hard16x16,
                                Hard32x32, Hard64x64, Normal8x8, Normal16x16,
                                Normal32x32, Normal64x64)
from pogema.integrations.make_pogema import pogema_v0

__version__ = "1.2.1"

__all__ = [
    "GridConfig",
    "pogema_v0",
    "AStarAgent",
    "BatchAStarAgent",
    "Easy8x8",
    "Normal8x8",
    "Hard8x8",
    "ExtraHard8x8",
    "Easy16x16",
    "Normal16x16",
    "Hard16x16",
    "ExtraHard16x16",
    "Easy32x32",
    "Normal32x32",
    "Hard32x32",
    "ExtraHard32x32",
    "Easy64x64",
    "Normal64x64",
    "Hard64x64",
    "ExtraHard64x64",
]

register(
    id="Pogema-v0",
    entry_point="pogema.integrations.make_pogema:make_single_agent_gym",
)
