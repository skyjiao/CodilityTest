# -*- coding: utf-8 -*-
__docformat__ = 'NumPy'

import pandas as pd
import numpy as np
import os, sys

def solution(A):
    # write your code in Python 2.7
    N = len(A)
    if N == 0:
        return 0

    head = A[0]
    tail = sum(A) - head
    current = abs(head - tail)

    for i in range(1, N-1):
        head += A[i]
        tail -= A[i]
        current = min(abs(head - tail), current)

    return current

if __name__ == "__main__":
    # assert(solution([1, 1]) == 0)
    print(solution([1, 1, 1]))