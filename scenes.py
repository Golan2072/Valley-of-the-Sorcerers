#scene-related code

import utility

class Scene:
    def __init__(self, items_dict):
        self.number = 0
        self.type = "Room"
        self.default_state = True
        self.description = "PLACEHOLDER"
        self.alternative_description = "PLACEHOLDER2"
        self.default_choices = {}
        self.alternative_choices = {}
        self.content = []

    def describe(self):
        if self.default_state:
            print(f"{self.description}")
        elif not self.default_state:
            print(f"{self.alternative_description}")
        else:
            print (f"\n")
    
    def choices(self):
        if self.default_state:
            player_choices = self.default_choices
        elif not self.default_state:
            player_choices = self.alternative_choices
        else:
            player_choices = f"\n"
