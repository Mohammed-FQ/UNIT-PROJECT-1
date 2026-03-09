import json
from random import choice

from core.enemy import Enemy
from systems.game_state import GAME_STATE
from world.chest import Chest
from world.location import Location


class Game_Map:
    """Game map containing all locations and their connections."""

    def __init__(self, map_file=None, loot_data=None):
        if map_file is None:
            map_file = GAME_STATE["game_map"]
        if loot_data is None:
            loot_data = GAME_STATE["loot_data"]
        self.start_location = None
        self.locations = self.load_map(map_file, loot_data)
        self.current_location = self.start_location

    def load_map(self, map_file, loot_data):
        """Load map data from JSON file and create Location instances."""
        with open(map_file, 'r') as f:
            map_data = json.load(f)

        grid = []
        distance_from_start = len(map_data)

        for row in map_data:
            grid_row = []
            for cell in row:
                chest = None
                enemy = None
                if cell["name"] == "Python's Throne":
                    enemy = Enemy("THE PYTHON", health=100, attack_power=20, loot=None)
                else:
                    if cell["enemy"]:
                        # Random 50% chance that enemy has loot.
                        chance = choice([True, False])

                        if distance_from_start > 4:
                            if chance:
                                loot = Chest(level=3, loot_data=loot_data).get_item()
                            else:
                                loot = None
                            enemy = Enemy("Giant Python", health=30, attack_power=10, loot=loot)
                        elif distance_from_start > 2:
                            if chance:
                                loot = Chest(level=2, loot_data=loot_data).get_item()
                            else:
                                loot = None
                            enemy = Enemy("Medium Python", health=20, attack_power=7, loot=loot)
                        else:
                            if chance:
                                loot = Chest(level=1, loot_data=loot_data).get_item()
                            else:
                                loot = None
                            enemy = Enemy("Lil Python", health=15, attack_power=5, loot=loot)
                if cell["chest"]:
                    if distance_from_start > 4:
                        chest = Chest(level=3, loot_data=loot_data)
                    elif distance_from_start > 2:
                        chest = Chest(level=2, loot_data=loot_data)
                    else:
                        chest = Chest(level=1, loot_data=loot_data)

                location = Location(name=cell["name"], chest=chest, enemy=enemy)
                grid_row.append(location)

            distance_from_start -= 1
            grid.append(grid_row)

        self.start_location = grid[len(grid) - 1][len(grid[0]) // 2]
        self.locations = grid
        self.connect_locations()
        return grid

    def connect_locations(self):
        """Set north/south/east/west neighbors for all locations based on grid position."""
        for i in range(len(self.locations)):
            for j in range(len(self.locations[i])):
                location = self.locations[i][j]
                if i > 0:
                    location.north = self.locations[i-1][j]
                if i < len(self.locations) - 1:
                    location.south = self.locations[i+1][j]
                if j > 0:
                    location.west = self.locations[i][j-1]
                if j < len(self.locations[i]) - 1:
                    location.east = self.locations[i][j+1]

    def get_start_location(self):
        """Return the starting location for the player."""
        return self.start_location

    def get_grid(self):
        """Return the 2D grid of locations."""
        return self.locations

    def set_current_location(self, row, col):
        """Set the current location to the location at the specified grid position."""
        if 0 <= row < len(self.locations) and 0 <= col < len(self.locations[0]):
            self.current_location = self.locations[row][col]
        else:
            raise ValueError(f"Invalid location position: ({row}, {col})")

    def get_location_position(self, location):
        """Get the grid position (row, col) of a given location."""
        for i, row in enumerate(self.locations):
            for j, loc in enumerate(row):
                if loc == location:
                    return (i, j)
        return None

    def move_player(self, direction):
        """Move the player in the specified direction. Returns True if successful, False otherwise."""
        if self.current_location is None:
            return False

        next_location = self.current_location.move(direction)
        if next_location is not None:
            self.current_location = next_location
            return True
        return False


