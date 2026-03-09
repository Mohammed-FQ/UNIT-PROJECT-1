import os

from core.player import Player
from systems.game_loop import game_loop
from systems.game_state import GAME_STATE, reset_game_state
from systems.ui import ui_header, ui_print, ui_spacer
from world.game_map import Game_Map


def print_menu_header(title):
    ui_header(title)


def main_menu():
    while True:
        print_menu_header("Welcome")
        ui_print("1. Start Game")
        ui_print("2. Exit")
        choice = input("Enter choice: ")
        ui_spacer()
        if choice == "1":
            reset_game_state()
            should_start = start_menu()
            if not should_start:
                continue
            player = Player()
            map_grid = Game_Map()
            GAME_STATE["player"] = player
            GAME_STATE["map_grid"] = map_grid
            GAME_STATE["current_location"] = map_grid.get_start_location()

            game_loop()
            continue
        elif choice == "2":
            break
        else:
            ui_print("That option is not valid, try again.", style="bold red")

def start_menu():
    print_menu_header("Start Menu")
    while True:
        ui_print("1. Start New Game")
        ui_print("2. Change Map")
        ui_print("3. Change Loot Drops")
        ui_print("4. Back to Main Menu")
        choice = input("Enter choice: ")
        ui_spacer()
        if choice == "1":
            return True
        elif choice == "2":
            maps()
        elif choice == "3":
            loot_drops()
        elif choice == "4":
            return False
        else:
            ui_print("Pick a number from 1 to 4.", style="bold red")

def maps():
    ui_header("Change Map")
    folder_path = "world/maps/"
    file_maps = os.listdir(folder_path)
    ui_print("Available Maps:", style="bold cyan")
    for index, file in enumerate(file_maps, 1):
        ui_print(f"{index}. {file}")
    choice = input("Enter the number of the map you want to use: ")
    ui_spacer()
    try:
        selected_map = file_maps[int(choice) - 1]
        GAME_STATE["game_map"] = os.path.join(folder_path, selected_map)
        ui_print(f"Selected map: {selected_map}", style="bold green")
    except (IndexError, ValueError):
        ui_print("Map selection failed. Choose a number from the list.", style="bold red")



def loot_drops():
    ui_header("Change Loot Drops")
    folder_path = "world/loot_drops/"
    file_loot = os.listdir(folder_path)
    ui_print("Available Loot Files:", style="bold cyan")
    for index, file in enumerate(file_loot, 1):
        ui_print(f"{index}. {file}")
    choice = input("Enter the number of the loot drops file you want to use: ")
    ui_spacer()
    try:
        selected_loot = file_loot[int(choice) - 1]
        GAME_STATE["loot_data"] = os.path.join(folder_path, selected_loot)
        ui_print(f"Selected loot file: {selected_loot}", style="bold green")
    except (IndexError, ValueError):
        ui_print("Loot selection failed. Choose a number from the list.", style="bold red")