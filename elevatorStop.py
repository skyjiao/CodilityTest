# -*- coding: utf-8 -*-
__docformat__ = 'NumPy'

import pandas as pd
import numpy as np
import os, sys

def solution(A, B, M, X, Y):
    # Y: max weight
    # X: max number
    stop_count = 0
    tot_weight = 0
    person_count = 0
    floor_list = []

    person_idx = 0
    reset = False

    while person_idx < len(A):
        if (tot_weight + A[person_idx]) <= Y and person_count + 1 <= X:
            tot_weight += A[person_idx]
            person_count += 1
            floor_list.append(B[person_idx])
            if person_idx == len(A) - 1:
                reset = True

            person_idx += 1
        else:
            reset = True

        if reset:
            stop_count += len(set(floor_list)) + 1
            tot_weight = 0
            person_count = 0
            floor_list = []
            reset = False
    return stop_count

if __name__ == "__main__":
    A = [40, 40, 100, 80, 20]
    B = [3, 3, 2, 2, 3]
    print(solution(A, B, 3, 5, 200))