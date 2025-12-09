from Assets.text import *
from time import sleep
from Classes.player import player
from Functions.misc import print_text
from Functions.combat import battle
from Functions.minigames import wordle
from random import randint

def meadows(player: player) -> bool:
    position = 1
    fishing_pool = [{"name": "Large Healing Potion", "healing": 10}, {"name": "Healing Potion", "healing": 5}, "Seahorse", "Common carp", "Goldfish", "Leather boot", "Bluegill", "Catfish"]
    fishing_rod_durability = 3
    checked_chest = False
    while True:
        match position:
            case 1:
                print_text(meadows_1, 0.075)
                sleep(0.3)
                choice = input("What will you do:\n1. Approach the hut\n2. Check inventory(Recommended)\n: ")
                match choice:
                    case "1":
                        print_text(meadows_2, 0.075)
                        if battle(player, {"name": "Wild Boar", "hp": 10, "ac": 3, "damage": 0, "speed": 3, "xp": 30}):
                            position = 2
                        else:
                            return False
                    case "2":
                        player.inventory()
            case 2:
                print_text(meadows_3, 0.075)
                choice = input("What will you do:\n1. Enter the hut \n2. Go to the pond\n3. Check inventory\n: ")
                match choice:
                    case "1":
                        if "Hut key" in player.keys:
                            print_text("You try to enter the hut, you use the hut key and unlock the door\n", 0.075)
                            position = 4
                        else:
                            print_text("You try to enter the hut, but the door is locked\n", 0.075)
                    case "2":
                        position = 3
                    case "3":
                        player.inventory()
            case 3:
                print_text(meadows_4, 0.075)
                choice = input("What will you do:\n1. Use the fishing rod\n2. Talk to the witch\n3. Go back to the hut\n4. Check inventory\n: ")
                match choice:
                    case "1":
                        if not fishing_rod_durability == 0:
                            print_text("You started to fish using the fishing rod.\n", 0.075)
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
                print_text(meadows_5, 0.075)
                choice = input("What will you do:\n1. Investigate The Brewing pot\n2. Open the chest\n3. Go back outside\n4. Check inventory\n")
                match choice:
                    case "1":
                        if "Witch's Chest key" not in player.keys:
                            print_text(witch_hut_1, 0.075)
                            choice = input("Do you want to eat the suspicious stew? (y)Yes or (n)No\n")
                            match choice.lower():
                                case "y":
                                    print_text(witch_hut_2, 0.075)
                                    player.keys.append("Witch's Chest key")
                                case _:
                                    pass
                        else:
                            print_text("You already ate from the stew.\n", 0.075)
                    case "2":
                        if "Witch's Chest key" in player.keys:
                            # print_text(witch_hut_3, 0.075)
                            return True
                        else:
                            print_text("You tried to open the chest, but it is locked.\n", 0.075)
                    case "3":
                        position = 2
                    case "4":
                        player.inventory()