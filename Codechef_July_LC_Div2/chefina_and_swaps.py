from testInput import input
from sys import maxsize
# from testInput import input
from copy import deepcopy
from collections import Counter

for _ in range(int(input())):
    n = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    freq = {}
    minn = maxsize
    for x in arr1:
        if x not in freq:
            freq[x] = 1
        else:
            freq[x] += 1
        minn = min(minn, x)
    for x in arr2:
        if x not in freq:
            freq[x] = 1
        else:
            freq[x] += 1
        minn = min(minn, x)
    flag = False
    for k, v in freq.items():
        if v & 1:
            flag = True
        freq[k] = v // 2
    if flag:
        print(-1)
        continue
    freq2 = deepcopy(freq)
    for x in arr1:
        if x in freq2:
            if freq2[x] > 0:
                freq2[x] -= 1
    freq1 = deepcopy(freq)
    for x in arr2:
        if x in freq1:
            if freq1[x] > 0:
                freq1[x] -= 1
    keys1 = sorted(list(freq1.keys()))
    keys2 = sorted(list(freq2.keys()))
    temp1 = []
    temp2 = []
    for x in keys1:
        value = freq1[x]
        while value != 0:
            temp1.append(x)
            value -= 1
    for x in keys2:
        value = freq2[x]
        while value != 0:
            temp2.append(x)
            value -= 1
    # print(temp1)
    # print(temp2)
    if len(temp1) != len(temp2):
        print(-1)
        continue
    cost = 0
    temp2 = temp2[::-1]
    for i in range(len(temp1)):
        cost += min(minn * 2, temp2[i], temp1[i])

    print(cost)

