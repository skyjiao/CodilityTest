# -*- coding: utf-8 -*-
__docformat__ = 'NumPy'

import pandas as pd
import numpy as np
import os, sys
from itertools import combinations, combinations_with_replacement, permutations


def solution(A):
    N = len(A)
    if N == 0:
        return "impossible"

    if N == 1:
        if A[0] == 0:
            return "R"
        else:
            return "impossible"

    gen = combinations_with_replacement([1, 2, 3], N)
    for color_map_source in gen:
        for color_map in set(permutations(color_map_source)):
            mystr = ""
            red_list, green_list, blue_list = [], [], []
            for i, color in enumerate(color_map):
                if color == 1:
                    red_list.append(A[i])
                    mystr += "R"
                elif color == 2:
                    green_list.append(A[i])
                    mystr += "G"
                else:
                    blue_list.append(A[i])
                    mystr += "B"

                if sum(red_list) == sum(green_list) == sum(blue_list):
                    print(color_map)
                    return mystr

    # with two colors
    gen = combinations_with_replacement([1, 2], N)
    for color_map_source in gen:
        for color_map in set(permutations(color_map_source)):
            mystr = ""
            red_list, green_list = [], []
            for i, color in enumerate(color_map):
                if color == 1:
                    red_list.append(A[i])
                    mystr += "R"
                else:
                    green_list.append(A[i])
                    mystr += "G"

                if sum(red_list) == sum(green_list):
                    print(color_map)
                    return mystr

    # only one color
    if sum(A) == 0:
        return "R"*N

    return "impossible"

if __name__ == "__main__":
    print(solution([3, 7, 2, 5, 4]))