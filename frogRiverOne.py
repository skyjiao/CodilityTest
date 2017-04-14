# -*- coding: utf-8 -*-
__docformat__ = 'NumPy'

import pandas as pd
import numpy as np
import os, sys


def solution(X, A):
    # X = 5, A = [1, 2, 5, 3, 2]
    # N = len(A)
    counter = [0] * X
    nb_switch = 0
    for i, val in enumerate(A):
        if val <= X and counter[val - 1] != 1:
            counter[val - 1] = 1
            nb_switch += 1

        if nb_switch == X:
            return i
    return -1

if __name__ == "__main__":
    print(solution(X = 3, A = [1, 3, 1]))
