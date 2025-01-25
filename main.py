#main game file

import items
import mobs
import player
import scenes
import utility
import json


class Game:
    def __init__(self):
        with open("Data/settings.json", "r") as setting_file:
            self.settings = json.load(setting_file)       
        with open("Data/items.json", "r") as items_file:
            self.item_source_dict = json.load(items_file)
        self.item_dict = {}
        for item in self.item_source_dict:
            self.item_dict[self.item_source_dict[item]["name"]] = items.Item()
            self.item_dict[self.item_source_dict[item]["name"]].name = self.item_source_dict[item]["name"]
            self.item_dict[self.item_source_dict[item]["name"]].price = self.item_source_dict[item]["price"]
            self.item_dict[self.item_source_dict[item]["name"]].damage = (self.item_source_dict[item]["damage"]["number"], self.item_source_dict[item]["damage"]["sides"])
            self.item_dict[self.item_source_dict[item]["name"]].itemtype = self.item_source_dict[item]["itemtype"]
            self.item_dict[self.item_source_dict[item]["name"]].protection = self.item_source_dict[item]["protection"]
            self.item_dict[self.item_source_dict[item]["name"]].description = self.item_source_dict[item]["description"]
            if self.item_source_dict[item]["equippable"] == "True":
               self.item_dict[self.item_source_dict[item]["name"]].equippable = True
            elif self.item_source_dict[item]["equippable"] == "False":
               self.item_dict[self.item_source_dict[item]["name"]].equippable = False
        self.mobs_dict = {}
        with open("Data/mobs.json", "r") as mobs_file:
            self.mobs_source_dict = json.load(mobs_file)
        for mob in self.mobs_source_dict:
            self.mobs_dict[self.mobs_source_dict[mob]["name"]] = mobs.Mob(self.item_dict)
            self.mobs_dict[self.mobs_source_dict[mob]["name"]].name = self.mobs_source_dict[mob]["name"]
            self.mobs_dict[self.mobs_source_dict[mob]["name"]].stamina = self.mobs_source_dict[mob]["stamina"]
            self.mobs_dict[self.mobs_source_dict[mob]["name"]].armor = self.item_dict[self.mobs_source_dict[mob]["armor"]]
            self.mobs_dict[self.mobs_source_dict[mob]["name"]].combat_skill = self.mobs_source_dict[mob]["combat_skill"]
            self.mobs_dict[self.mobs_source_dict[mob]["name"]].weapon =  self.item_dict[self.mobs_source_dict[mob]["weapon"]]
            self.mobs_dict[self.mobs_source_dict[mob]["name"]].currency = self.mobs_source_dict[mob]["currency"]
            self.mobs_dict[self.mobs_source_dict[mob]["name"]].xp = self.mobs_source_dict[mob]["xp"]
            self.mobs_dict[self.mobs_source_dict[mob]["name"]].description = self.mobs_source_dict[mob]["description"]
        self.avatar = player.Player(self.item_dict)


def combat(mob, player):
    print (f"{mob.name} attacks you! Prepare for battle!")
    round = 1
    attack = False
    flee = False
    while True:
        utility.clear_screen()
        print(f"Combat - Round {round}!")
        while True:
            choice = input("What do you want to do? Enter A to attack, F to flee, X to exit game: ")
            if choice.lower() == "a":
                attack = True
                flee = False
                break
            elif choice.lower() == "f":
                attack = False
                flee = True
                break
            elif choice.lower() == "x":
                quit()
            else:
                print("Invalid choice, please re-enter your choice.")
        if attack:
            player.attack(mob)
            mob.attack(player)
            round +=1
            if player.alive and mob.alive:
                input("Press ENTER to continue")
                pass
            elif not player.alive:
                input("Press ENTER to continue")
                break
            elif player.alive and not mob.alive:
                print(f"Victory! You defeated the {mob.name}")
                player.gain_xp(mob.xp)
                player.currency += mob.currency
                input("Press ENTER to continue")
                break

        elif not attack:
            if flee:
                evasion_roll = utility.dice(2, 6) + player.stealth_skill
                print (f"You rolled {evasion_roll} to evade!")
                if evasion_roll >= 8:
                    print(f"You evaded the {mob.name}!")
                    break
                else:
                    print(f"You failed to evade the {mob.name}!")
                    round +=1
        else:
            break


if __name__ == "__main__":
    game = Game()
    combat(game.mobs_dict["Velociraptor"], game.avatar)