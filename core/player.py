from core.entity import Entity
from core.weapon import Weapon


class Player(Entity):
    """Main controllable hero with inventory and optional equipped weapon."""

    def __init__(self, name="Hero", health=100, attack_power=5, equiped=None, inventory=None):
        super().__init__(name=name, health=health, attack_power=attack_power)
        if equiped is None:
            equiped = Weapon("Fist", 5)
        if inventory is None:
            inventory = []
        self.equiped_weapon = equiped
        self.inventory = inventory

    def add_item(self, item):
        """Add an item to inventory."""
        self.inventory.append(item)

    def remove_item(self, item):
        """Remove an item from inventory if present."""
        if item in self.inventory:
            self.inventory.remove(item)

    def equip_weapon(self, weapon):
        """Equip weapon and update attack power to weapon damage."""
        self.equiped_weapon = weapon
        self.attack_power = weapon.damage

    def heal(self, amount):
        """Restore health up to max cap of 100."""
        self.health += amount
        if self.health > 100:
            self.health = 100

    def get_status(self):
        weapon_name = self.equiped_weapon.name if self.equiped_weapon else "None"
        return f"{self.name}: Health={self.health}, Attack Power={self.attack_power}, Equipped Weapon={weapon_name}"
    
    """Getters for player attributes."""
    
    def get_inventory(self):
        return self.inventory
    
    def get_equipped_weapon(self):
        return self.equiped_weapon
    
    def get_name(self):
        return self.name