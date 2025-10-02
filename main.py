from Functions.combat import battle
from Classes.player import *
from Classes.enemy import enemy
from Classes.item import item
from time import sleep
from Assets.ascii_art import title_screen
from Assets.text import *

def main():
    player_name: str = input("Please enter your name: ")
    sleep(0.5)
    for char in intro_text:
        sleep(0.075)
        print(char, end='', flush=True)
    for char in welcome:
        sleep(0.3)
        print(char, end='', flush=True)
    sleep(1)
    print(title_screen)
    sleep(2)
    main_character = player(player_name, 20, 20, 5, 4)
    main_character.add_item(healing_potion)
    main_character.add_item(large_healing_potion)
    battle(main_character, goblin)


goblin = enemy("wild Boar", 20, 3, 3)
healing_potion = item("Healing potion", 5)
large_healing_potion = item("Large healing potion", 10)

main()