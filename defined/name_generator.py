import random

from defined.name_list import *


def char_name(race, gender):
    """Function to return character name based on character race and gender"""
    name = ""

    if race == "Dwarf" and gender == "Female":
        name = random.choice(dwarf_first_names_female)
    elif race == "Dwarf" and gender == "Male":
        name = random.choice(dwarf_first_names_male)
    elif race == "Dragonborn" and gender == "Female":
        name = random.choice(dragonborn_first_names_female)
    elif race == "Dragonborn" and gender == "Male":
        name = random.choice(dragonborn_first_names_male)
    elif race == "Elf" and gender == "Female":
        name = random.choice(elf_first_names_female)
    elif race == "Elf" and gender == "Male":
        name = random.choice(elf_first_names_male)
    elif race == "Gnome" and gender == "Female":
        name = random.choice(gnome_first_names_female)
    elif race == "Gnome" and gender == "Male":
        name = random.choice(gnome_first_names_male)
    elif race == "Halfling" and gender == "Female":
        name = random.choice(halfling_first_names_female)
    elif race == "Halfling" and gender == "Male":
        name = random.choice(halfling_first_names_male)
    elif race == "Half-Elf" and gender == "Female":
        name = random.choice(half_elf_first_names_female)
    elif race == "Half-Elf" and gender == "Male":
        name = random.choice(half_elf_first_names_male)
    elif race == "Half-Orc" and gender == "Female":
        name = random.choice(half_orc_first_names_female)
    elif race == "Half-Orc" and gender == "Male":
        name = random.choice(half_orc_first_names_male)
    elif race == "Human" and gender == "Female":
        name = random.choice(human_first_names_female)
    elif race == "Human" and gender == "Male":
        name = random.choice(human_first_names_male)
    elif race == "Tiefling" and gender == "Female":
        name = random.choice(tiefling_first_names_female)
    elif race == "Tiefling" and gender == "Male":
        name = random.choice(tiefling_first_names_male)
    else:
        name = "Unknown"

    match race:
        case "Dwarf":
            name += f" {random.choice(dwarf_last_names)}"
        case "Elf":
            name += f" {random.choice(elf_last_names)}"
        case "Halfling":
            name += f" {random.choice(halfling_last_names)}"
        case "Human":
            name += f" {random.choice(human_last_names)}"
        case "Dragonborn":
            name += f" {random.choice(dragonborn_last_names)}"
        case "Gnome":
            name += f" {random.choice(gnome_last_names)}"
        case "Half-Elf":
            name += f" {random.choice(half_elf_last_names)}"
        case "Half-Orc":
            name += f" {random.choice(half_orc_last_names)}"
        case "Tiefling":
            name += f" {random.choice(tiefling_last_names)}"

    return name
