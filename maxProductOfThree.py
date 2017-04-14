# -*- coding: utf-8 -*-
__docformat__ = 'NumPy'

import pandas as pd
import numpy as np
import os, sys

"""
A non-empty zero-indexed array A consisting of N integers is given.
The product of triplet (P, Q, R) equates to A[P] * A[Q] * A[R] (0 ≤ P < Q < R < N).

For example, array A such that:

  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6
contains the following example triplets:

(0, 1, 2), product is −3 * 1 * 2 = −6
(1, 2, 4), product is 1 * 2 * 5 = 10
(2, 4, 5), product is 2 * 5 * 6 = 60
Your goal is to find the maximal product of any triplet.
"""

from functools import reduce

def solution(A):
    # write your code in Python 2.7
    pos_A = [x for x in A if x >= 0]
    neg_A = [x for x in A if x < 0]

    if len(neg_A) == 0:
        sorted_pos_A = sorted(pos_A, reverse = True)[:3]
        return reduce(lambda x, y: x * y, sorted_pos_A)
    elif len(neg_A) == 1:
        if len(pos_A) == 2:
            return neg_A[0] * pos_A[0] * pos_A[1]
        else:
            sorted_pos_A = sorted(pos_A, reverse=True)[:3]
            return reduce(lambda x, y: x * y, sorted_pos_A)

    elif len(neg_A) >= 2:
        if len(pos_A) == 0:
            return reduce(lambda x, y: x * y, sorted(neg_A, reverse = True)[:3])
        elif len(pos_A) == 1:
            # sorted_pos_A = sorted(pos_A, reverse = True)[:3]
            neg_top3 = sorted(neg_A)
            return pos_A[0] * neg_top3[0] * neg_top3[1]
        elif len(pos_A) == 2:
            neg_top3 = sorted(neg_A)
            return max(pos_A) * neg_top3[0] * neg_top3[1]
        else:
            # len(pos_A) >= 3
            neg_top3 = sorted(neg_A)
            pos_top3 = sorted(pos_A, reverse = True)
            return max(pos_top3[0] * neg_top3[0] * neg_top3[1], pos_top3[0] * pos_top3[1] * pos_top3[2])

def solution2(A):
    A.sort()
    return max(A[0] * A[1] * A[-1], A[-1] * A[-2] * A[-3])

if __name__ == "__main__":
    print(solution([-1, 1, 1000]))
