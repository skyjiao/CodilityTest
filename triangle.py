# -*- coding: utf-8 -*-
__docformat__ = 'NumPy'

import pandas as pd
import numpy as np
import os, sys

def solution(A):
    # write your code in Python 2.7
    N = len(A)
    if N <= 2:
        return -1
    sorted_A = sorted(A)
    for i in range(N - 2):
        if sorted_A[i] + sorted_A[i + 1] > sorted_A[i + 2]:
            return 1
    return -1

if __name__ == "__main__":
    print(solution([10, 2, 5]))