# -*- coding: utf-8 -*-
__docformat__ = 'NumPy'

import pandas as pd
import numpy as np
import os, sys
"""
A non-empty zero-indexed array A consisting of N integers is given.

A permutation is a sequence containing each element from 1 to N once, and only once.

For example, array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
is a permutation, but array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
is not a permutation, because value 2 is missing.

The goal is to check whether array A is a permutation.
"""

def solution(A):
    # write your code in Python 2.7
    N = len(A)
    full_A = list(range(1, N+1))
    for val in A:
        if val > N:
            return 0
        if full_A[val - 1] == 0:
            return 0
        full_A[val - 1] = 0

    for val in full_A:
        if val != 0:
            return 0

    return 1

def solution2(A):
    N = len(A)
    counter = [0]*N

    for val in A:
        if not 1 <= val <= N:
            return 0
        else:
            if counter[val - 1] == 1:
                return 0
            else:
                counter[val - 1] = 1
    return 1

if __name__ == "__main__":
    print(solution2([1]))