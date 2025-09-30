from Functions.combat import battle
from Classes.player import *
from Classes.enemy import enemy

def main():
    battle(main_character, goblin)

main_character = player("Roy", 20, 5, 4)
goblin = enemy("Goblin", 10, 3, 3)

main()