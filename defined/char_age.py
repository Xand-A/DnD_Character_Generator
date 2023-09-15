from .char_details import RACES
import random
from random import randint


def char_age(self):
    """
    Give character an appropriate age for given race
    """
    r = randint(1, 100)  # random percentage
    r_a_mod = random.randrange(86, 99) / 100  # age modifier

    # the following are ordered according to dnd_world
    maxa = [433, 845, 167, 98, 94, 522, 222, 80, 102]  # max ages
    aa = [17, 17, 17, 17, 15, 20, 17, 16, 17]  # adulthood ages
    r_a_check = [0.74, 0.88, 0.85, 0.85, 0.70, 0.82, 0.88, 0.79, 0.82]  # age check
    alter_chance = [89, 89, 89, 89, 85, 89, 89, 82, 89]  # age alter chance

    for i in range(len(RACES)):
        if self == RACES[i]:
            age = randint(1, (maxa[i] - aa[i]) + aa[i])
            if age >= int(r_a_check[i] * maxa[i]) and r < alter_chance[i]:
                age = int(age * r_a_mod)
            break

    return age
