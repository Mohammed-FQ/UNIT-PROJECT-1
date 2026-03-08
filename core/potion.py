from core.loot import Loot


class Potion(Loot):
    """Loot that restores player health when consumed."""

    def __init__(self, name, health_restore):
        super().__init__(name)
        self.health_restore = health_restore

    def get_health_restore(self):
        return self.health_restore