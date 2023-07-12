import random


def abilityscore_generator(characterClass):
    """Function rolls a 1D6 4 times, dropping the lowest number
    Adds the remaining numbers together saving that number
    repeats this 5 for times for a total of 6 numbers (matching ability scores count)
    Orders the distribution of dice rolls by 'favoured' stat per class
    """

    scores = []
    for x in range(6):
        score = []
        for x in range(4):
            score.append(random.randint(1, 6))

        score = sorted(score)
        score.pop(0)
        scores.append(sum(score))

    scores = sorted(scores)

    arrangedScore = {
        "STR": 0,
        "DEX": 0,
        "CON": 0,
        "INT": 0,
        "WIS": 0,
        "CHA": 0,
    }

    scoreAssignments = {
        "Barbarian": [5, 4, 3, 2, 1, 0],
        "Bard": [0, 2, 3, 4, 1, 5],
        "Cleric": [0, 1, 2, 3, 5, 4],
        "Druid": [3, 4, 1, 2, 5, 0],
        "Fighter": [5, 4, 3, 2, 1, 0],
        "Monk": [3, 5, 4, 0, 2, 1],
        "Paladin": [5, 0, 3, 2, 1, 4],
        "Ranger": [5, 4, 3, 2, 1, 0],
        "Rogue": [1, 5, 3, 2, 0, 4],
        "Sorcerer": [0, 2, 4, 5, 3, 1],
        "Warlock": [0, 2, 4, 5, 3, 1],
        "Wizard": [0, 2, 3, 5, 4, 1],
    }

    assignedScores = scoreAssignments.get(characterClass, [0, 1, 2, 3, 4, 5])

    arrangedScore = {
        "STR": scores[assignedScores[0]],
        "DEX": scores[assignedScores[1]],
        "CON": scores[assignedScores[2]],
        "INT": scores[assignedScores[3]],
        "WIS": scores[assignedScores[4]],
        "CHA": scores[assignedScores[5]],
    }

    return arrangedScore

def stat_bonus(race):
    """Races have stat bonuses which are in addition to the ability scores 
    which act as modifiers on rolls - taking random race generated and show 
    bonuses as well
    """

    arrangedScore = {
        "STR": 0,
        "DEX": 0,
        "CON": 0,
        "INT": 0,
        "WIS": 0,
        "CHA": 0,
    }

    scoreAssignments = {
        "Dwarf": [2,0, 1, 0, 0, 0],
        "Elf": [0, 2, 0, 0, 1, 0],
        "Halfling": [0, 2, 1, 0, 0, 0],
        "Dragonborn": [2, 0, 0, 0, 0, 1],
        "Gnome": [0, 1, 0, 2, 0, 0],
        "Half-Elf": [0, 0, 0, 0, 2, 2],
        "Half-Orc": [2, 0, 1, 0, 0, 0],
        "Tiefling": [0, 0, 0, 1, 0, 2],
    }

    # Humans get +1 to two skills - randomise this

    my_list = [0, 0, 0, 0, 0, 0]

    indices = [i for i in range(len(my_list)) if my_list[i] == 0]
    random_indices = random.sample(indices, 2)

    for index in random_indices:
        my_list[index] = 1

    if race != "Human":
        assignedScores = scoreAssignments.get(race, [0, 1, 2, 3, 4, 5])
    else: assignedScores = my_list

    arrangedScore = {
        "STR": assignedScores[0],
        "DEX": assignedScores[1],
        "CON": assignedScores[2],
        "INT": assignedScores[3],
        "WIS": assignedScores[4],
        "CHA": assignedScores[5],
    }


    return arrangedScore


def ability_scores_(characterClass, race):
    """Takes into account generated ability scores and the racial benefits"""
    dict1 = abilityscore_generator(characterClass)
    dict2 = stat_bonus(race)
    result = {}
    for key in dict1:
        if key in dict2:
            result[key] = dict1[key] + dict2[key]
        else:
            result[key] = dict1[key]
    for key in dict2:
        if key not in dict1:
            result[key] = dict2[key]
    return result

def modifiers_(abilityScores):
    modifiers = {}
    for key, value in abilityScores.items():
        modifiers[key] = (value - 10) // 2
    return modifiers