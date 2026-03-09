def build_initial_game_state():
    return {
        "player": None,
        "map_grid": None,
        "message": "Welcome to the Game! Explore the map, defeat enemies, and find loot to slay The Python!",
        "current_location": None,
        "in_combat": False,
        "in_inventory": False,
        "victory": False,
        "defeat": False,
        "chest_available": False,
        "game_map": "world/maps/default_map.json",
        "loot_data": "world/loot_drops/default_loot.json"
    }


GAME_STATE = build_initial_game_state()

def reset_game_state():
    """Reset the game state to initial values."""
    GAME_STATE.clear()
    GAME_STATE.update(build_initial_game_state())