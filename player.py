#player-related code

import utility
import mobs
import items
import json

class Player (mobs.Mob):
    def __init__(self, item_dict):
        self.item_dict = item_dict
        super().__init__(self.item_dict)
        self.name = "Avatar"
        self.max_stamina = 14
        self.stamina = 14
        self.charclass = "Fighter"
        self.combat_skill = 0
        self.physical_skill = 0
        self.survival_skill = 0
        self.tech_skill = 0
        self.stealth_skill = 0
        self.social_skill = 0
        self.knowledge_skill = 0
        self.inventory = {}
        self.rations = 0
        self.xp_gained = 0
        self.level = 1
        self.weapon = item_dict["Fists"]
        self.location = 0
        with open("Data/settings.json", "r") as setting_file:
            self.settings = json.load(setting_file)
    
    def inventory_add(self, item):  #item is an item object from items.py
        if item in self.inventory.keys():
            self.inventory[item] += 1
        else:
            self.inventory[item] = 1
        print(f"{item.name} added to inventory.")

    def inventory_remove(self, item):
        if item not in self.inventory.keys():
            print("No such item.")
            pass
        elif item in self.inventory.keys() and self.inventory[item] > 1:
            self.inventory[item] -= 1
            print(f"{item.name} Removed from inventory.")
        elif item in self.inventory.keys() and self.inventory[item] == 1:
            self.inventory.pop(item)
            print(f"{item.name} Removed from inventory.")
        else:
            pass

    def pay(self, price):
        if price > self.currency:
            print (f"Insufficient {self.settings["currency"]} for payment.")
            return False
        elif price <= self.currency:
            print (f"{price} {self.settings["currency"]} traded. {self.currency - price} {self.settings["currency"]} remaining.")
            self.currency -= price
            return True
    
    def buy(self, item):    #item is an item object from items.py
        purchase = self.pay(item.price)
        if purchase:
            self.inventory_add(item)
        else:
            pass

    def show_inventory(self):   #item is an item object from items.py
        for item in self.inventory.keys():
            print(f"{self.inventory[item]}x {item.name}")
    
    def equip_weapon(self, weapon): #weapon is an item object from items.py
        if self.weapon == self.item_dict["None"]:
            self.weapon = weapon
            print(f"{self.weapon.name} equipped!")
        elif self.weapon != self.item_dict["None"]:
            old_weapon = self.weapon.name
            self.weapon = weapon
            print(f"{old_weapon} unequipped; {self.weapon.name} equipped!")
        else:
            pass
    
    def equip_armor(self, armor): #armor is an item object from items.py
        if self.armor == self.item_dict["None"]:
            self.armor = armor
            print(f"{self.armor.name} equipped!")
        elif self.armor != self.item_dict["None"]:
            old_armor = self.armor.name
            self.armor = armor
            print(f"{old_armor} unequipped; {self.armor.name} equipped!")
        else:
            pass

    def gain_xp(self, xp):
        self.xp_gained += xp
        level_dict = {2: 2000, 3: 4000, 4: 8000, 5: 16000, 6: 32000, 7: 64000, 8: 128000, 9: 256000, 10: 512000}
        print(f"{xp} Experience gained! Total Experience {self.xp_gained}")
        if self.level in range (0, 9):
            if self.xp_gained >= level_dict[self.level+1]:
                self.level += 1
                print(f"You have reached level {self.level}!")
        else:
            pass
    
    def injury(self, incoming_damage):
        damage = incoming_damage - self.armor.protection
        if damage <= 0:
            print(f"Your armor absorbed {incoming_damage} points of damage! No damage caused!")
        elif damage > 0:
            self.stamina -= int(damage)
            if self.armor.protection > 0:
                print(f"You suffered {damage} points of damage; its armor absorbed {self.armor.protection} points of damage!")
            else:
                print(f"You suffered {damage} points of damage.")
        else:
            pass
        if self.stamina <= 0:
            self.alive = False
            print(f"You were killed! Game Over!")
        else:
            pass