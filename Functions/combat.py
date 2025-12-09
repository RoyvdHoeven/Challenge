from Functions.misc import d20, d8
from time import sleep
from Assets.ascii_art import ascii_text
from Classes.player import player
from Assets.text import battle_info
from Functions.misc import print_text

def battle(player: player, enemy) -> bool:
    print(ascii_text[0])
    sleep(1)
    print_text(f"You've encountered an {enemy["name"]}\n", 0.05)
    # checks if the player and enemy are alive
    while player.hp > 0 and enemy["hp"] > 0:
        print_text(f"Your HP: {player.hp}/{player.max_hp}, Armour: {player.ac}, {enemy["name"]} HP: {enemy["hp"]}, Armour: {enemy["ac"]}, Power: {enemy["damage"]}\n", 0.05)
        # checks who goes first
        if player.speed < enemy["speed"]:
            enemy_turn(player, enemy)
            if player.hp > 0:
                sleep(1)
                player_turn(player, enemy)
        else:
            player_turn(player, enemy)
            if enemy["hp"] > 0:
                sleep(1)
                enemy_turn(player, enemy)
    # lose condition
    if player.hp <= 0:
        sleep(2)
        print(ascii_text[1])
        return False
    # win condition
    elif enemy["hp"] <= 0:
        print_text(f"{enemy["name"]} died\n", 0.05)
        sleep(2)
        print(ascii_text[2])
        print_text(f"You gained {enemy["xp"]}xp\n", 0.05)
        player.xp += enemy["xp"]
        # levels up player if reached the needed xp
        while True:
            if player.xp >= player.xp_needed:
                player.level_up()
            else:
                return True


def enemy_turn(player: player, enemy):
    value = d20()
    print_text(f"{enemy["name"]} rolled: {value}\n", 0.05)
    if value >= player.ac:
        print_text(f"{enemy["name"]} hit\n", 0.05)
        damage = d8()
        print_text(f"{enemy["name"]} rolled {damage}\n", 0.05)
        if value == 20:
            damage = damage * 2 
        print_text(f"{enemy["name"]} does {damage + enemy["damage"]} damage\n", 0.05)
        player.hp -= damage + enemy["damage"]
        print_text(f"{player.name}'s remaining hp: {player.hp}\n", 0.05)
    else:
        print("missed")
        sleep(1)


def player_turn(player: player, enemy):
    while True:
        print("1. Fight\n2. Items\n3. Info")
        choice: str = input("What do you want to do: ")
        match choice:
            case "1":
                input("press enter to roll d20 for hit:")
                value = d20()
                print_text(f"{player.name} rolled {value}\n", 0.05)
                if value >= enemy["ac"]:
                    print_text("critical hit!!!\n" if value == 20 else f"{player.name} hit\n", 0.05)
                    input("press enter to roll d8 for damage:")
                    damage = d8()
                    print_text(f"{player.name} rolled {damage}\n", 0.05)
                    if value == 20:
                        damage *= 2
                    print_text(f"{player.name} do {damage + player.equiped["damage"]} damage\n", 0.05)
                    enemy["hp"] -= damage + player.equiped["damage"]
                    print_text(f"{enemy["name"]} remaining hp: {enemy["hp"]}\n", 0.05)
                    return
                else:
                    print("missed")
                    sleep(1)
                    return
            case "2":
                i = 1
                for item in player.consumables:
                    print(f"{i}. {item["name"]} +{item["healing"]}hp")
                    i += 1
                print("0. Go back")
                item_choice = int(input("What item do you want to use: "))
                if item_choice <= len(player.consumables) and item_choice > 0:
                    print(f"used {player.consumables[item_choice - 1]["name"]}")
                    player.heal(player.consumables[item_choice - 1])
            case "3":
                print_text(battle_info, 0.05)