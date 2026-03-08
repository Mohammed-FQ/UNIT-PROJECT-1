class Location:
    """A single navigable location with optional chest/enemy and neighbors."""

    def __init__(self, name, north=None, south=None, east=None, west=None, chest=None, enemy=None, level=1):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.chest = chest
        self.enemy = enemy
        self.level = level

    def move(self, direction):
        """Return neighboring location in the requested direction."""
        if direction == "north":
            return self.north
        elif direction == "south":
            return self.south
        elif direction == "east":
            return self.east
        elif direction == "west":
            return self.west
        return None

    def get_enemy(self):
        """Get the enemy at this location."""
        return self.enemy

    def get_chest(self):
        """Get the chest at this location."""
        return self.chest

    def get_name(self):
        """Get the name of this location."""
        return self.name

    def get_level(self):
        """Get the level of this location."""
        return self.level

    def has_enemy(self):
        """Check if this location has an enemy."""
        return self.enemy is not None

    def has_chest(self):
        """Check if this location has a chest."""
        return self.chest is not None

    def remove_enemy(self):
        """Remove the enemy from this location."""
        self.enemy = None

    def remove_chest(self):
        """Remove the chest from this location."""
        self.chest = None

    def get_available_directions(self):
        """List valid movement directions from this location."""
        directions = []
        if self.north:
            directions.append("north")
        if self.south:
            directions.append("south")
        if self.east:
            directions.append("east")
        if self.west:
            directions.append("west")
        return directions