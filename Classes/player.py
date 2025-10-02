from Classes.item import item

class player:
    def __init__(self, name: str, max_hp: int, hp: int, ac: int, speed: int):
        self.name = name
        self.max_hp = max_hp
        self.hp = hp
        self.ac = ac
        self.speed = speed
        self.items: item = []

    def add_item(self, item:item):
        self.items.append(item)

    def heal(self, item: item):
        if self.hp + item.hp > self.max_hp:
            self.hp = self.max_hp
        else:
            self.hp += item.hp
            self.items.remove(item)
        print(f"{self.name} healed {item.hp} hp\nRemaining hp: {self.hp}")

        
    
