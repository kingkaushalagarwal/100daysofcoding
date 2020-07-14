from copy import deepcopy
# from testInput import input

def getSum(bitree, i):
    summ = 0;
    i += 1
    while i > 0:
        summ += bitree[i]
        i -= i & (-i)
    return summ


def update(bitree, n, i, val):
    i += 1
    while i <= n:
        bitree[i] += val
        i += i & (-i)


def construct(arr):
    n = len(arr)
    bitree = [0] * (n + 1)
    for i in range(n):
        update(bitree, n, i + 1, arr[i])
    return bitree


for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr2 = sorted(arr)
    arr2=arr2[::-1]
    # print("arr : ", arr2)
    d = {}
    for i in range(len(arr)):
        d[arr2[i]] = i
    # print("dictionary: ",d)
    stack = [0] * (n + 1)
    ans =0
    for i in range(len(arr)):
        index = d[arr[i]]
        ans += getSum(stack, index - 1)
        update(stack, n, index, 1)
        # stack[index] += 1
    # print("stack: ",stack)
    print(ans)

