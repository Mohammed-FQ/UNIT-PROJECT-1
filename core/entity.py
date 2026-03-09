class Entity:
    """Shared stats and combat helpers used by all living actors."""

    def __init__(self, name="Unknown", health=0, attack_power=0):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, target):
        """Apply this entity's attack power to target."""
        target.take_damage(self.attack_power)
        return self.attack_power

    def take_damage(self, amount):
        """Reduce health but do not go below zero."""
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        """Check if the entity is still alive."""
        return self.health > 0
    
    def get_status(self):
        """Get a string representation of the entity's current status."""
        return f"{self.name}: Health={self.health}, Attack Power={self.attack_power}"
    
    """Getters for entity attributes."""
    
    def get_name(self):
        return self.name

    def get_health(self):
        return self.health
    
    def get_attack_power(self):
        return self.attack_power