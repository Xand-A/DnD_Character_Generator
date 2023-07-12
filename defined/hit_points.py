import random

def rollHP(characterClass,modifiers):
    my_hp = 0
    if characterClass == 'Barbarian':
        die = random.randint(1,8)
        my_hp = my_hp + die + modifiers['CON']
    elif characterClass == 'Fighter' or characterClass == 'Paladin' or characterClass == 'Ranger':
        die = random.randint(1,10)
        my_hp = my_hp + die + modifiers['CON']
    elif characterClass == 'Cleric' or characterClass == 'Druid' or characterClass == 'Bard'\
        or characterClass == 'Monk' or characterClass == 'Rogue' or characterClass == 'Warlock':
            die = random.randint(1,8)
            my_hp = my_hp + die + modifiers['CON']
    else:  # You must be a Wizard or Mage
            die = random.randint(1,6)
            my_hp = my_hp + die + modifiers['CON']

    return my_hp
