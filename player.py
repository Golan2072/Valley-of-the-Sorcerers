#player-related code

import utility
import mobs
import items
import json
import main

class Player:
    def __init__(self, item_dict):
        self.item_dict = item_dict
        self.name = ""
        self.alive = True
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
        self.currency = 0
        self.weapon = item_dict["None"]
        self.armor = item_dict["None"]
        self.location = 0
        with open("Data/settings.json", "r") as setting_file:
            self.settings = json.load(setting_file)

    def set_max_stamina(self):
        self.max_stamina = 14 + 3 * self.physical_skill
    
    def injury(self, incoming_damage):
        damage = incoming_damage - self.armor.protection
        if damage <= 0:
            print(f"Your armor absorbed {incoming_damage} points of damage! No damage caused!")
        elif damage > 0:
            self.stamina -= int(damage)
            if self.armor.protection > 0:
                print(f"You suffered {damage} points of damage; your armor absorbed {self.armor.protection} points of damage!")
            else:
                print(f"You suffered {damage} points of damage.")
        else:
            pass
        if self.stamina <= 0:
            self.alive = False
            print("You died - GAME OVER")
        else:
            pass
    
    def healing(self, healed_amount):
        new_stamina = healed_amount + self.stamina
        if new_stamina >= self.max_stamina:
            limited_healing = self.max_stamina - self.stamina
            self.stamina = self.max_stamina
            print(f"{limited_healing} Stamina points healed.\n")
        else:
            self.stamina += healed_amount
            print (f"{healed_amount} Stamina points healed.")

    def move(self, destination):
        self.location = int(destination)

    def attack(self, mob):
        attack_roll = utility.dice(2,6) + self.combat_skill
        if attack_roll >= mob.defense:
            mob.injury(utility.dice(self.weapon.damage[0], self.weapon.damage[1]))
    
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