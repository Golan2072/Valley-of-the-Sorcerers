#mob-related code

import utility

class Mob:
    def __init__(self, item_dict):
        self.name = "Default"
        self.alive = True
        self.stamina = 14
        self.armor = item_dict["None"]
        self.combat_skill = 0
        self.weapon = item_dict["None"]
        self.currency = 0
        self.xp = 1
    
    def set_max_stamina(self):
        self.max_stamina = 14 + 3 * self.physical_skill
    
    def injury(self, incoming_damage):
        damage = incoming_damage - self.armor.protection
        if damage <= 0:
            print(f"The {self.name}'s armor absorbed {incoming_damage} points of damage! No damage caused!")
        elif damage > 0:
            self.stamina -= int(damage)
            if self.armor.protection > 0:
                print(f"{self.name} suffered {damage} points of damage; its armor absorbed {self.armor.protection} points of damage!")
            else:
                print(f"{self.name} suffered {damage} points of damage.")
        else:
            pass
        if self.stamina <= 0:
            self.alive = False
            print(f"{self.name} was killed!")
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
        print(f"{self.name} rolled {attack_roll}!")
        if attack_roll >= 8:
            print(f"{self.name} hit the {mob.name}!")
            mob.injury(utility.dice(self.weapon.damage[0], self.weapon.damage[1]))
        else:
            print(f"{self.name} missed the {mob.name}!")