from Functions.combat import battle
from Functions.misc import print_text
from Classes.player import player
from time import sleep
from Assets.ascii_art import title_screen
from Assets.text import *
from Levels.meadows import meadows

def main():
    player_name: str = input("Please enter your name: ")
    # sleep(0.5)
    # print_text(intro_text, 0.075)
    # print_text("Welcome to ...", 0.3)
    # sleep(1)
    # print(title_screen)
    # sleep(2)

    healing_potion = {"name": "Healing Potion", "healing": 5}
    wooden_stick = {"name": "Wooden Stick", "damage": 2}

    main_character = player(player_name, 20, 20, 5, 4)
    main_character.consumables.append(healing_potion)
    main_character.weapons.append(wooden_stick)
    if not meadows(main_character):
        print_text("Game over", 0.075)
    else:
        print_text("The end", 0.080)


main()