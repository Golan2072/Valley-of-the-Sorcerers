#scene-related code

import utility

class Scene:
    def __init__(self, number):
        self.number = number
        self.default_state = True
        self.description = ""
        self.alternative_description = ""
        self.default_choices = {}
        self.alternative_choices = {}
        self.content = []

    def describe(self):
        if self.default_state:
            print(f"{self.description} \n")
        elif not self.default_state:
            print(f"{self.alternative_description} \n")
        else:
            print (f"\n")
    
    def choices(self):
        if self.default_state:
            player_choices = self.default_choices
        elif not self.default_state:
            player_choices = self.alternative_choices
        else:
            player_choices = f"\n"
