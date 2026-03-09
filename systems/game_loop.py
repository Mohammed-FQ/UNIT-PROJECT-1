
from systems.combat import fight
from systems.game_state import GAME_STATE
from systems.inventory import inventory_management
from systems.ui import ui_header, ui_print, ui_separator, ui_spacer
from systems.animated_events import victory, defeat


def print_hud():
    location = GAME_STATE["current_location"]
    enemy_name = location.get_enemy().get_name() if GAME_STATE["in_combat"] else "None"
    chest_status = "Available" if GAME_STATE["chest_available"] else "None"
    directions = ", ".join(location.get_available_directions())
    enemy_style = "bold red" if GAME_STATE["in_combat"] else None
    chest_style = "bold yellow" if GAME_STATE["chest_available"] else None

    ui_header(GAME_STATE["message"])
    ui_separator()
    ui_print(f"Location: {location.get_name()}", style="bold")
    ui_print(f"Health: {GAME_STATE['player'].get_health()} | Weapon: {GAME_STATE['player'].get_equipped_weapon().get_name()}")
    ui_print(f"Enemy: {enemy_name}", style=enemy_style)
    ui_print(f"Chest: {chest_status}", style=chest_style)
    ui_print(f"Directions: {directions if directions else 'None'}")
    ui_separator()


def print_actions():
    ui_print("1- Move West")
    ui_print("2- Move East")
    ui_print("3- Move North")
    ui_print("4- Move South")
    ui_print("5- Open Inventory")
    ui_print("6- Open Chest")
    ui_print("7- Enter Combat")
    ui_print("8- Exit To Main Menu")


def print_game_result():
    if GAME_STATE["victory"]:
        victory()
        ui_spacer()
    elif GAME_STATE["defeat"]:
        defeat()
        ui_spacer()

def move_player(direction):
    if can_move():
        next_location = GAME_STATE["current_location"].move(direction)
        if next_location:
            GAME_STATE["current_location"] = next_location
            GAME_STATE["message"] = f"You moved {direction} to {GAME_STATE['current_location'].get_name()}."
        else:
            GAME_STATE["message"] = f"You can't move {direction} from here."


def can_move():
    if GAME_STATE["in_combat"]:
        GAME_STATE["message"] = "You can't move while in combat!"
        return False
    elif GAME_STATE["chest_available"]:
        GAME_STATE["message"] = "Open the chest first before moving."
        return False
    else:
        return True


def game_loop():
    """Main game loop that runs until victory or defeat."""
    exited_to_menu = False

    while not GAME_STATE["victory"] and not GAME_STATE["defeat"]:
        GAME_STATE["chest_available"] = GAME_STATE["current_location"].has_chest()
        GAME_STATE["in_combat"] = GAME_STATE["current_location"].has_enemy()
        print_hud()
        print_actions()
        action = input("Enter choice: ")
        ui_spacer()
        if action == "1":
            move_player("west")
        elif action == "2":
            move_player("east")
        elif action == "3":
            move_player("north")
        elif action == "4":
            move_player("south")
        elif action == "5":
            GAME_STATE["in_inventory"] = True
            inventory_management()
        elif action == "6":
            if GAME_STATE["chest_available"]:
                GAME_STATE["message"] = f"You opened the chest and found an item. Found {GAME_STATE['current_location'].get_chest().get_item().get_name()}"
                GAME_STATE["player"].add_item(GAME_STATE["current_location"].get_chest().get_item())
                GAME_STATE["current_location"].remove_chest()
                GAME_STATE["chest_available"] = False
            else:
                GAME_STATE["message"] = "No chest here."
        elif action == "7":
            if GAME_STATE["in_combat"]:
                fight()
            else:
                GAME_STATE["message"] = "No enemy here. Move to another location."
        elif action == "8":
            GAME_STATE["message"] = "Returning to main menu..."
            exited_to_menu = True
            break
        else:
            GAME_STATE["message"] = "I don't know that action. Pick a number from the menu."

    if not exited_to_menu:
        print_game_result()


