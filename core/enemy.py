from core.entity import Entity


class Enemy(Entity):
    """Combat entity that holds a single loot drop."""

    def __init__(self, name, health, attack_power, loot=None):
        super().__init__(name=name, health=health, attack_power=attack_power)
        self.loot = loot

    def drop_loot(self):
        """Return item granted when this enemy is defeated."""
        return self.loot
    
    def get_status(self):
        loot_name = self.loot.name if self.loot else "None"
        return f"{self.name}: Health={self.health}, Attack Power={self.attack_power}, Loot={loot_name}"