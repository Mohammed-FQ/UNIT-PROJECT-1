from core.potion import Potion
from core.weapon import Weapon
from systems.game_state import GAME_STATE
from systems.ui import ui_header, ui_print, ui_separator, ui_spacer


def print_inventory_header(player):
    ui_header("Inventory")
    ui_separator()
    ui_print(f"Health: {player.get_health()} | Weapon: {player.get_equipped_weapon().get_name()}")
    ui_print(f"Items: {[item.get_name() for item in player.get_inventory()]}")


def inventory_management():
    """Handle inventory management and chest interactions."""
    player = GAME_STATE["player"]
    while GAME_STATE["in_inventory"]:
        potions = []
        weapons = []
        for item in player.get_inventory():
            if isinstance(item, Potion):
                potions.append(item)
            elif isinstance(item, Weapon):
                weapons.append(item)

        print_inventory_header(player)
        ui_print("1- Change Weapon")
        ui_print("2- Use Potion")
        ui_print("3- Close Inventory")
        choice = input("Enter choice: ")
        ui_spacer()
        if choice == "1":
            change_weapon(weapons, player)
        elif choice == "2":
            use_potion(potions, player)
        elif choice == "3":
            GAME_STATE["in_inventory"] = False
            break
        else:
            ui_print("Pick 1, 2, or 3.", style="bold red")


def change_weapon(weapons, player):
    while True:
        if not weapons:
            ui_print("You don't have any spare weapons yet.", style="yellow")
            break
        for idx, weapon in enumerate(weapons):
            ui_print(f"{idx + 1}- {weapon.get_name()} (Damage: {weapon.get_damage()})")
        weapon_choice = input("Select a weapon to equip or q to exit: ")
        ui_spacer()
        if weapon_choice.lower() == "q":
            break
        elif weapon_choice.isdigit() and 1 <= int(weapon_choice) <= len(weapons):
            selected_weapon = weapons[int(weapon_choice) - 1]
            current_weapon = player.get_equipped_weapon()
            player.equip_weapon(selected_weapon)
            player.remove_item(selected_weapon)
            player.add_item(current_weapon)
            ui_print(f"Equipped {selected_weapon.get_name()}.", style="bold green")
            break
        else:
            ui_print("That weapon number is not valid.", style="bold red")


def use_potion(potions, player):
    while True:
        if not potions:
            ui_print("No potions left in your bag.", style="yellow")
            break
        for idx, potion in enumerate(potions):
            ui_print(f"{idx + 1}- {potion.get_name()} (Heal: {potion.get_health_restore()})")
        potion_choice = input("Select a potion to use or q to exit: ")
        ui_spacer()
        if potion_choice.lower() == "q":
            break
        elif potion_choice.isdigit() and 1 <= int(potion_choice) <= len(potions):
            selected_potion = potions[int(potion_choice) - 1]
            player.heal(selected_potion.get_health_restore())
            player.remove_item(selected_potion)
            ui_print(f"Used {selected_potion.get_name()}.", style="bold green")
            break
        else:
            ui_print("That potion number is not valid.", style="bold red")
