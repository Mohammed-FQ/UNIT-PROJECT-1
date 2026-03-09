from systems.game_state import GAME_STATE
from systems.inventory import inventory_management
from systems.ui import ui_header, ui_print, ui_spacer


def fight():
    """Handle combat between the player and an enemy."""
    player = GAME_STATE["player"]
    enemy = GAME_STATE["current_location"].get_enemy()
    if enemy is None:
        GAME_STATE["message"] = "No enemy in this location."
        return True

    ui_header(f"You encounter a {enemy.get_name()}!")
    while player.is_alive() and enemy.is_alive():
        ui_print("1- Attack")
        ui_print("2- Open Inventory")
        action = input("Enter choice: ")
        ui_spacer()
        if action == "1":
            damage = player.attack(enemy)
            ui_print(f"You attack the {enemy.get_name()} for {damage} damage! It has {enemy.get_health()} health left.", style="bold green")
        elif action == "2":
            GAME_STATE["in_inventory"] = True
            inventory_management()
            continue
        else:
            ui_print("Pick 1 to attack or 2 for inventory.", style="bold red")
            continue

        if enemy.is_alive():
            damage = enemy.attack(player)
            ui_print(f"The {enemy.get_name()} attacks you for {damage} damage! You have {player.get_health()} health left.", style="bold red")

    if not player.is_alive():
        GAME_STATE["defeat"] = True
        GAME_STATE["message"] = "You were defeated. Game over."
        return False

    dropped_loot = enemy.drop_loot()
    GAME_STATE["current_location"].remove_enemy()
    GAME_STATE["in_combat"] = False

    if dropped_loot is not None:
        player.add_item(dropped_loot)
        GAME_STATE["message"] = f"You defeated {enemy.get_name()} and got {dropped_loot.get_name()}!"
    else:
        GAME_STATE["message"] = f"You defeated {enemy.get_name()}!"

    if enemy.get_name() == "THE PYTHON":
        GAME_STATE["victory"] = True
        GAME_STATE["message"] = "You defeated THE PYTHON and saved the village!"

    return True
