from Functions.dice_roll import d20, d8
from time import sleep
from Functions.ascii_art import ascii_text
from Classes.player import player
from Classes.enemy import enemy

def battle(player: player, enemy: enemy):
    print(ascii_text[0])
    sleep(1)
    while player.hp > 0 and enemy.hp > 0:
        print(f"Your HP: {player.hp}, {enemy.name} HP: {enemy.hp}")
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
        print(f"your remaining hp: {player.hp}")
        sleep(1)
    else:
        sleep(1)
        print("missed")

def player_turn(player: player, enemy: enemy):
    input("press enter to roll for hit:")
    value = d20()
    sleep(1)
    print(f"you rolled {value}")
    if value >= enemy.ac:
        sleep(1)
        print(f"{player.name} hit")
        sleep(1)
        input("press enter to roll for damage")
        damage = d8()
        sleep(1)
        print(f"You rolled {damage}")
        if value == 20:
            damage = damage * 2
        sleep(1)
        print(f"you do {damage} damage")
        enemy.hp -= damage
        sleep(1)
        print(f"{enemy.name} remaining hp: {enemy.hp}")
        sleep(1)
    else:
        sleep(1)
        print("missed")



      
