# -*- coding: utf-8 -*-
__docformat__ = 'NumPy'

import pandas as pd
import numpy as np
import os, sys

"""
Write a function:

def solution(A)

that, given a non-empty zero-indexed array A of N integers,
returns the minimal positive integer (greater than 0) that does not occur in A.

For example, given:

  A[0] = 1
  A[1] = 3
  A[2] = 6
  A[3] = 4
  A[4] = 1
  A[5] = 2
the function should return 5.
"""

import timeit

def solution(A):
    # with complexity NlogN I think
    A = sorted(set(A))
    should_be = 1
    for val in A:
        if val > 0:
            if val == should_be:
                should_be += 1
            else:
                return should_be
    return should_be

def solution2(A):
    N = len(A)
    full_A = list(range(N+2))
    for val in A:
        if val < N + 1 and val > 0:
            full_A[val] = 0

    for val in full_A:
        if val > 0:
            return val

if __name__ == "__main__":
    t = timeit.Timer("solution2([1])")
    t.timeit()

