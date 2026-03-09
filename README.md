# Python Slayer

## Project Summary

Python Slayer is a command-line RPG built in Python. The player explores a grid-based world, collects loot, manages inventory, fights enemies, and wins by defeating `THE PYTHON`.

## Features

- Menu-driven gameplay with a clear command flow
- Select map and loot files before starting a run
- Grid movement: west, east, north, south
- Turn-based combat with inventory access during fights
- Chest and enemy loot collection
- Weapon swapping and potion usage
- Victory and defeat end screens

## Project Structure

- `play_game.py`: entry point
- `core/`: entity (player, enemy), loot (weapon, potion)
- `systems/`: menus, game loop, combat, UI, game state
- `world/`: map/chest/location logic + JSON data files

## Quick Start

### Requirements

- Python (3.11 recommended)
- `rich`
- `asciimatics`

From the project root (`UNIT-PROJECT-1`):

Install dependencies:

### Windows

```
python -m venv gameEnv
source gameEnv/Scripts/activate
pip install -r requirements.txt
python play_game.py
```

### macOS/Linux

```
python3 -m venv gameEnv
source gameEnv/bin/activate
pip3 install -r requirements.txt
python3 play_game.py
```

##### \*\*\* if you are havinng issues installing dependencies I only used rich and asciimatics

## Controls

#### giFor the best gameplay experience, run the CLI in full-screen mode.

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
