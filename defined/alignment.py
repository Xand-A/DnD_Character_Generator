import random

from .char_details import ALIGN_LIST


def align_finder():
    """Function to determine a characters alignment for backstory etc"""

    align1 = ALIGN_LIST[0][random.randint(0, len(ALIGN_LIST) - 1)]
    align2 = ALIGN_LIST[1][random.randint(0, len(ALIGN_LIST) - 1)]

    align = align1 + " " + align2

    if align == "Neutral Neutral":
        return "Neutral"
    else:
        align

    return align
