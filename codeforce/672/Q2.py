# from testInput import input
from collections import Counter
def positionOfFirstBit(num):
    if num==0:
        return 0
    count =0
    while num>0:
        num = num>>1
        count+=1
    return count


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    if n==1:
        print(0)
        continue
    firstBitPosition = []

    for i in range(n):
        firstBitPosition.append(positionOfFirstBit(arr[i]))
    # for i in range(n):
    #     print(arr[i],firstBitPosition[i])
    counter = Counter(firstBitPosition)
    ans =0
    for key,val in counter.items():
        ans+=val*(val-1)//2
    print(ans)