from Functions.dice_roll import d20, d8
from time import sleep
from Assets.ascii_art import ascii_text
from Classes.player import player
from Classes.enemy import enemy
from Assets.text import battle_info

def battle(player: player, enemy: enemy):
    print(f"You've encountered an {enemy.name}")
    sleep(1)
    print(ascii_text[0])
    sleep(1)
    while player.hp > 0 and enemy.hp > 0:
        print(f"Your HP: {player.hp}/{player.max_hp}, Armour: {player.ac}, {enemy.name} HP: {enemy.hp}, Armour: {enemy.ac}")
        sleep(1)
        if player.speed < enemy.speed:
            enemy_turn(player, enemy)
            if player.hp > 0:
                sleep(1)
                player_turn(player, enemy)
        else:
            player_turn(player, enemy)
            if enemy.hp > 0:
                sleep(1)
                enemy_turn(player, enemy)
    if player.hp <= 0:
        sleep(2)
        print(ascii_text[1])
    elif enemy.hp <= 0:
        print(f"{enemy.name} died")
        sleep(2)
        print(ascii_text[2])

def enemy_turn(player: player, enemy: enemy):
    value = d20()
    sleep(1)
    print(f"{enemy.name} rolled: {value}")
    if value >= player.ac:
        sleep(1)
        print(f"{enemy.name} hit")
        damage = d8()
        sleep(1)
        print(f"{enemy.name} rolled {damage}")
        if value == 20:
            damage = damage * 2 
        sleep(1)
        print(f"{enemy.name} does {damage} damage")
        player.hp -= damage
        sleep(1)
        print(f"{player.name}'s remaining hp: {player.hp}")
        sleep(1)
    else:
        sleep(1)
        print("missed")

def player_turn(player: player, enemy: enemy):
    print("1. Fight\n2. Items\n3. Info")
    choice: str = input("What do you want to do: ")
    match choice:
        case "1":
            input("press enter to roll d20 for hit:")
            value = d20()
            sleep(1)
            print(f"{player.name} rolled {value}")
            if value >= enemy.ac:
                sleep(1)
                print("critical hit!!!" if value == 20 else f"{player.name} hit")
                sleep(1)
                input("press enter to roll d8 for damage")
                damage = d8()
                sleep(1)
                print(f"{player.name} rolled {damage}")
                if value == 20:
                    damage = damage * 2
                sleep(1)
                print(f"{player.name} do {damage} damage")
                enemy.hp -= damage
                sleep(1)
                print(f"{enemy.name} remaining hp: {enemy.hp}")
                sleep(1)
            else:
                sleep(1)
                print("missed")
        case "2":
            i = 1
            for item in player.items:
                print(f"{i}. {item.name} +{item.hp}hp")
                i += 1
            print("0. Go back")
            item_choice = int(input("What item do you want to use: "))
            if item_choice <= len(player.items) and item_choice > 0:
                print(f"used {player.items[item_choice - 1].name}")
                player.heal(player.items[item_choice - 1])
            else:
                player_turn(player, enemy)
        case "3":
            info_choice = input("1. Combat\n2. Healing items\n0. Go back\nOn what do you need info: ")
            match info_choice:
                case "1":
                    pass
                case "2":
                    pass
                case _:
                    player_turn(player, enemy)

        case _:
            player_turn(player, enemy)



      
