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
            if self.item_source_dict[item]["equippable"] == "True":
               self.item_dict[self.item_source_dict[item]["name"]].equippable = True
            elif self.item_source_dict[item]["equippable"] == "False":
               self.item_dict[self.item_source_dict[item]["name"]].equippable = False 

if __name__ == "__main__":
    game = Game()
    avatar = player.Player(game.item_dict)
    avatar.armor = game.item_dict["Leather Jacket"]
    avatar.weapon = game.item_dict["None"]
    avatar.injury(10)
    avatar.currency = 25
    print(avatar.stamina)
    avatar.buy(game.item_dict["Chainsword"])
    avatar.equip_weapon(game.item_dict["Chainsword"])
    avatar.buy(game.item_dict["Ration"])
    avatar.buy(game.item_dict["Ration"])
    avatar.buy(game.item_dict["Ration"])
    avatar.inventory_remove(game.item_dict["Ration"])
    avatar.show_inventory()
