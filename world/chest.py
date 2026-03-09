import json
from random import choices

from core.potion import Potion
from core.weapon import Weapon
from systems.game_state import GAME_STATE

class Chest:
    """Chest that rolls exactly one loot item at creation time."""

    def __init__(self, level=1, loot_data=None):
        if loot_data is None:
            loot_data = GAME_STATE["loot_data"]
        self.level = level
        self.loot = self.generate_loot(loot_data)

    def get_item(self):
        """Return chest loot item."""
        return self.loot

    def get_level(self):
        """Get the level of this chest."""
        return self.level

    def generate_loot(self, loot_data_j):
        with open(loot_data_j, 'r') as f:
            loot_data = json.load(f)

        weights = []
        for item in loot_data:
            if item["level"] == self.level:
                weight = 10
            else:
                weight = 3
            weights.append(weight)

        selected_loot = choices(loot_data, weights=weights, k=1)[0]

        # Convert dictionary → object
        if selected_loot["type"] == "Potion":
            return Potion(
                selected_loot["name"],
                selected_loot["health_restore"]
            )

        elif selected_loot["type"] == "Weapon":
            return Weapon(
                selected_loot["name"],
                selected_loot["damage"]
            )