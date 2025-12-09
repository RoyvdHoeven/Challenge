from time import sleep
from Functions.misc import print_text
from random import randint

class player:
    def __init__(self, name: str, max_hp: int, hp: int, ac: int, speed: int):
        self.name = name
        self.max_hp = max_hp
        self.hp = hp
        self.ac = ac
        self.speed = speed
        self.level = 1
        self.xp = 0
        self.xp_needed = 100
        self.equiped = {"name": "Unarmed", "damage": 0}
        self.consumables = []
        self.weapons = []
        self.keys = []


    # function to heal the player
    def heal(self, item):
        if self.hp + item["healing"] > self.max_hp:
            self.hp = self.max_hp
        else:
            self.hp += item["healing"]
        self.consumables.remove(item)
        print(f"{self.name} healed {item["healing"]} hp\nRemaining hp: {self.hp}")

    
    # function to level up the player and raise some stats with a random integer
    def level_up(self):
        self.level += 1
        print_text(f"You leveled up to level {self.level}\n", 0.075)
        self.xp_needed *= 1.10
        self.max_hp += randint(1,5)
        self.hp = self.max_hp
        self.ac += randint(0,2)
        self.speed += randint(0,1)


    # open inventory
    def inventory(self):
        while True:
            string = f"Inventory\n{self.name}, level: {self.level}, XP: {self.xp}/{self.xp_needed}, HP: {self.hp}/{self.max_hp}, Armour: {self.ac}, Speed: {self.speed}, Equiped Weapon: {self.equiped["name"]}\n"
            print_text(string, 0.05)
            print("Consumables")
            sleep(0.3)
            consumable_count = 1
            for item in self.consumables:
                print(f" {consumable_count}.",item["name"], f"+{item["healing"]}HP")
                consumable_count += 1
                sleep(0.3)
            print("Weapons")
            sleep(0.3)
            weapon_count = 1
            for item in self.weapons:
                print(f" {weapon_count}.",item["name"], f"+{item["damage"]} Damage")
                weapon_count += 1
                sleep(0.3)
            key_count = 1
            print("Keyring")
            for item in self.keys:
                print(f" {item}")
                key_count += 1
            match int(input("What do you want to do:\n1. Use consumable\n2. Equip weapon\n0. Go back\n")):
                case 1:
                    # lets the player use an healing item
                    choice = int(input("Which consumable do you want to use: "))
                    if choice <= len(self.consumables) and choice > 0:
                        self.heal(self.consumables[choice - 1])
                case 2:
                    # lets the player equip or unequip an weapon
                    choice = int(input("Which weapon do you want to equip (press 0 to unequip current weapon): "))
                    if choice <= len(self.weapons) and choice > 0:
                        self.equiped = self.weapons[choice - 1]
                        print(f"Equiped {self.weapons[choice - 1]["name"]}")
                    if choice == 0:
                        self.equiped = {"name": "Unarmed", "damage": 0}
                        print("Unequiped weapon")
                case _:
                    return
        