# Advent-of-Code/common.py
#
# This module contains the common functions used in this repository.


def parser(file):
    """parser: Input text file parser"""

    f = open(str(file), "r")
    f_list = f.readlines()
    readings = [i.strip() for i in f_list]

    return readings
