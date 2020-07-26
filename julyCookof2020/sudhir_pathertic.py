import sys
import math
import collections
import operator as op
from collections import deque
from math import gcd, inf, sqrt, pi, cos, sin, ceil, log2
from bisect import bisect_right, bisect_left

# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

from functools import reduce
from sys import stdin, stdout, setrecursionlimit
setrecursionlimit(2**20)


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def ncr(n, r):
    r = min(r, n - r)
    numer = reduce(op.mul, range(n, n - r, -1), 1)
    denom = reduce(op.mul, range(1, r + 1), 1)
    return numer // denom  # or / in Python 2


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return (list(factors))


def isPowerOfTwo(x):
    return (x and (not(x & (x - 1))))


def factors(n):
    return list(set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))

MOD = 1000000007
PMOD = 998244353
ans1 = 1193829614179601806
ans2 = 1931237034633205845
T = 1
T = int(stdin.readline())
for _ in range(T):
    # x, y, z = list(map(int, stdin.readline().rstrip().split()))
    n = int(stdin.readline())
    # a = list(map(int, stdin.readline().rstrip().split()))
    # q = int(stdin.readline())
    # c = list(map(int, stdin.readline().rstrip().split()))
    # s = list(stdin.readline().strip('\n'))
    g, vis, dpt = [], [0] * (n + 1), [0] * (n + 1)
    for i in range(n + 1):
        g.append([])
    nval = n
    while n - 1 > 0:
        u, v = list(map(int, stdin.readline().rstrip().split()))
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
        n -= 1
    q = []
    vis[0] = 1
    q.append(0)
    while len(q) != 0:
        u = q[0]
        q.pop(0)
        for v in g[u]:
            if vis[v] == 0:
                vis[v] = 1
                dpt[v] = dpt[u] + 1
                q.append(v)
    for i in range(nval):
        if dpt[i] % 2 == 0:
            print(ans1, end=' ')
        else:
            print(ans2, end=' ')
    print()
