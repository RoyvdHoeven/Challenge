from Functions.combat import battle
from Classes.player import *
from Classes.enemy import enemy
from Classes.item import item
from time import sleep
from Functions.ascii_art import title_screen

def main():
    print(title_screen)
    sleep(2)
    player_name: str = input("Please enter your name: ")
    main_character = player(player_name, 20, 20, 5, 4)
    main_character.add_item(healing_potion)
    main_character.add_item(large_healing_potion)
    battle(main_character, goblin)

goblin = enemy("Goblin", 20, 3, 3)
healing_potion = item("Healing potion", 5)
large_healing_potion = item("Large healing potion", 10)

main()