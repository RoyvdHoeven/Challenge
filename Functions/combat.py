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
    sleep(1)
    # checks if the player and enemy are alive
    while player.hp > 0 and enemy["hp"] > 0:
        print(f"Your HP: {player.hp}/{player.max_hp}, Armour: {player.ac}, {enemy["name"]} HP: {enemy["hp"]}, Armour: {enemy["ac"]}, Power: {enemy["damage"]}")
        sleep(1)
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
        print(f"{enemy["name"]} died")
        sleep(2)
        print(ascii_text[2])
        print_text(f"You gained {enemy["xp"]}xp\n", 0.075)
        player.xp += enemy["xp"]
        # levels up player if reached the needed xp
        while True:
            if player.xp >= player.xp_needed:
                player.level_up()
            else:
                return True


def enemy_turn(player: player, enemy):
    value = d20()
    sleep(1)
    print(f"{enemy["name"]} rolled: {value}")
    if value >= player.ac:
        sleep(1)
        print(f"{enemy["name"]} hit")
        damage = d8()
        sleep(1)
        print(f"{enemy["name"]} rolled {damage}")
        if value == 20:
            damage = damage * 2 
        sleep(1)
        print(f"{enemy["name"]} does {damage + enemy["damage"]} damage")
        player.hp -= damage + enemy["damage"]
        sleep(1)
        print(f"{player.name}'s remaining hp: {player.hp}")
        sleep(1)
    else:
        sleep(1)
        print("missed")


def player_turn(player: player, enemy):
    while True:
        print("1. Fight\n2. Items\n3. Info")
        choice: str = input("What do you want to do: ")
        match choice:
            case "1":
                input("press enter to roll d20 for hit:")
                value = d20()
                sleep(1)
                print(f"{player.name} rolled {value}")
                if value >= enemy["ac"]:
                    sleep(1)
                    print("critical hit!!!" if value == 20 else f"{player.name} hit")
                    sleep(1)
                    input("press enter to roll d8 for damage:")
                    damage = d8()
                    sleep(1)
                    print(f"{player.name} rolled {damage}")
                    if value == 20:
                        damage *= 2
                    sleep(1)
                    print(f"{player.name} do {damage + player.equiped["damage"]} damage")
                    enemy["hp"] -= damage + player.equiped["damage"]
                    sleep(1)
                    print(f"{enemy["name"]} remaining hp: {enemy["hp"]}")
                    sleep(1)
                    return
                else:
                    sleep(1)
                    print("missed")
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
                print_text(battle_info, 0.075)