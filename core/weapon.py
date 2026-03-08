from core.loot import Loot


class Weapon(Loot):
    """Loot that increases player attack when equipped."""

    def __init__(self, name, damage):
        super().__init__(name)
        self.damage = damage

    def get_damage(self):
        return self.damage