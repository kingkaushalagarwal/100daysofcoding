
import math
import os
import random
import re
import sys
from math import log
from testInput import input

# Complete the solve function below.
def solve(x, l, r):
    length = int(log(r, 2)) + 1
    summ = 0
    for i in range(length, -1, -1):
        if i == length:
            if r & (1 << i) == 0:
                continue
        value = 2 ** i
        if (x & (1 << i) == 0):
            if (value + summ) <= r:
                summ += value
        else:
            if (summ + (2 ** (i) - 1)) < l:
                summ += value
        print(i,summ,value)
    return summ^x


if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        xlr = input().rstrip().split()

        x = int(xlr[0])

        l = int(xlr[1])

        r = int(xlr[2])
        print("x l r",x,l,r)
        result = solve(x, l, r)
        print(result)