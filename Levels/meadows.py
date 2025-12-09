from Assets.text import *
from time import sleep
from Classes.player import player
from Functions.misc import print_text
from Functions.combat import battle
from Functions.minigames import wordle
from random import randint
from Functions.misc import d20

def meadows(player: player) -> bool:
    position = 1
    fishing_pool = [{"name": "Large Healing Potion", "healing": 10}, {"name": "Healing Potion", "healing": 5}, "Seahorse", "Common carp", "Goldfish", "Leather boot", "Bluegill", "Catfish"]
    fishing_rod_durability = 3
    checked_chest = False
    while True:
        match position:
            case 1:
                print_text(meadows_1, 0.05)
                sleep(0.3)
                choice = input("What will you do:\n1. Approach the hut\n2. Check inventory\n: ")
                match choice:
                    case "1":
                        print_text(meadows_2, 0.05)
                        if battle(player, {"name": "Wild Boar", "hp": 10, "ac": 3, "damage": 0, "speed": 3, "xp": 115}):
                            position = 2
                        else:
                            return False
                    case "2":
                        player.inventory()
            case 2:
                print_text(meadows_3, 0.05)
                choice = input("What will you do:\n1. Enter the hut \n2. Go to the pond\n3. Check inventory\n: ")
                match choice:
                    case "1":
                        if "Hut key" in player.keys:
                            print_text("You try to enter the hut, you use the hut key and unlock the door\n", 0.05)
                            position = 4
                        else:
                            print_text("You try to enter the hut, but the door is locked\n", 0.05)
                    case "2":
                        position = 3
                    case "3":
                        player.inventory()
            case 3:
                print_text(meadows_4, 0.05)
                choice = input("What will you do:\n1. Use the fishing rod\n2. Talk to the witch\n3. Go back to the hut\n4. Check inventory\n: ")
                match choice:
                    case "1":
                        if not fishing_rod_durability == 0:
                            print_text("You started to fish using the fishing rod.\n", 0.05)
                            fishing_loot = randint(0,len(fishing_pool) - 1)
                            if type(fishing_pool[fishing_loot]) == dict:
                                print_text(f"BITE!!!\nYou pull your fishing rod out of the water and find a {fishing_pool[fishing_loot]["name"]}\nYou put it in your inventory\n", 0.05)
                                player.consumables.append(fishing_pool[fishing_loot])
                                fishing_rod_durability -=1
                            elif fishing_pool[fishing_loot] == "Seahorse":
                                print_text("BITE!!!\nYou pull your fishing rod out of the water and find a Seahorse.\nWhen you try to grab the seahorse, it dissapears into thin air\nYou hallucinated it, Seahorses don't exist.\n", 0.05)
                                fishing_rod_durability -= 1
                            else:
                                print_text(f"BITE!!!\nYou pull your fishing rod out of the water and find a {fishing_pool[fishing_loot]}\nYou unhook it and throw it back into the water.\n", 0.05)
                                fishing_rod_durability -= 1
                            fishing_pool.pop(fishing_loot)
                            if fishing_rod_durability > 0:
                                print_text(f"Fishing rod has {fishing_rod_durability} uses left\n", 0.05)
                            if fishing_rod_durability == 0:
                                print_text("You carefully put down the fishing rod but it broke into a million pieces\n", 0.05)
                        else:
                            print_text("The fishing rod is still broken\n", 0.05)
                    case "2":
                        if not "Hut key" in player.keys:
                            print_text(witch_1, 0.05)
                            sleep(0.75)
                            if wordle("witch"):
                                print_text(witch_2, 0.05)
                                print("\nYou put the key in your inventory.\n")
                                player.keys.append("Hut key")
                            else:
                                if not battle(player, {"name": "Wild Boar", "hp": 10, "ac": 3, "damage": 0, "speed": 3, "xp": 30}):
                                    return False
                        else:
                            if checked_chest:
                                print_text(witch_4, 0.05)
                            else:
                                print_text(witch_3, 0.05)
                    case "3":
                        position = 2
                    case "4":
                        player.inventory()
            case 4:
                print_text(meadows_5, 0.05)
                choice = input("What will you do:\n1. Investigate The Brewing pot\n2. Open the chest\n3. Go back outside\n4. Check inventory\n")
                match choice:
                    case "1":
                        if "Witch's Chest key" not in player.keys:
                            print_text(witch_hut_1, 0.05)
                            choice = input("Do you want to eat the suspicious stew? (y)Yes or (n)No\n")
                            match choice.lower():
                                case "y":
                                    print_text(witch_hut_2, 0.05)
                                    player.keys.append("Witch's Chest key")
                                case _:
                                    pass
                        else:
                            print_text("You already ate from the stew.\n", 0.05)
                    case "2":
                        if "Witch's Chest key" in player.keys:
                            print_text(witch_hut_3, 0.05)
                            choice = input("1. \033[32mI was just uhh...checking...\33[0m\n2. \033[32mI uhh... just fell down...I wasn't opening it(perception check)\33[0m\n: ")
                            fight = True
                            match choice:
                                case "1":
                                    print_text("\033[34mChecking for what?\n Checking for things to steal?\n\033[0m", 0.05)
                                case "2":
                                    input(print_text("Roll d20 for peception check(10 needed): ", 0.05))
                                    roll = d20()
                                    print_text(f"You rolled {roll}\n", 0.05)
                                    if roll >= 10:
                                        print_text("Perception check succesfull", 0.05)
                                        fight = False
                                        print_text("\033[34moh...well, get up then and stay away from my stuff\n\033[0m", 0.05)
                                        print_text("The witch walks out and leaves you alone in the hut again", 0.05)
                                    else:
                                        print_text("\033[34mYou fell down? Do you really think im that stupid?\n\033[0m", 0.05)
                            if fight:
                                if battle(player, {"name": "Witch", "hp": 25, "ac": 5, "damage": 2, "speed": 5, "xp": 300}):
                                    print_text("", 0.05)
                                else:
                                    return False
                            print_text("You open the chest and find an bronze sword", 0.05)
                            bronze_sword = {"name": "Bronze_sword", "damage": 6}
                            player.weapons.append(bronze_sword)
                            print_text("Bronze sword has been added to your inventory\n", 0.05)
                            print_text("As you put your new weapon in your inventory, you hear a loud shriek from under the floor, the floor starts to crumble.\n", 0.05)
                            print_text("The floor starts to break under your feet, you realize the hut was build on top of a pit as you fall down...\n", 0.05)
                            return True
                        else:
                            print_text("You tried to open the chest, but it is locked.\n", 0.05)
                    case "3":
                        position = 2
                    case "4":
                        player.inventory()