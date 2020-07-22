#using fenwick tree to solve
# https://www.codechef.com/problems/BAADSHAH
from copy import deepcopy
def getSum(bitree, i):
    summ = 0;
    i +=
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
        update(bitree, n, i , arr[i])
    return bitree

n,m = map(int,input().split())
arr = list(map(int,input().split()))
bitree = construct(arr)


for i in range(m):
    query = list(map(int,input().split()))
    if query[0]==1:
        ind = query[1]-1
        curr_val = query[2]
        prev_val = arr[ind]
        update(bitree,n,ind,curr_val-prev_val)
        arr[ind]= curr_val
    elif query[0]==2:
        val=query[1]
        l = 0
        r = n-1
        mid=0
        flag = 0
        while (l <= r):
            mid = l + (r - l) //2;
            ans = getSum(bitree,mid);
            if (ans > val):
                r=mid-1
            elif (ans <val):
                l=mid+1
            else:
                pos=mid
                flag=1
                break

        if (flag):
            print("Found",pos+1);
        else:
            print("Not Found");

