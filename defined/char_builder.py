from defined.char_details import (RACES, 
                                 CLASSES,
                                 GENDER)
#from defined.name_generator import char_name
from defined.ability_scores import  ability_scores_, modifiers_
from defined.alignment import align_finder
from defined.char_age import char_age
#from defined.name_generator import char_name
from defined.hit_points import rollHP

import random

class character:
    def __init__(self):
        self.race = RACES[random.randint(0, len(RACES) - 1)]
        self.characterClass = CLASSES[random.randint(0, len(CLASSES) - 1)]
        self.gender = GENDER[random.randint(0, len(GENDER) - 1)]
        #self.name = char_name(self.race, self.gender)
        self.abilityScores = ability_scores_(self.characterClass, self.race)
        self.modifiers = modifiers_(self.abilityScores)
        self.hitPoints = rollHP(self.characterClass, self.modifiers)
        self.alignment = align_finder()
        self.age = char_age(self.race)
