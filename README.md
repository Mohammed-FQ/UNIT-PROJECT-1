# Python Slayer

## Project Summary
Python Slayer is a command-line RPG built in Python. The player explores a grid-based world, collects loot, manages inventory, fights enemies, and wins by defeating `THE PYTHON`.

The project is structured with modular packages:
- `core/`: player, enemies, and loot entities
- `systems/`: game loop, menus, combat, inventory, and game state
- `world/`: map loading, locations, chests, and JSON content files

## Implemented Features
- Main menu and start menu flow
- Map and loot-file selection before game start
- Grid movement (north, south, east, west)
- Rich CLI HUD and formatted gameplay output
- Chest interaction and loot collection
- Inventory actions (equip weapon, use potion)
- Turn-based combat with in-combat inventory access
- Victory/defeat handling and return to main menu

## Requirements
- Python 3.10+ (3.11 recommended)
- `rich`

Install dependencies:
```bash
pip install -r requirements.txt
```

## Run
Run from the project root (`UNIT-PROJECT-1`).

Windows:
```bash
python play_game.py
```

Windows (included virtual environment):
```bash
gameEnv\Scripts\python.exe play_game.py
```

macOS/Linux:
```bash
python3 play_game.py
```

## Controls
Main Menu:
1. Start Game
2. Exit

Start Menu:
1. Start New Game
2. Change Map
3. Change Loot Drops
4. Back to Main Menu

In Game:
1. Move West
2. Move East
3. Move North
4. Move South
5. Open Inventory
6. Open Chest
7. Enter Combat
8. Exit To Main Menu

Combat:
1. Attack
2. Open Inventory

Inventory:
1. Change Weapon
2. Use Potion
3. Close Inventory

## Custom Content
Content files are loaded from:
- Maps: `world/maps/`
- Loot: `world/loot_drops/`

Included examples:
- Maps: `default_map.json`, `easy_map.json`, `hard_map.json`
- Loot: `default_loot.json`, `overpowered_loot.json`

Map item format:
```json
{ "name": "Village Square", "enemy": false, "chest": false }
```

Loot item format:
```json
{ "type": "Weapon", "name": "Sword", "damage": 10, "level": 1 }
```
```json
{ "type": "Potion", "name": "Health Potion", "health_restore": 20, "level": 1 }
```