# -*- coding: utf-8 -*-
__docformat__ = 'NumPy'

import pandas as pd
import numpy as np
import os, sys

"""
A non-empty zero-indexed array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P < Q < N, is called a slice of array A (notice that the slice contains at least two elements). The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice. To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

For example, array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
contains the following example slices:

slice (1, 2), whose average is (2 + 2) / 2 = 2;
slice (3, 4), whose average is (5 + 1) / 2 = 3;
slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.
The goal is to find the starting position of a slice whose average is minimal.

Write a function:

def solution(A)

that, given a non-empty zero-indexed array A consisting of N integers,
returns the starting position of the slice with the minimal average.
If there is more than one slice with a minimal average,
you should return the smallest starting position of such a slice.

For example, given array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
the function should return 1, as explained above.

Assume that:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−10,000..10,000].
"""

def solution(A):
    # the trick is the minimum average slice length can not exceed 3!
    N = len(A)
    current_best = sum(A[:2])/2
    current_idx = 0
    for i in range(len(A)):
        if i == N - 1:
            return current_idx
        elif i  == N - 2:
            if (A[i] + A[i + 1])/2 < current_best:
                return i
            else:
                return current_idx
        else:
            v1 = (A[i] + A[i + 1]) / 2
            v2 = (A[i] + A[i + 1] + A[i + 2]) / 3
            v = min(v1, v2)
            if v < current_best:
                current_best = v
                current_idx = i
    return current_idx

if __name__ == "__main__":
    print(solution([4, 5]))