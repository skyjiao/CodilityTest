# -*- coding: utf-8 -*-
__docformat__ = 'NumPy'

import pandas as pd
import numpy as np
import os, sys
"""
A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

S is empty;
S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

def solution(S)

that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0,
as explained above.

Assume that:

N is an integer within the range [0..200,000];
string S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")".
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N) (not counting the storage required for input arguments).
"""

class MyStack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

class MyQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

def solution(S):
    stack = MyStack()

    for s in S:
        if s in ["(", "[", "{"]:
            stack.push(s)
            # print(stack.items)
        else:
            if stack.is_empty():
                return False
            else:
                item = stack.pop()
                if not ((item == "(" and s == ")") or (item == "[" and s == "]") or (item == "{" and s == "}")):
                    return False

    return stack.is_empty()


if __name__ == "__main__":
    print(solution("{[()()]}"))

